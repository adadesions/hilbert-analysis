import json

with open('hc_index.json', 'r') as json_file:
    data = json.load(json_file)
    print(len(data['orders']['8']))
