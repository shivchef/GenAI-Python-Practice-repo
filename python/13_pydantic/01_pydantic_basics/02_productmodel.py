from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool = True #we can assign default value in it


Product_one = Product(id = 1, name= "Laptop", price = 9992.93, in_stock=True)


Product_two = Product(id=2, name="mouse",price = 24.13)


Product_three = Product(name = 'Keyboard')