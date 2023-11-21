#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: (c) 2021, Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# template: header.j2
# This module is autogenerated using the ansible.content_builder.
# See: https://github.com/ansible-community/ansible.content_builder


DOCUMENTATION = r"""
module: vcenter_host_info
short_description: Returns information about at most 2500 visible (subject to permission
    checks) hosts in vCenter matching the {@link FilterSpec}.
description: Returns information about at most 2500 visible (subject to permission
    checks) hosts in vCenter matching the {@link FilterSpec}.
options:
    clusters:
        description:
        - Clusters that must contain the hosts for the hosts to match the filter.
        elements: str
        type: list
    connection_states:
        description:
        - Connection states that a host must be in to match the filter (see {@link
            Summary#connectionState}.
        elements: str
        type: list
    datacenters:
        aliases:
        - filter_datacenters
        description:
        - Datacenters that must contain the hosts for the hosts to match the filter.
        elements: str
        type: list
    folders:
        aliases:
        - filter_folders
        description:
        - Folders that must contain the hosts for the hosts to match the filter.
        elements: str
        type: list
    hosts:
        description:
        - Identifiers of hosts that can match the filter.
        elements: str
        type: list
    names:
        aliases:
        - filter_names
        description:
        - Names that hosts must have to match the filter (see {@link Summary#name}).
        elements: str
        type: list
    session_timeout:
        description:
        - 'Timeout settings for client session. '
        - 'The maximal number of seconds for the whole operation including connection
            establishment, request sending and response. '
        - The default value is 300s.
        type: float
        version_added: 2.1.0
    standalone:
        description:
        - If true, only hosts that are not part of a cluster can match the filter,
            and if false, only hosts that are are part of a cluster can match the
            filter.
        type: bool
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
version_added: 0.1.0
requirements:
- vSphere 7.0.2 or greater
- python >= 3.6
- aiohttp
notes:
- Tested on vSphere 7.0.2
"""

EXAMPLES = r"""
- name: Get a list of the hosts
  vmware.vmware_rest.vcenter_host_info:
  register: my_hosts
"""

RETURN = r"""
# content generated by the update_return_section callback# task: Get a list of the hosts
value:
  description: Get a list of the hosts
  returned: On success
  sample:
  - connection_state: CONNECTED
    host: host-1013
    name: esxi1.test
    power_state: POWERED_ON
  type: list
"""

# This structure describes the format of the data expected by the end-points
PAYLOAD_FORMAT = {
    "list": {
        "query": {
            "clusters": "clusters",
            "connection_states": "connection_states",
            "datacenters": "datacenters",
            "folders": "folders",
            "hosts": "hosts",
            "names": "names",
            "standalone": "standalone",
        },
        "body": {},
        "path": {},
    }
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
    build_full_device_list,
    exists,
    gen_args,
    open_session,
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

    argument_spec["clusters"] = {"type": "list", "elements": "str"}
    argument_spec["connection_states"] = {"type": "list", "elements": "str"}
    argument_spec["datacenters"] = {
        "aliases": ["filter_datacenters"],
        "type": "list",
        "elements": "str",
    }
    argument_spec["folders"] = {
        "aliases": ["filter_folders"],
        "type": "list",
        "elements": "str",
    }
    argument_spec["hosts"] = {"type": "list", "elements": "str"}
    argument_spec["names"] = {
        "aliases": ["filter_names"],
        "type": "list",
        "elements": "str",
    }
    argument_spec["standalone"] = {"type": "bool"}

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


# template: info_list_and_get_module.j2
def build_url(params):
    import yarl

    if params.get("host"):
        _in_query_parameters = PAYLOAD_FORMAT["get"]["query"].keys()
        return yarl.URL(
            ("https://{vcenter_hostname}" "/api/vcenter/host/").format(**params)
            + params["host"]
            + gen_args(params, _in_query_parameters),
            encoded=True,
        )
    _in_query_parameters = PAYLOAD_FORMAT["list"]["query"].keys()
    return yarl.URL(
        ("https://{vcenter_hostname}" "/api/vcenter/host").format(**params)
        + gen_args(params, _in_query_parameters),
        encoded=True,
    )


async def entry_point(module, session):
    url = build_url(module.params)
    async with session.get(url, **session_timeout(module.params)) as resp:
        _json = await resp.json()

        if "value" not in _json:  # 7.0.2+
            _json = {"value": _json}

        if module.params.get("host"):
            _json["id"] = module.params.get("host")
        elif module.params.get("label"):  # TODO extend the list of filter
            _json = await exists(module.params, session, str(url))
        elif (
            isinstance(_json["value"], list)
            and len(_json["value"]) > 0
            and isinstance(_json["value"][0], str)
        ):
            # this is a list of id, we fetch the details
            full_device_list = await build_full_device_list(session, str(url), _json)
            _json = {"value": [i["value"] for i in full_device_list]}

        return await update_changed_flag(_json, resp.status, "get")


if __name__ == "__main__":
    import asyncio

    current_loop = asyncio.get_event_loop_policy().get_event_loop()
    current_loop.run_until_complete(main())
