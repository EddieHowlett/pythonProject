import json

python_dict = {'name': 'Eddie', 'age': 22}
with open('output.json', 'w') as file:
    json.dump(python_dict, file)