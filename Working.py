# Started with fast API before that , we have to create our own virtual environment

# To create virtual environment pyhton -n venv myenv
# To activate use this 
# myenv\Scripts\Activate
# also use to activate with path to activate 
# myenv\Scripts\Activate.ps1 (Copy relative path)

# pip list is used to identify the which package available with version
# uvicorn is server which is installef 
# port of uvicorn is 800

# fastApi have four different decorators based on the CRUD operations
# post deco, get deco, put deco, delete deco

# to start the server
# pydantic used for the validation
# uvicorn main:app --reload

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from data_for_frontend import Product
from database_conn import get_Data , add_data, update_Data, delete_Data

app = FastAPI()

# In list it is automatic object created
# Simple and short database for now 

# adding for CORS to connect with forntend and match the policy
app.add_middleware(CORSMiddleware,
                allow_origins = ['http://localhost:3000'],
                allow_methods = ['*']
                # used to allow more endpoints
)


@app.get('/')
def getData():
    return "Welcome to jaipur...."

@app.get('/products')
def get_products():
    return get_Data()

# using dynamic path with formatted stirng braces {id}, using loop to get all ids data
@app.get('/Products/{id}')
def get_products(id:int): #Requesting id in interger in this 
    products = get_Data() #fetching data from the database
    for i in  products:
        if i.id == id:
            return i
    return "404 Product not found"

# Adding new items or creating data
# First product is object and other Product is class
# and products is a list 
@app.post('/products')
def create_product(product: Product):
    return add_data(product)

# to update
@app.put('/products/{id}')
def update_product(id:int, product: Product):
    return update_Data(id, product)
    

# to delete 
@app.delete('/products/{id}')
def delete_product(id:int):
    return delete_Data(id)


# Now connecting with database 
