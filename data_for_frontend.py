# for data validation 
from pydantic import BaseModel
# base modle is used to validate data 
class Product(BaseModel):
    id:int
    name: str 
    description : str
    price: float
    quantity: int
    # creating constructor
    # def __init__(self, id, name, description ,price, quantity ):
    #     self.id = id
    #     self.name = name
    #     self.description = description
    #     self.price = price
    #     self.quantity = quantity
        