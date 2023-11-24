#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: (c) 2021, Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# template: header.j2
# This module is autogenerated using the ansible.content_builder.
# See: https://github.com/ansible-community/ansible.content_builder


DOCUMENTATION = r"""
module: vcenter_vm_hardware_serial
short_description: Adds a virtual serial port to the virtual machine.
description: Adds a virtual serial port to the virtual machine.
options:
    allow_guest_control:
        description:
        - Flag indicating whether the guest can connect and disconnect the device.
        - If unset, the value is unchanged.
        type: bool
    backing:
        description:
        - Physical resource backing for the virtual serial port.
        - If unset, defaults to automatic detection of a suitable host device. Required
            with I(state=['present'])
        - 'Valid attributes are:'
        - ' - C(type) (str): This option defines the valid backing types for a virtual
            serial port. ([''present''])'
        - '   This key is required with [''present''].'
        - '   - Accepted values:'
        - '     - FILE'
        - '     - HOST_DEVICE'
        - '     - NETWORK_CLIENT'
        - '     - NETWORK_SERVER'
        - '     - PIPE_CLIENT'
        - '     - PIPE_SERVER'
        - ' - C(file) (str): Path of the file backing the virtual serial port.'
        - This field is optional and it is only relevant when the value of I(type)
            is FILE. (['present'])
        - ' - C(host_device) (str): Name of the device backing the virtual serial
            port. '
        - ''
        - ''
        - If unset, the virtual serial port will be configured to automatically detect
            a suitable host device. (['present'])
        - ' - C(pipe) (str): Name of the pipe backing the virtual serial port.'
        - This field is optional and it is only relevant when the value of I(type)
            is one of PIPE_SERVER or PIPE_CLIENT. (['present'])
        - ' - C(no_rx_loss) (bool): Flag that enables optimized data transfer over
            the pipe. When the value is true, the host buffers data to prevent data
            overrun. This allows the virtual machine to read all of the data transferred
            over the pipe with no data loss.'
        - If unset, defaults to false. (['present'])
        - ' - C(network_location) (str): URI specifying the location of the network
            service backing the virtual serial port. '
        - '   - If I(type) is NETWORK_SERVER, this field is the location used by clients
            to connect to this server. The hostname part of the URI should either
            be empty or should specify the address of the host on which the virtual
            machine is running.'
        - '   - If I(type) is NETWORK_CLIENT, this field is the location used by the
            virtual machine to connect to the remote server.'
        - ' '
        - This field is optional and it is only relevant when the value of I(type)
            is one of NETWORK_SERVER or NETWORK_CLIENT. (['present'])
        - ' - C(proxy) (str): Proxy service that provides network access to the network
            backing. If set, the virtual machine initiates a connection with the proxy
            service and forwards the traffic to the proxy.'
        - If unset, no proxy service should be used. (['present'])
        type: dict
    label:
        description:
        - The name of the item
        type: str
    port:
        description:
        - Virtual serial port identifier.
        - The parameter must be the id of a resource returned by M(vmware.vmware_rest.vcenter_vm_hardware_serial).
            Required with I(state=['absent', 'connect', 'disconnect', 'present'])
        type: str
    session_timeout:
        description:
        - 'Timeout settings for client session. '
        - 'The maximal number of seconds for the whole operation including connection
            establishment, request sending and response. '
        - The default value is 300s.
        type: float
        version_added: 2.1.0
    start_connected:
        description:
        - Flag indicating whether the virtual device should be connected whenever
            the virtual machine is powered on.
        - If unset, the value is unchanged.
        type: bool
    state:
        choices:
        - absent
        - connect
        - disconnect
        - present
        default: present
        description: []
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
    yield_on_poll:
        description:
        - 'CPU yield behavior. If set to true, the virtual machine will periodically
            relinquish the processor if its sole task is polling the virtual serial
            port. The amount of time it takes to regain the processor will depend
            on the degree of other virtual machine activity on the host. '
        - ' This field may be modified at any time, and changes applied to a connected
            virtual serial port take effect immediately.'
        - ''
        - If unset, the value is unchanged.
        type: bool
author:
- Ansible Cloud Team (@ansible-collections)
version_added: 0.1.0
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

- name: Create a new serial port
  vmware.vmware_rest.vcenter_vm_hardware_serial:
    vm: '{{ test_vm1_info.id }}'
    label: Serial port 2
    allow_guest_control: true
  register: _result

- name: Create another serial port with a label
  vmware.vmware_rest.vcenter_vm_hardware_serial:
    vm: '{{ test_vm1_info.id }}'
    label: Serial port 2
    allow_guest_control: true
  register: _result

- name: Create an existing serial port (label)
  vmware.vmware_rest.vcenter_vm_hardware_serial:
    vm: '{{ test_vm1_info.id }}'
    label: Serial port 1
    allow_guest_control: true
  register: _result

- name: Get an existing serial port (label)
  vmware.vmware_rest.vcenter_vm_hardware_serial_info:
    vm: '{{ test_vm1_info.id }}'
    label: Serial port 1
  register: serial_port_1

- name: Delete an existing serial port (port id)
  vmware.vmware_rest.vcenter_vm_hardware_serial:
    vm: '{{ test_vm1_info.id }}'
    port: '{{ serial_port_1.id }}'
    state: absent
  register: _result

- name: Delete an existing serial port (label)
  vmware.vmware_rest.vcenter_vm_hardware_serial:
    vm: '{{ test_vm1_info.id }}'
    label: Serial port 2
    state: absent
  register: _result
"""

