import yaml

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

dictionary_serialised_by_yaml = yaml.dump(data)                         # сериализация словаря в строку

# сериализация словаря в файл
with open ('first.yaml', 'w') as file:
    yaml.dump(data, file)

# смотрим, что получилось
with open ('first.yaml', 'r') as file:
    varyaml = yaml.load(file)

print(varyaml)