import json

new_file_name = "new_example.json"
f = open("example.json")

my_json = json.load(f)
print(my_json)

my_json['string'] = "off"

with open(new_file_name, "x") as ff:
    json.dump(my_json, ff)

new_json_str = open(new_file_name).read()
new_json_dic = json.loads(new_json_str)

print(new_json_dic)