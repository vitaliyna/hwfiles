import json

data =  {  
    'age':  4455,  
    'name':  'Peter', 
    'children':  [ 
            {
                    'age':  33, 
                    'name':  'Alice'  
            }  
    ],  
    'married':  True, 
    'city':  None  
}

dictionary_serialised_by_json = json.dumps(data)                         # сериализация словаря в строку

# сериализация словаря в файл
with open ('second.json', 'w') as file:
    json.dump(data, file)

with open ('second.json', 'r') as file:
    varjson = json.load(file)

print(varjson)

            