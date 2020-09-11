#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = """
module: vcenter_vm_hardware_adapter_scsi
short_description: Handle resource of type vcenter_vm_hardware_adapter_scsi
description: Handle resource of type vcenter_vm_hardware_adapter_scsi
options:
  adapter:
    description:
    - Virtual SCSI adapter identifier.
    - 'The parameter must be an identifier for the resource type: vcenter.vm.hardware.ScsiAdapter.
      Required with I(state=[''delete'', ''update''])'
    type: str
  bus:
    description:
    - SCSI bus number.
    - If unset, the server will choose an available bus number; if none is available,
      the request will fail.
    type: int
  pci_slot_number:
    description:
    - Address of the SCSI adapter on the PCI bus. If the PCI address is invalid, the
      server will change it when the VM is started or as the device is hot added.
    - If unset, the server will choose an available address when the virtual machine
      is powered on.
    type: int
  sharing:
    choices:
    - NONE
    - PHYSICAL
    - VIRTUAL
    description:
    - The Scsi.Sharing enumerated type defines the valid bus sharing modes for a virtual
      SCSI adapter.
    type: str
  state:
    choices:
    - absent
    - present
    - present
    default: present
    description: []
    type: str
  type:
    choices:
    - BUSLOGIC
    - LSILOGIC
    - LSILOGICSAS
    - PVSCSI
    description:
    - The Scsi.Type enumerated type defines the valid emulation types for a virtual
      SCSI adapter.
    type: str
  vcenter_hostname:
    description:
    - The hostname or IP address of the vSphere vCenter
    - If the value is not specified in the task, the value of environment variable
      C(VMWARE_HOST) will be used instead.
    required: true
    type: str
  vcenter_password:
    description:
    - The vSphere vCenter username
    - If the value is not specified in the task, the value of environment variable
      C(VMWARE_PASSWORD) will be used instead.
    required: true
    type: str
  vcenter_username:
    description:
    - The vSphere vCenter username
    - If the value is not specified in the task, the value of environment variable
      C(VMWARE_USER) will be used instead.
    required: true
    type: str
  vcenter_validate_certs:
    default: true
    description:
    - Allows connection when SSL certificates are not valid. Set to C(false) when
      certificates are not trusted.
    - If the value is not specified in the task, the value of environment variable
      C(VMWARE_VALIDATE_CERTS) will be used instead.
    type: bool
  vm:
    description:
    - Virtual machine identifier.
    - 'The parameter must be an identifier for the resource type: VirtualMachine.'
    type: str
author:
- Goneri Le Bouder (@goneri) <goneri@lebouder.net>
version_added: 1.0.0
requirements:
- python >= 3.6
- aiohttp
"""

EXAMPLES = """
- name: Collect information about a specific VM
  vcenter_vm_info:
    vm: '{{ search_result.value[0].vm }}'
  register: test_vm1_info
- name: Create a SCSI adapter at PCI slot 35
  vcenter_vm_hardware_adapter_scsi:
    vm: '{{ test_vm1_info.id }}'
    pci_slot_number: 35
- name: Drop the SCSI controller
  vcenter_vm_hardware_adapter_scsi:
    vm: '{{ test_vm1_info.id }}'
    pci_slot_number: 35
    state: absent
