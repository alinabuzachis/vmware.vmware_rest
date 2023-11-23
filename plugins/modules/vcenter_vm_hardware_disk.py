#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: (c) 2021, Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# template: header.j2
# This module is autogenerated using the ansible.content_builder.
# See: https://github.com/ansible-community/ansible.content_builder


DOCUMENTATION = r"""
module: vcenter_vm_hardware_disk
short_description: Adds a virtual disk to the virtual machine
description: Adds a virtual disk to the virtual machine. While adding the virtual
    disk, a new VMDK file may be created or an existing VMDK file may be used to back
    the virtual disk.
options:
    backing:
        description:
        - Existing physical resource backing for the virtual disk. Exactly one of
            I(backing) or I(new_vmdk) must be specified.
        - If unset, the virtual disk will not be connected to an existing backing.
            Required with I(state=['present'])
        - 'Valid attributes are:'
        - ' - C(type) (str): This option defines the valid backing types for a virtual
            disk. ([''present''])'
        - '   This key is required with [''present''].'
        - '   - Accepted values:'
        - '     - VMDK_FILE'
        - ' - C(vmdk_file) (str): Path of the VMDK file backing the virtual disk.'
        - This field is optional and it is only relevant when the value of I(type)
            is VMDK_FILE. (['present'])
        type: dict
    disk:
        description:
        - Virtual disk identifier.
        - The parameter must be the id of a resource returned by M(vmware.vmware_rest.vcenter_vm_hardware_disk).
            Required with I(state=['absent', 'present'])
        type: str
    ide:
        description:
        - Address for attaching the device to a virtual IDE adapter.
        - If unset, the server will choose an available address; if none is available,
            the request will fail.
        - 'Valid attributes are:'
        - ' - C(primary) (bool): Flag specifying whether the device should be attached
            to the primary or secondary IDE adapter of the virtual machine.'
        - If unset, the server will choose a adapter with an available connection.
            If no IDE connections are available, the request will be rejected. (['present'])
        - ' - C(master) (bool): Flag specifying whether the device should be the master
            or slave device on the IDE adapter.'
        - If unset, the server will choose an available connection type. If no IDE
            connections are available, the request will be rejected. (['present'])
        type: dict
    label:
        description:
        - The name of the item
        type: str
    new_vmdk:
        description:
        - Specification for creating a new VMDK backing for the virtual disk. Exactly
            one of I(backing) or I(new_vmdk) must be specified.
        - If unset, a new VMDK backing will not be created.
        - 'Valid attributes are:'
        - ' - C(name) (str): Base name of the VMDK file. The name should not include
            the ''.vmdk'' file extension.'
        - If unset, a name (derived from the name of the virtual machine) will be
            chosen by the server. (['present'])
        - ' - C(capacity) (int): Capacity of the virtual disk backing in bytes.'
        - If unset, defaults to a guest-specific capacity. (['present'])
        - ' - C(storage_policy) (dict): The I(storage_policy_spec) structure contains
            information about the storage policy that is to be associated the with
            VMDK file.'
        - 'If unset the default storage policy of the target datastore (if applicable)
            is applied. Currently a default storage policy is only supported by object
            based datastores : VVol & vSAN. For non- object datastores, if unset then
            no storage policy would be associated with the VMDK file. ([''present''])'
        - '   - Accepted keys:'
        - '     - policy (string): Identifier of the storage policy which should be
            associated with the VMDK file.'
        - 'When clients pass a value of this structure as a parameter, the field must
            be the id of a resource returned by M(vmware.vmware_rest.vcenter_storage_policies). '
        type: dict
    nvme:
        description:
        - Address for attaching the device to a virtual NVMe adapter.
        - If unset, the server will choose an available address; if none is available,
            the request will fail. Required with I(state=['present'])
        - 'Valid attributes are:'
        - ' - C(bus) (int): Bus number of the adapter to which the device should be
            attached. ([''present''])'
        - '   This key is required with [''present''].'
        - ' - C(unit) (int): Unit number of the device.'
        - If unset, the server will choose an available unit number on the specified
            adapter. If there are no available connections on the adapter, the request
            will be rejected. (['present'])
        type: dict
    sata:
        description:
        - Address for attaching the device to a virtual SATA adapter.
        - If unset, the server will choose an available address; if none is available,
            the request will fail. Required with I(state=['present'])
        - 'Valid attributes are:'
        - ' - C(bus) (int): Bus number of the adapter to which the device should be
            attached. ([''present''])'
        - '   This key is required with [''present''].'
        - ' - C(unit) (int): Unit number of the device.'
        - If unset, the server will choose an available unit number on the specified
            adapter. If there are no available connections on the adapter, the request
            will be rejected. (['present'])
        type: dict
    scsi:
        description:
        - Address for attaching the device to a virtual SCSI adapter.
        - If unset, the server will choose an available address; if none is available,
            the request will fail. Required with I(state=['present'])
        - 'Valid attributes are:'
        - ' - C(bus) (int): Bus number of the adapter to which the device should be
            attached. ([''present''])'
        - '   This key is required with [''present''].'
        - ' - C(unit) (int): Unit number of the device.'
        - If unset, the server will choose an available unit number on the specified
            adapter. If there are no available connections on the adapter, the request
            will be rejected. (['present'])
        type: dict
    session_timeout:
        description:
        - 'Timeout settings for client session. '
        - 'The maximal number of seconds for the whole operation including connection
            establishment, request sending and response. '
        - The default value is 300s.
        type: float
        version_added: 2.1.0
    state:
        choices:
        - absent
        - present
        default: present
        description: []
        type: str
    type:
        choices:
        - IDE
        - NVME
        - SATA
        - SCSI
        description:
        - The I(host_bus_adapter_type) enumerated type defines the valid types of
            host bus adapters that may be used for attaching a virtual storage device
            to a virtual machine.
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
        - The vSphere vCenter password
        - If the value is not specified in the task, the value of environment variable
            C(VMWARE_PASSWORD) will be used instead.
        required: true
        type: str
    vcenter_rest_log_file:
        description:
        - 'You can use this optional parameter to set the location of a log file. '
        - 'This file will be used to record the HTTP REST interaction. '
        - 'The file will be stored on the host that run the module. '
        - 'If the value is not specified in the task, the value of '
        - environment variable C(VMWARE_REST_LOG_FILE) will be used instead.
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
        - The parameter must be the id of a resource returned by M(vmware.vmware_rest.vcenter_vm_info).
            This parameter is mandatory.
        required: true
        type: str
author:
- Ansible Cloud Team (@ansible-collections)
version_added: 2.0.0
requirements:
- vSphere 7.0.3 or greater
- python >= 3.6
- aiohttp
notes:
- Tested on vSphere 7.0.3
"""

