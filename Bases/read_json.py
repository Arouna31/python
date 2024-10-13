import json
from sum import add

with open('users.json', 'r') as file:
    data: set = json.load(file)
    print(data['users'][0])

print(add(1,2))