"""

# This structure describes the format of the data expected by the end-points
PAYLOAD_FORMAT = {
    "list": {"query": {}, "body": {}, "path": {"vm": "vm"}},
    "create": {
        "query": {},
        "body": {
            "bus": "spec/bus",
            "pci_slot_number": "spec/pci_slot_number",
            "sharing": "spec/sharing",
            "type": "spec/type",
        },
        "path": {"vm": "vm"},
    },
    "delete": {"query": {}, "body": {}, "path": {"adapter": "adapter", "vm": "vm"}},
    "get": {"query": {}, "body": {}, "path": {"adapter": "adapter", "vm": "vm"}},
    "update": {
        "query": {},
        "body": {"sharing": "spec/sharing"},
        "path": {"adapter": "adapter", "vm": "vm"},
    },
}

import socket
import json
from ansible.module_utils.basic import env_fallback

try:
    from ansible_collections.cloud.common.plugins.module_utils.turbo.module import (
        AnsibleTurboModule as AnsibleModule,
    )
except ImportError:
    from ansible.module_utils.basic import AnsibleModule
from ansible_collections.vmware.vmware_rest.plugins.module_utils.vmware_rest import (
    exists,
    gen_args,
    get_device_info,
    get_subdevice_type,
    list_devices,
    open_session,
    prepare_payload,
    update_changed_flag,
)


def prepare_argument_spec():
    argument_spec = {
        "vcenter_hostname": dict(
            type="str", required=True, fallback=(env_fallback, ["VMWARE_HOST"]),
        ),
        "vcenter_username": dict(
            type="str", required=True, fallback=(env_fallback, ["VMWARE_USER"]),
        ),
        "vcenter_password": dict(
            type="str",
            required=True,
            no_log=True,
            fallback=(env_fallback, ["VMWARE_PASSWORD"]),
        ),
        "vcenter_validate_certs": dict(
            type="bool",
            required=False,
            default=True,
            fallback=(env_fallback, ["VMWARE_VALIDATE_CERTS"]),
        ),
    }

    argument_spec["adapter"] = {"type": "str"}
    argument_spec["bus"] = {"default": 0, "type": "int"}
    argument_spec["pci_slot_number"] = {"type": "int"}
    argument_spec["sharing"] = {
        "type": "str",
        "choices": ["NONE", "PHYSICAL", "VIRTUAL"],
    }
    argument_spec["state"] = {
        "type": "str",
        "choices": ["absent", "present", "present"],
        "default": "present",
    }
    argument_spec["type"] = {
        "type": "str",
        "choices": ["BUSLOGIC", "LSILOGIC", "LSILOGICSAS", "PVSCSI"],
    }
    argument_spec["vm"] = {"type": "str"}

    return argument_spec


async def main():
    module_args = prepare_argument_spec()
    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)
    session = await open_session(
        vcenter_hostname=module.params["vcenter_hostname"],
        vcenter_username=module.params["vcenter_username"],
        vcenter_password=module.params["vcenter_password"],
    )
    result = await entry_point(module, session)
    module.exit_json(**result)


def build_url(params):

    return (
        "https://{vcenter_hostname}" "/rest/vcenter/vm/{vm}/hardware/adapter/scsi"
    ).format(**params)


async def entry_point(module, session):
    if module.params["state"] == "present":
        if "_create" in globals():
            operation = "create"
        else:
            operation = "update"
    elif module.params["state"] == "absent":
        operation = "delete"
    else:
        operation = module.params["state"]
    func = globals()[("_" + operation)]
    return await func(module.params, session)


async def _create(params, session):
    if params["adapter"]:
        _json = await get_device_info(
            params, session, build_url(params), params["adapter"]
        )
    else:
        _json = await exists(params, session, build_url(params), ["adapter"])
    if _json:
        if "_update" in globals():
            params["adapter"] = _json["id"]
            return await globals()["_update"](params, session)
        else:
            return await update_changed_flag(_json, 200, "get")
    payload = prepare_payload(params, PAYLOAD_FORMAT["create"])
    _url = "https://{vcenter_hostname}/rest/vcenter/vm/{vm}/hardware/adapter/scsi".format(
        **params
    )
    async with session.post(_url, json=payload) as resp:
        try:
            if resp.headers["Content-Type"] == "application/json":
                _json = await resp.json()
        except KeyError:
            _json = {}
        if (resp.status in [200, 201]) and ("value" in _json):
            if isinstance(_json["value"], dict):
                _id = list(_json["value"].values())[0]
            else:
                _id = _json["value"]
            _json = await get_device_info(params, session, _url, _id)
        return await update_changed_flag(_json, resp.status, "create")


async def _delete(params, session):
    _in_query_parameters = PAYLOAD_FORMAT["delete"]["query"].keys()
    payload = payload = prepare_payload(params, PAYLOAD_FORMAT["delete"])
    subdevice_type = get_subdevice_type(
        "/rest/vcenter/vm/{vm}/hardware/adapter/scsi/{adapter}"
    )
    if subdevice_type and (not params[subdevice_type]):
        _json = await exists(params, session, build_url(params))
        if _json:
            params[subdevice_type] = _json["id"]
    _url = "https://{vcenter_hostname}/rest/vcenter/vm/{vm}/hardware/adapter/scsi/{adapter}".format(
        **params
    ) + gen_args(
        params, _in_query_parameters
    )
    async with session.delete(_url, json=payload) as resp:
        try:
            if resp.headers["Content-Type"] == "application/json":
                _json = await resp.json()
        except KeyError:
            _json = {}
        return await update_changed_flag(_json, resp.status, "delete")


async def _update(params, session):
    payload = payload = prepare_payload(params, PAYLOAD_FORMAT["update"])
    _url = "https://{vcenter_hostname}/rest/vcenter/vm/{vm}/hardware/adapter/scsi/{adapter}".format(
        **params
    )
    async with session.get(_url) as resp:
        _json = await resp.json()
        for (k, v) in _json["value"].items():
            if (k in payload) and (payload[k] == v):
                del payload[k]
            elif "spec" in payload:
                if (k in payload["spec"]) and (payload["spec"][k] == v):
                    del payload["spec"][k]
        try:
            if payload["spec"]["upgrade_version"] and (
                "upgrade_policy" not in payload["spec"]
            ):
                payload["spec"]["upgrade_policy"] = _json["value"]["upgrade_policy"]
        except KeyError:
            pass
        if (payload == {}) or (payload == {"spec": {}}):
            _json["id"] = params.get("adapter")
            return await update_changed_flag(_json, resp.status, "get")
    async with session.patch(_url, json=payload) as resp:
        try:
            if resp.headers["Content-Type"] == "application/json":
                _json = await resp.json()
        except KeyError:
            _json = {}
        _json["id"] = params.get("adapter")
        return await update_changed_flag(_json, resp.status, "update")


if __name__ == "__main__":
    import asyncio

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