EXAMPLES = r"""
- name: Look up the VM called test_vm1 in the inventory
  register: search_result
  vmware.vmware_rest.vcenter_vm_info:
    filter_names:
    - test_vm1

- name: Collect information about a specific VM
  vmware.vmware_rest.vcenter_vm_info:
    vm: '{{ search_result.value[0].vm }}'
  register: test_vm1_info

- name: Create a new disk
  vmware.vmware_rest.vcenter_vm_hardware_disk:
    vm: '{{ test_vm1_info.id }}'
    type: SATA
    new_vmdk:
      capacity: 320000
  register: my_new_disk

- name: Delete the disk
  vmware.vmware_rest.vcenter_vm_hardware_disk:
    vm: '{{ test_vm1_info.id }}'
    disk: '{{ my_new_disk.id }}'
    state: absent
  register: _result
"""

RETURN = r"""
"""

# This structure describes the format of the data expected by the end-points
PAYLOAD_FORMAT = {
    "update": {
        "query": {},
        "body": {"backing": "backing"},
        "path": {"disk": "disk", "vm": "vm"},
    },
    "delete": {"query": {}, "body": {}, "path": {"disk": "disk", "vm": "vm"}},
    "create": {
        "query": {},
        "body": {
            "backing": "backing",
            "ide": "ide",
            "new_vmdk": "new_vmdk",
            "nvme": "nvme",
            "sata": "sata",
            "scsi": "scsi",
            "type": "type",
        },
        "path": {"vm": "vm"},
    },
}  # pylint: disable=line-too-long

from ansible.module_utils.basic import env_fallback

