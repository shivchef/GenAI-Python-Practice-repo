from pydantic import BaseModel
from typing import List,Dict,Optional


class Cart(BaseModel):
    user_id: int
    items: List[str]
    quantities: Dict[str, int]


class BlogPost(BaseModel):
    title: str
    content: str
    image_url: Optional[str] = None #If we are uncertain about certain object then we can do this

cart_data = {
    'user_id' : 123,
    'items':["Laptop", 'Mouse',"keyboard"],
    'quantities': {'laptop':1 , 'Mouse':3,'keyboard': 3}

}

cart = Cart(**cart_data)