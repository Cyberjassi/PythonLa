import json
# file = open('fj.txt','r')
# file_contents = json.load(file)
# file.close()

# print(file_contents['friends'][0])

# cars = [
#     {'make':'ford','model':'Fiesta'},
#     {'make':'ford','model':'focus'}
# ]

# file = open('fj.txt','a')
# json.dump(cars,file)
# file.close()

str = '[{"name":"jay","sername":"borausi"}]'

convert_json_to_dict = json.loads(str)
print(convert_json_to_dict[0]['name'])