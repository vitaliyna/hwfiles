from pydantic import BaseModel
from typing import List, Optional

class Child(BaseModel):
    age: int
    name: str

class Person(BaseModel):
    age: int
    name: str   
    children: Optional[List[Child]] = None
    married: bool
    city: None

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

p = Person(**data)
print(p)