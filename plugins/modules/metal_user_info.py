#!/usr/bin/python
# -*- coding: utf-8 -*-

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

# DOCUMENTATION, EXAMPLES, and RETURN are generated by
# ansible_specdoc. Do not edit them directly.

DOCUMENTATION = ""
EXAMPLES = ""
RETURN = ""

# End of generated documentation

from ansible.module_utils._text import to_native
from ansible_specdoc.objects import (
    SpecField,
    FieldType,
    SpecReturnValue,
)
import traceback
import requests

from ansible_collections.equinix.cloud.plugins.module_utils.equinix import (
    EquinixModule,
    getSpecDocMeta,
    get_diff
)

module_spec = dict(
    metal_api_token=SpecField(
        type=FieldType.string,
        description=['The Equinix Metal API token to use.'],
        required=True,
    )
)

specdoc_examples = [
    '''
- name: Gather information about the current current user
  hosts: localhost
  tasks:
    - equinix.cloud.metal_user_info:
        metal_api_token: "{{ lookup('env', 'METAL_API_TOKEN') }}"
      register: result

    - debug:
        var: result
''',
]

return_values = [
    {
        "id": "497f6eca-6276-4993-bfeb-53cbbbba6f08",
        "short_id": "497f6eca",
        "first_name": "John",
        "last_name": "Doe",
        "full_name": "John Doe",
        "email": "john.doe@email.com",
        "social_accounts": {},
        "created_at": "2019-08-24T14:15:22Z",
        "updated_at": "2019-08-24T14:15:22Z",
        "default_organization_id": "7498eaa8-62af-4757-81e0-959250fc9cd5",
        "customdata": {},
        "opt_in": False,
        "opt_in_updated_at": None,
        "default_project_id": None,
        "number_of_ssh_keys": 0,
        "originating_idp": "Equinix",
        "timezone": "America/New_York",
        "language": None,
        "mailing_address": None,
        "verification_stage": "verified",
        "two_factor_auth": "",
        "max_projects": 0,
        "last_login_at": "2019-08-24T14:15:22Z",
        "features": [],
        "emails": [
            {
                "href": "string"
            }
        ],
        "avatar_url": "https://www.gravatar.com/avatar/49d55cbf53f2dae15bfa4c3a3fb884f9?d=mm",
        "avatar_thumb_url": "https://www.gravatar.com/avatar/49d55cbf53f2dae15bfa4c3a3fb884f9?d=mm",
        "href": "/metal/v1/users/497f6eca-6276-4993-bfeb-53cbbbba6f08",
        "phone_number": None,
        "restricted": False
    }
]

SPECDOC_META = getSpecDocMeta(
    short_description='Gather information about the current user for Equinix Metal',
    description='Gather information about the current user for Equinix Metal',
    examples=specdoc_examples,
    options=module_spec,
    return_values={
        "user": SpecReturnValue(
            description='Information about the current user.',
            type=FieldType.dict,
            sample=return_values,
        ),
    },
)

def main():
    module = EquinixModule(
        argument_spec=SPECDOC_META.ansible_spec,
        is_info=True,
    )

    changed = False
    return_value = {}

    try:
        module.params_syntax_check()
        metal_api_token = module.params['metal_api_token']
        headers = {
            'X-Auth-Token': metal_api_token
        }

        response = requests.get("https://api.equinix.com/metal/v1/user", headers=headers)
        if response.status_code == 200:
            return_value = {'user': response.json()}
        else:
            module.fail_json(msg='Failed to retrieve user information', response=response.text)
    except Exception as e:
        tb = traceback.format_exc()
        module.fail_json(msg="Error in metal_user_info: {0}".format(to_native(e)), exception=tb)

    module.exit_json(changed=changed, **return_value)


if __name__ == '__main__':
    main()