RETURN = r"""
# content generated by the update_return_section callback# task: Create an existing serial port (label)
id:
  description: moid of the resource
  returned: On success
  sample: '9000'
  type: str
value:
  description: Create an existing serial port (label)
  returned: On success
  sample:
    allow_guest_control: 1
    backing:
      auto_detect: 1
      host_device: ''
      type: HOST_DEVICE
    label: Serial port 1
    start_connected: 0
    state: NOT_CONNECTED
    yield_on_poll: 0
  type: dict
"""

# This structure describes the format of the data expected by the end-points
PAYLOAD_FORMAT = {
    "delete": {"query": {}, "body": {}, "path": {"port": "port", "vm": "vm"}},
    "create": {
        "query": {},
        "body": {
            "allow_guest_control": "allow_guest_control",
            "backing": "backing",
            "start_connected": "start_connected",
            "yield_on_poll": "yield_on_poll",
        },
        "path": {"vm": "vm"},
    },
    "update": {
        "query": {},
        "body": {
            "allow_guest_control": "allow_guest_control",
            "backing": "backing",
            "start_connected": "start_connected",
            "yield_on_poll": "yield_on_poll",
        },
        "path": {"port": "port", "vm": "vm"},
    },
    "disconnect": {"query": {}, "body": {}, "path": {"port": "port", "vm": "vm"}},
    "connect": {"query": {}, "body": {}, "path": {"port": "port", "vm": "vm"}},
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
    session_timeout,
    update_changed_flag,
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

    argument_spec["allow_guest_control"] = {"type": "bool"}
    argument_spec["backing"] = {"type": "dict"}
    argument_spec["label"] = {"type": "str"}
    argument_spec["port"] = {"type": "str"}
    argument_spec["start_connected"] = {"type": "bool"}
    argument_spec["state"] = {
        "type": "str",
        "choices": ["absent", "connect", "disconnect", "present"],
        "default": "present",
    }
    argument_spec["vm"] = {"required": True, "type": "str"}
    argument_spec["yield_on_poll"] = {"type": "bool"}

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
    return ("https://{vcenter_hostname}" "/api/vcenter/vm/{vm}/hardware/serial").format(
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


async def _connect(params, session):
    _in_query_parameters = PAYLOAD_FORMAT["connect"]["query"].keys()
    payload = prepare_payload(params, PAYLOAD_FORMAT["connect"])
    subdevice_type = get_subdevice_type(
        "/api/vcenter/vm/{vm}/hardware/serial/{port}?action=connect"
    )
    if subdevice_type and not params[subdevice_type]:
        _json = await exists(params, session, build_url(params))
        if _json:
            params[subdevice_type] = _json["id"]
    _url = (
        "https://{vcenter_hostname}"
        # aa
        "/api/vcenter/vm/{vm}/hardware/serial/{port}?action=connect"
    ).format(**params) + gen_args(params, _in_query_parameters)
    async with session.post(_url, json=payload, **session_timeout(params)) as resp:
        try:
            if resp.headers["Content-Type"] == "application/json":
                _json = await resp.json()
        except KeyError:
            _json = {}
        if "value" not in _json:  # 7.0.2
            _json = {"value": _json}

        return await update_changed_flag(_json, resp.status, "connect")


async def _create(params, session):
    lookup_url = per_id_url = build_url(params)
    uniquity_keys = ["port"]
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
                return await get_device_info(session, url, _json[0]["port"])

    _json = None

    if params["port"]:
        _json = await get_device_info(session, build_url(params), params["port"])

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
            params["port"] = _json["id"]
            return await globals()["_update"](params, session)

        return await update_changed_flag(_json, 200, "get")

    payload = prepare_payload(params, PAYLOAD_FORMAT["create"])
    _url = ("https://{vcenter_hostname}" "/api/vcenter/vm/{vm}/hardware/serial").format(
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
    subdevice_type = get_subdevice_type("/api/vcenter/vm/{vm}/hardware/serial/{port}")
    if subdevice_type and not params[subdevice_type]:
        _json = await exists(params, session, build_url(params))
        if _json:
            params[subdevice_type] = _json["id"]
    _url = (
        "https://{vcenter_hostname}" "/api/vcenter/vm/{vm}/hardware/serial/{port}"
    ).format(**params) + gen_args(params, _in_query_parameters)
    async with session.delete(_url, json=payload, **session_timeout(params)) as resp:
        try:
            if resp.headers["Content-Type"] == "application/json":
                _json = await resp.json()
        except KeyError:
            _json = {}
        return await update_changed_flag(_json, resp.status, "delete")


async def _disconnect(params, session):
    _in_query_parameters = PAYLOAD_FORMAT["disconnect"]["query"].keys()
    payload = prepare_payload(params, PAYLOAD_FORMAT["disconnect"])
    subdevice_type = get_subdevice_type(
        "/api/vcenter/vm/{vm}/hardware/serial/{port}?action=disconnect"
    )
    if subdevice_type and not params[subdevice_type]:
        _json = await exists(params, session, build_url(params))
        if _json:
            params[subdevice_type] = _json["id"]
    _url = (
        "https://{vcenter_hostname}"
        # aa
        "/api/vcenter/vm/{vm}/hardware/serial/{port}?action=disconnect"
    ).format(**params) + gen_args(params, _in_query_parameters)
    async with session.post(_url, json=payload, **session_timeout(params)) as resp:
        try:
            if resp.headers["Content-Type"] == "application/json":
                _json = await resp.json()
        except KeyError:
            _json = {}
        if "value" not in _json:  # 7.0.2
            _json = {"value": _json}

        return await update_changed_flag(_json, resp.status, "disconnect")


async def _update(params, session):
    payload = prepare_payload(params, PAYLOAD_FORMAT["update"])
    _url = (
        "https://{vcenter_hostname}" "/api/vcenter/vm/{vm}/hardware/serial/{port}"
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
            _json["id"] = params.get("port")
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

        _json["id"] = params.get("port")
        return await update_changed_flag(_json, resp.status, "update")


if __name__ == "__main__":
    import asyncio

    current_loop = asyncio.get_event_loop_policy().get_event_loop()
    current_loop.run_until_complete(main())
