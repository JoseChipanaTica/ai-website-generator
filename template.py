import os
import json

path = os.getcwd()

template_path = path + os.sep + 'templates' + os.sep + 'basic-template.json'

with open(template_path, 'r') as file:
    template_json = file.read()
    file.close()

template_json = json.loads(template_json)

pages = template_json['website']['pages']

for page in pages:
    blocks = page['blocks']
    for block in blocks:
        content = block['content']
        for item in content:
            block_data = item['block']
            for data in block_data:
                print(data)

data = [data['prompt'] for page in pages
        for block in page['blocks']
        for item in block['content']
        for data in item['block']]

for item in data:
    print(item)
