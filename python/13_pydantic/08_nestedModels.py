from typing import List, Optional
from pydantic import BaseModel

class Address(BaseModel):
    street: str
    city: str
    postal_code: str

class User(BaseModel):
    id: int
    name: str
    address: Address

address = Address(
    street = '123',
    city='kolhapur',
    postal_code='89633'

)

user = User(
    id=1,
    name= "mila",
    address=address
)

user_data={
    'id':1,
    'name':'Nillind',
    "address":{
        'street':"312",
        'city':'kolhapur',
        'postal_code':'89027'
    }
}

user = User(**user_data)
print(user)