EXAMPLES = r'''
# lookup sample:
- name: lookup MOID of the object in the path
  debug: msg="{{ lookup('vmware_id', {'vm', '/my_dc/host/my_cluster/esxi1.test/test_vm1'}) }}"
'''

RETURN = r'''
'''

INVENTORY = {
    "resource_pool": {
        "list": {
            "query": {
                "clusters": "clusters",
                "datacenters": "datacenters",
                "hosts": "hosts",
                "names": "names",
                "parent_resource_pools": "parent_resource_pools",
                "resource_pools": "resource_pools",
            },
            "body": {},
            "path": {},
        } 
    },
    "datacenter": {
        "list": {
            "query": {
                "datacenters": "datacenters",
                "folders": "folders",
                "names": "names"
            },
            "body": {},
            "path": {},
        }
    },
    "folder": {
        "list": {
            "query": {
                "datacenters": "datacenters",
                "folders": "folders",
                "names": "names",
                "parent_folders": "parent_folders",
                "type": "type",
            },
            "body": {},
            "path": {},
        }
    },
    "cluster": {
        "list": {
            "query": {
                "clusters": "clusters",
                "datacenters": "datacenters",
                "folders": "folders",
                "names": "names",
            },
            "body": {},
            "path": {},
        }
    },
    "host": {
        "list": {
            "query": {
                "clusters": "clusters",
                "datacenters": "datacenters",
                "folders": "folders",
                "hosts": "hosts",
                "names": "names",

            },
            "body": {},
            "path": {},
        }
    },
    "datastore": {
        "list": {
            "query": {
                "datacenters": "datacenters",
                "datastores": "datastores",
                "folders": "folders",
                "names": "names",
                "types": "types",
            },
            "body": {},
            "path": {},
        }
    },
    "vm": {
        "list": {
            "query": {
                "clusters": "clusters",
                "datacenters": "datacenters",
                "folders": "folders",
                "hosts": "hosts",
                "names": "names",
                "resource_pools": "resource_pools",
                "vms": "vms"
            },
            "body": {},
            "path": {},
        }
    },
    "network": {
        "list": {
            "query": {
                "datacenters": "datacenters",
                "folders": "folders",
                "names": "names",
                "networks": "networks",
                "types": "types"
            },
            "body": {},
            "path": {},
        }
    }
}


import json
import socket
import asyncio

from ansible.errors import AnsibleError
from ansible.plugins.lookup import LookupBase
from ansible_collections.cloud.common.plugins.module_utils.turbo.exceptions import EmbeddedModuleFailure

from ansible_collections.vmware.vmware_rest.plugins.module_utils.vmware_rest import (
    gen_args,
    open_session,
)


class LookupModule(LookupBase):
    def run(self, terms, variables, **kwargs):
        import asyncio
        '''
            :arg terms: a list of lookups to run.
                e.g. 'object_name', 'path'
            :kwarg vcenter_hostname: identity of the vCenter hostname
            :kwarg vcenter_username: vCenter username
            :kwarg vcenter_password: 
            :kwarg vcenter_validate_certs: Set to True to validate certs
            :kwarg vcenter_rest_log_file: AWS region in which to do the lookup
            :returns: A list of moid values or a list of dictionaries.
        '''

        loop = asyncio.get_event_loop()
        self.pool = loop.run_until_complete(self.entry_point(terms, variables, **kwargs))


    async def entry_point(self, terms, variable,  **kwargs):
        session = None

        if not kwargs.get("vcenter_hostname"):
            raise AnsibleError("vcenter_hostname cannot be empty")
        if not kwargs.get("vcenter_username"):
            raise AnsibleError("vcenter_username cannot be empty")
        if not kwargs.get("vcenter_password"):
            raise AnsibleError("vcenter_password cannot be empty")

        try:
            session = await open_session(
                vcenter_hostname=kwargs.get("vcenter_hostname"),
                vcenter_username=kwargs.get("vcenter_username"),
                vcenter_password=kwargs.get("vcenter_password"),
                validate_certs=kwargs.get("vcenter_validate_certs") or False,
                log_file=kwargs.get("vcenter_rest_log_file") or None,
            )
        except EmbeddedModuleFailure as err:
            raise AnsibleError(err.get_message())
        
        return session