try:
    from ansible_collections.cloud.common.plugins.module_utils.turbo.exceptions import (
        EmbeddedModuleFailure,
    )
    from ansible_collections.cloud.common.plugins.module_utils.turbo.module import (
        AnsibleTurboModule as AnsibleModule,
    )

    AnsibleModule.collection_name = "vmware.vmware_rest"
except ImportError:
    from ansible.module_utils.basic import AnsibleModule
from ansible_collections.vmware.vmware_rest.plugins.module_utils.vmware_rest import (
    exists,
    gen_args,
    get_device_info,
    get_subdevice_type,
    open_session,
    prepare_payload,
    update_changed_flag,
    session_timeout,
)


def prepare_argument_spec():
    argument_spec = {
        "vcenter_hostname": dict(
            type="str",
            required=True,
            fallback=(env_fallback, ["VMWARE_HOST"]),
        ),
        "vcenter_username": dict(
            type="str",
            required=True,
            fallback=(env_fallback, ["VMWARE_USER"]),
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
        "vcenter_rest_log_file": dict(
            type="str",
            required=False,
            fallback=(env_fallback, ["VMWARE_REST_LOG_FILE"]),
        ),
        "session_timeout": dict(
            type="float",
            required=False,
            fallback=(env_fallback, ["VMWARE_SESSION_TIMEOUT"]),
        ),
    }

    argument_spec["backing"] = {"type": "dict"}
    argument_spec["disk"] = {"type": "str"}
    argument_spec["ide"] = {"type": "dict"}
    argument_spec["label"] = {"type": "str"}
    argument_spec["new_vmdk"] = {"type": "dict"}
    argument_spec["nvme"] = {"type": "dict"}
    argument_spec["sata"] = {"type": "dict"}
    argument_spec["scsi"] = {"type": "dict"}
    argument_spec["state"] = {
        "type": "str",
        "choices": ["absent", "present"],
        "default": "present",
    }
    argument_spec["type"] = {"type": "str", "choices": ["IDE", "NVME", "SATA", "SCSI"]}
    argument_spec["vm"] = {"required": True, "type": "str"}

    return argument_spec


async def main():
    required_if = list([])

    module_args = prepare_argument_spec()
    module = AnsibleModule(
        argument_spec=module_args, required_if=required_if, supports_check_mode=True
    )
    if not module.params["vcenter_hostname"]:
        module.fail_json("vcenter_hostname cannot be empty")
    if not module.params["vcenter_username"]:
        module.fail_json("vcenter_username cannot be empty")
    if not module.params["vcenter_password"]:
        module.fail_json("vcenter_password cannot be empty")
    try:
        session = await open_session(
            vcenter_hostname=module.params["vcenter_hostname"],
            vcenter_username=module.params["vcenter_username"],
            vcenter_password=module.params["vcenter_password"],
            validate_certs=module.params["vcenter_validate_certs"],
            log_file=module.params["vcenter_rest_log_file"],
        )
    except EmbeddedModuleFailure as err:
        module.fail_json(err.get_message())
    result = await entry_point(module, session)
    module.exit_json(**result)


# template: default_module.j2
def build_url(params):
    return ("https://{vcenter_hostname}" "/api/vcenter/vm/{vm}/hardware/disk").format(
        **params
    )


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

    func = globals()["_" + operation]

    return await func(module.params, session)


async def _create(params, session):
    lookup_url = per_id_url = build_url(params)
    uniquity_keys = ["disk"]
    comp_func = None

    async def lookup_with_filters(params, session, url):
        # e.g: for the datacenter resources
        if "folder" not in params:
            return
        if "name" not in params:
            return
        async with session.get(
            f"{url}?names={params['name']}&folders={params['folder']}"
        ) as resp:
            _json = await resp.json()
            if isinstance(_json, list) and len(_json) == 1:
                return await get_device_info(session, url, _json[0]["disk"])

    _json = None

    if params["disk"]:
        _json = await get_device_info(session, build_url(params), params["disk"])

    if not _json and (uniquity_keys or comp_func):
        _json = await exists(
            params,
            session,
            url=lookup_url,
            uniquity_keys=uniquity_keys,
            per_id_url=per_id_url,
            comp_func=comp_func,
        )

    if not _json:
        _json = await lookup_with_filters(params, session, build_url(params))

    if _json:
        if "value" not in _json:  # 7.0.2+
            _json = {"value": _json}
        if "_update" in globals():
            params["disk"] = _json["id"]
            return await globals()["_update"](params, session)

        return await update_changed_flag(_json, 200, "get")

    payload = prepare_payload(params, PAYLOAD_FORMAT["create"])
    _url = ("https://{vcenter_hostname}" "/api/vcenter/vm/{vm}/hardware/disk").format(
        **params
    )
    async with session.post(_url, json=payload, **session_timeout(params)) as resp:
        if resp.status == 500:
            text = await resp.text()
            raise EmbeddedModuleFailure(
                f"Request has failed: status={resp.status}, {text}"
            )
        try:
            if resp.headers["Content-Type"] == "application/json":
                _json = await resp.json()
        except KeyError:
            _json = {}

        if (resp.status in [200, 201]) and "error" not in _json:
            if isinstance(_json, str):  # 7.0.2 and greater
                _id = _json  # TODO: fetch the object
            elif isinstance(_json, dict) and "value" not in _json:
                _id = list(_json["value"].values())[0]
            elif isinstance(_json, dict) and "value" in _json:
                _id = _json["value"]
            _json_device_info = await get_device_info(session, _url, _id)
            if _json_device_info:
                _json = _json_device_info

        return await update_changed_flag(_json, resp.status, "create")


async def _delete(params, session):
    _in_query_parameters = PAYLOAD_FORMAT["delete"]["query"].keys()
    payload = prepare_payload(params, PAYLOAD_FORMAT["delete"])
    subdevice_type = get_subdevice_type("/api/vcenter/vm/{vm}/hardware/disk/{disk}")
    if subdevice_type and not params[subdevice_type]:
        _json = await exists(params, session, build_url(params))
        if _json:
            params[subdevice_type] = _json["id"]
    _url = (
        "https://{vcenter_hostname}" "/api/vcenter/vm/{vm}/hardware/disk/{disk}"
    ).format(**params) + gen_args(params, _in_query_parameters)
    async with session.delete(_url, json=payload, **session_timeout(params)) as resp:
        try:
            if resp.headers["Content-Type"] == "application/json":
                _json = await resp.json()
        except KeyError:
            _json = {}
        return await update_changed_flag(_json, resp.status, "delete")


async def _update(params, session):
    payload = prepare_payload(params, PAYLOAD_FORMAT["update"])
    _url = (
        "https://{vcenter_hostname}" "/api/vcenter/vm/{vm}/hardware/disk/{disk}"
    ).format(**params)
    async with session.get(_url, **session_timeout(params)) as resp:
        _json = await resp.json()
        if "value" in _json:
            value = _json["value"]
        else:  # 7.0.2 and greater
            value = _json
        for k, v in value.items():
            if k in payload:
                if isinstance(payload[k], dict) and isinstance(v, dict):
                    to_delete = True
                    for _k in list(payload[k].keys()):
                        if payload[k][_k] != v.get(_k):
                            to_delete = False
                    if to_delete:
                        del payload[k]
                elif payload[k] == v:
                    del payload[k]
                elif payload[k] == {}:
                    del payload[k]

        if payload == {} or payload == {"spec": {}}:
            # Nothing has changed
            if "value" not in _json:  # 7.0.2
                _json = {"value": _json}
            _json["id"] = params.get("disk")
            return await update_changed_flag(_json, resp.status, "get")
    async with session.patch(_url, json=payload, **session_timeout(params)) as resp:
        try:
            if resp.headers["Content-Type"] == "application/json":
                _json = await resp.json()
        except KeyError:
            _json = {}
        if "value" not in _json:  # 7.0.2
            _json = {"value": _json}

        # e.g: content_configuration
        if not _json and resp.status == 204:
            async with session.get(_url, **session_timeout(params)) as resp_get:
                _json_get = await resp_get.json()
                if _json_get:
                    _json = _json_get

        _json["id"] = params.get("disk")
        return await update_changed_flag(_json, resp.status, "update")


if __name__ == "__main__":
    import asyncio

    current_loop = asyncio.get_event_loop_policy().get_event_loop()
    current_loop.run_until_complete(main())
