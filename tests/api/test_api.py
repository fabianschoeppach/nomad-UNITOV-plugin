### Only runs clean when api is running

import requests
import json
import sys;
base_url = 'http://localhost:8000/fairdi/nomad/latest/api/v1'

response = requests.post(
    f'{base_url}/entries/query',
    json={
        'query': {
            'results.material.elements': {
                'all': ['Ti', 'O']
            }
        },
        'pagination': {
            'page_size': 1
        },
        'required': {
            'include': ['entry_id']
        }
    })
response_json = response.json()

print(json.dumps(response.json(), indent=2))





if(response_json['data'] == []):
    print("No data in system.")
    sys.exit()

first_entry_id = response_json['data'][0]['entry_id']

response = requests.post(
    f'{base_url}/entries/{first_entry_id}/archive/query',
    json={
        'required': {
            'workflow': {
                'calculation_result_ref': {
                    'energy': '*',
                    'system_ref': {
                        'chemical_composition': '*'
                    }
                }
            }
        }
    })
response_json = response.json()
print(json.dumps(response_json, indent=2))