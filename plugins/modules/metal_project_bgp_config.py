#!/usr/bin/python
# -*- coding: utf-8 -*-

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

# DOCUMENTATION, EXAMPLES, and METAL_PROJECT_ARGS are generated by
# ansible_specdoc. Do not edit them directly.

DOCUMENTATION = '''
author: Equinix DevRel Team (@equinix) <support@equinix.com>
description: 'You can use this module to enable BGP Config for a project. To lookup
  BGP Config of an existing project, call the module only with `project_id`. '
module: metal_project_bgp_config
notes: []
options:
  asn:
    description:
    - Autonomous System Number for local BGP deployment
    required: true
    type: int
  deployment_type:
    description:
    - '"local" or "global". Local deployment type is likely to be usable immediately, '
    - '"global" will need to be reviewed by Equinix Metal support.'
    required: true
    type: str
  md5:
    description:
    - Password for BGP session in plaintext (not a checksum)
    required: false
    type: str
  project_id:
    description:
    - UUID of the project where BGP Config should be enabled
    required: true
    type: str
  use_case:
    description:
    - Description of your BGP use-case for Equinix Metal support
    required: false
    type: str
requirements: null
short_description: Manage BGP Config for Equinix Metal Project
'''
EXAMPLES = '''
- name: Enable local BGP Config in Equinix Metal project
  hosts: localhost
  tasks:
  - equinix.cloud.metal_project_bgp_config:
      deployment_type: local
      asn: 65000
      md5: null
      use_case: ansible test
      project_id: '{{ test_project.id }}'
'''
RETURN = '''
metal_project_bgp_config:
  description: The module object
  returned: always
  sample:
  - "\n{\n    \"changed\": true\n}\n"
  type: dict
'''

# End of generated documentation

from ansible.module_utils._text import to_native
from ansible_specdoc.objects import (
    SpecField,
    FieldType,
    SpecReturnValue,
)
import traceback

from ansible_collections.equinix.cloud.plugins.module_utils.equinix import (
    EquinixModule,
    get_diff,
    getSpecDocMeta,
)


module_spec = dict(
    project_id=SpecField(
        type=FieldType.string,
        description=['UUID of the project where BGP Config should be enabled'],
        required=True,
        editable=False,
    ),
    asn=SpecField(
        type=FieldType.integer,
        required=True,
        description=['Autonomous System Number for local BGP deployment'],
        editable=False,
    ),
    deployment_type=SpecField(
        type=FieldType.string,
        required=True,
        description=[
            '"local" or "global". Local deployment type is likely to be usable immediately, ',            
            '"global" will need to be reviewed by Equinix Metal support.',
        ],
        editable=False,
    ),
    md5=SpecField(
        type=FieldType.string,
        description=['Password for BGP session in plaintext (not a checksum)'],
        editable=False,
    ),
    use_case=SpecField(
        type=FieldType.string,
        description=['Description of your BGP use-case for Equinix Metal support'],
        editable=False,
    ),
)


specdoc_examples = [
    '''
- name: Enable local BGP Config in Equinix Metal project
  hosts: localhost
  tasks:
    - equinix.cloud.metal_project_bgp_config:
        deployment_type: local
        asn: 65000
        md5: null
        use_case: "ansible test"
        project_id: "{{ test_project.id }}"
''',
]

result_sample = ['''
{
    "changed": true
}
''']

MUTABLE_ATTRIBUTES = [
    k for k, v in module_spec.items() if v.editable
]

SPECDOC_META = getSpecDocMeta(
    short_description='Manage BGP Config for Equinix Metal Project',
    description=(
        'You can use this module to enable BGP Config for a project. To lookup BGP Config of an existing project, call the module only with `project_id`. '
    ),
    examples=specdoc_examples,
    options=module_spec,
    return_values={
        "metal_project_bgp_config": SpecReturnValue(
            description='The module object',
            type=FieldType.dict,
            sample=result_sample,
        ),
    },
)


def main():
    module = EquinixModule(
        argument_spec=SPECDOC_META.ansible_spec,
    )

    state = module.params.get("state")
    changed = False

    try:
        module.params_syntax_check()

        module.params['id'] = module.params.get("project_id")
        tolerate_not_found = state == "absent"
        fetched = module.get_by_id("metal_project_bgp_config", tolerate_not_found)

        if not fetched.get('id'):
            # api returns {max_prefix: 10, 'md5': None} even if config not exists
            # optional RESPONSE_ATTRIBUTE_MAP puts other attributes as Nones
            fetched = {}

        if fetched:
            if state == "present":
                diff = get_diff(module.params, fetched, MUTABLE_ATTRIBUTES)
                if diff:
                    module.fail_json(msg="BGP config cannot be updated")

            else:
                module.fail_json(msg="BGP config cannot be deleted. Please delete project")
        elif state == "present":
            fetched = module.create("metal_project_bgp_config")
            changed = True

    except Exception as e:
        tb = traceback.format_exc()
        module.fail_json(msg="Error in metal_project_bgp_config: {0}".format(to_native(e)),
                         exception=tb)

    fetched.update({'changed': changed})
    module.exit_json(**fetched)


if __name__ == '__main__':
    main()
