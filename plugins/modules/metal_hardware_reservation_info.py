#!/usr/bin/python
# -*- coding: utf-8 -*-

# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

# DOCUMENTATION, EXAMPLES, and RETURN are generated by
# ansible_specdoc. Do not edit them directly.

DOCUMENTATION = '''
author: Equinix DevRel Team (@equinix) <support@equinix.com>
description: Gather information about Equinix Metal hardware_reservations
module: metal_hardware_reservation_info
notes: []
options:
  project_id:
    description:
    - UUID of parent project containing the hardware_reservations.
    required: true
    type: str
requirements: null
short_description: Gather information about Equinix Metal hardware_reservations
'''
EXAMPLES = '''
- name: Gather information about all hardware_reservations in parent project
  hosts: localhost
  tasks:
  - equinix.cloud.metal_hardware_reservation_info:
      project_id: 2a5122b9-c323-4d5c-b53c-9ad3f54273e7
'''
RETURN = '''
hardware_reservations:
  description: Found hardware reservations
  returned: always
  sample:
  - device_id: ''
    id: 84363c08-a7f5-4e09-8b34-634e82e527c1
    plan: m3.small.x86
    project_id: c6ba3fb2-ee46-4623493a8-de324234a33b
    provisionable: false
    spare: false
    switch_uuid: 00a324b7
  type: dict
'''

# End

from ansible.module_utils._text import to_native
from ansible_specdoc.objects import SpecField, FieldType, SpecReturnValue
import traceback

from ansible_collections.equinix.cloud.plugins.module_utils.equinix import (
    EquinixModule,
    getSpecDocMeta,
)

module_spec = dict(
    project_id=SpecField(
        type=FieldType.string,
        description=['UUID of parent project containing the hardware_reservations.'],
        required=True,
    ),
)

specdoc_examples = ['''
- name: Gather information about all hardware_reservations in parent project 
  hosts: localhost
  tasks:
      - equinix.cloud.metal_hardware_reservation_info:
          project_id: 2a5122b9-c323-4d5c-b53c-9ad3f54273e7
''', '''
''',
                    ]

result_sample = [
    {
        "device_id": "",
        "id": "84363c08-a7f5-4e09-8b34-634e82e527c1",
        "plan": "m3.small.x86",
        "project_id": "c6ba3fb2-ee46-4623493a8-de324234a33b",
        "provisionable": False,
        "spare": False,
        "switch_uuid": "00a324b7"
    }
]

SPECDOC_META = getSpecDocMeta(
    short_description="Gather information about Equinix Metal hardware_reservations",
    description=(
        'Gather information about Equinix Metal hardware_reservations'
    ),
    examples=specdoc_examples,
    options=module_spec,
    return_values={
        "hardware_reservations": SpecReturnValue(
            description='Found hardware reservations',
            type=FieldType.dict,
            sample=result_sample,
        ),
    },
)


def main():
    module = EquinixModule(
        argument_spec=SPECDOC_META.ansible_spec,
        is_info=True,
    )
    try:
        module.params_syntax_check()
        return_value = {'resources': module.get_list("metal_project_hardware_reservation")}
    except Exception as e:
        tr = traceback.format_exc()
        module.fail_json(msg=to_native(e), exception=tr)
    module.exit_json(**return_value)


if __name__ == '__main__':
    main()
