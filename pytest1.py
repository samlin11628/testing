import json

with open("data.json", 'r') as load_f:
    data=json.load(load_f)
    print(data)
