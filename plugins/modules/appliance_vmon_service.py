#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: (c) 2021, Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# template: header.j2
# This module is autogenerated by vmware_rest_code_generator.
# See: https://github.com/ansible-collections/vmware_rest_code_generator
from __future__ import absolute_import, division, print_function

__metaclass__ = type


DOCUMENTATION = r"""
module: appliance_vmon_service
short_description: Lists details of services managed by vMon.
description: Lists details of services managed by vMon.
options:
    service:
        description:
        - identifier of the service whose properties are being updated.
        - The parameter must be the id of a resource returned by M(vmware.vmware_rest.appliance_vmon_service).
            Required with I(state=['restart', 'start', 'stop'])
        type: str
    session_timeout:
        description:
        - 'Timeout settings for client session. '
        - 'The maximal number of seconds for the whole operation including connection
            establishment, request sending and response. '
        - The default value is 300s.
        type: float
        version_added: 2.1.0
    startup_type:
        choices:
        - AUTOMATIC
        - DISABLED
        - MANUAL
        description:
        - The I(startup_type) enumerated type defines valid Startup Type for services
            managed by vMon.
        type: str
    state:
        choices:
        - list_details
        - present
        - restart
        - start
        - stop
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
author:
- Ansible Cloud Team (@ansible-collections)
version_added: TODO
requirements:
- vSphere 7.0.2 or greater
- python >= 3.6
- aiohttp
notes:
- Tested on vSphere 7.0.2
"""

EXAMPLES = r"""
"""

RETURN = r"""
"""

# This structure describes the format of the data expected by the end-points
PAYLOAD_FORMAT = {
    "start": {"query": {}, "body": {}, "path": {"service": "service"}},
    "list_details": {"query": {}, "body": {}, "path": {}},
    "stop": {"query": {}, "body": {}, "path": {"service": "service"}},
    "restart": {"query": {}, "body": {}, "path": {"service": "service"}},
    "update": {
        "query": {},
        "body": {"startup_type": "spec/startup_type"},
        "path": {"service": "service"},
    },
}  # pylint: disable=line-too-long

import json
import socket
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
    build_full_device_list,
    exists,
    gen_args,
    get_device_info,
    get_subdevice_type,
    list_devices,
    open_session,
    prepare_payload,
    update_changed_flag,
    session_timeout,
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

    argument_spec["service"] = {"type": "str"}
    argument_spec["startup_type"] = {
        "type": "str",
        "choices": ["AUTOMATIC", "DISABLED", "MANUAL"],
    }
    argument_spec["state"] = {
        "type": "str",
        "choices": ["list_details", "present", "restart", "start", "stop"],
        "default": "present",
    }

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
    return ("https://{vcenter_hostname}" "/rest/appliance/vmon/service").format(
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


async def _list_details(params, session):
    _in_query_parameters = PAYLOAD_FORMAT["list_details"]["query"].keys()
    payload = prepare_payload(params, PAYLOAD_FORMAT["list_details"])
    subdevice_type = get_subdevice_type("/rest/appliance/vmon/service")
    if subdevice_type and not params[subdevice_type]:
        _json = await exists(params, session, build_url(params))
        if _json:
            params[subdevice_type] = _json["id"]
    _url = (
        "https://{vcenter_hostname}"
        # aa
        "/rest/appliance/vmon/service"
    ).format(**params) + gen_args(params, _in_query_parameters)
    async with session.get(_url, json=payload, **session_timeout(params)) as resp:
        try:
            if resp.headers["Content-Type"] == "application/json":
                _json = await resp.json()
        except KeyError:
            _json = {}
        if "value" not in _json:  # 7.0.2
            _json = {"value": _json}

        return await update_changed_flag(_json, resp.status, "list_details")


async def _restart(params, session):
    _in_query_parameters = PAYLOAD_FORMAT["restart"]["query"].keys()
    payload = prepare_payload(params, PAYLOAD_FORMAT["restart"])
    subdevice_type = get_subdevice_type(
        "/rest/appliance/vmon/service/{service}/restart"
    )
    if subdevice_type and not params[subdevice_type]:
        _json = await exists(params, session, build_url(params))
        if _json:
            params[subdevice_type] = _json["id"]
    _url = (
        "https://{vcenter_hostname}"
        # aa
        "/rest/appliance/vmon/service/{service}/restart"
    ).format(**params) + gen_args(params, _in_query_parameters)
    async with session.post(_url, json=payload, **session_timeout(params)) as resp:
        try:
            if resp.headers["Content-Type"] == "application/json":
                _json = await resp.json()
        except KeyError:
            _json = {}
        if "value" not in _json:  # 7.0.2
            _json = {"value": _json}

        return await update_changed_flag(_json, resp.status, "restart")


async def _start(params, session):
    _in_query_parameters = PAYLOAD_FORMAT["start"]["query"].keys()
    payload = prepare_payload(params, PAYLOAD_FORMAT["start"])
    subdevice_type = get_subdevice_type("/rest/appliance/vmon/service/{service}/start")
    if subdevice_type and not params[subdevice_type]:
        _json = await exists(params, session, build_url(params))
        if _json:
            params[subdevice_type] = _json["id"]
    _url = (
        "https://{vcenter_hostname}"
        # aa
        "/rest/appliance/vmon/service/{service}/start"
    ).format(**params) + gen_args(params, _in_query_parameters)
    async with session.post(_url, json=payload, **session_timeout(params)) as resp:
        try:
            if resp.headers["Content-Type"] == "application/json":
                _json = await resp.json()
        except KeyError:
            _json = {}
        if "value" not in _json:  # 7.0.2
            _json = {"value": _json}

        return await update_changed_flag(_json, resp.status, "start")


async def _stop(params, session):
    _in_query_parameters = PAYLOAD_FORMAT["stop"]["query"].keys()
    payload = prepare_payload(params, PAYLOAD_FORMAT["stop"])
    subdevice_type = get_subdevice_type("/rest/appliance/vmon/service/{service}/stop")
    if subdevice_type and not params[subdevice_type]:
        _json = await exists(params, session, build_url(params))
        if _json:
            params[subdevice_type] = _json["id"]
    _url = (
        "https://{vcenter_hostname}"
        # aa
        "/rest/appliance/vmon/service/{service}/stop"
    ).format(**params) + gen_args(params, _in_query_parameters)
    async with session.post(_url, json=payload, **session_timeout(params)) as resp:
        try:
            if resp.headers["Content-Type"] == "application/json":
                _json = await resp.json()
        except KeyError:
            _json = {}
        if "value" not in _json:  # 7.0.2
            _json = {"value": _json}

        return await update_changed_flag(_json, resp.status, "stop")


async def _update(params, session):
    payload = prepare_payload(params, PAYLOAD_FORMAT["update"])
    _url = (
        "https://{vcenter_hostname}" "/rest/appliance/vmon/service/{service}"
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
            _json["id"] = params.get("service")
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

        _json["id"] = params.get("service")
        return await update_changed_flag(_json, resp.status, "update")


if __name__ == "__main__":
    import asyncio

    current_loop = asyncio.get_event_loop_policy().get_event_loop()
    current_loop.run_until_complete(main())
