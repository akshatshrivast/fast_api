import mysql.connector as sql
from data_for_frontend import Product

conn = sql.connect(host = 'localhost', user = 'root', password = 'root#2004', port = 3307)
conn.autocommit = True
curr = conn.cursor()
curr.execute("use data;")

def get_Data():
    products = []
    curr.execute("select * from backend_data;")
    data = curr.fetchall()
    # first import Product class
    for i in data:
        products.append(Product(id = i[0],
                 name = i[1],
                 description = i[2],
                 price = i[3],
                 quantity = i[4]
                 ))
    return products

def add_data(Product:Product):
    query = f"insert into backend_data values({Product.id}, '{Product.name}', '{Product.description}', {Product.price},{Product.quantity});"

    curr.execute(query)
    return "record added successfully"


def update_Data(id:int, Product:Product):

    query = f"update backend_data set name =' {Product.name}', description = '{Product.description}', price = {Product.price}, quantity = {Product.quantity} where id = {id};"

    curr.execute(query)
    return "Record Updated Successfully"


def delete_Data(id:int):
    query = f"delete from backend_data where id = {id};"
    curr.execute(query)
    return "Record deleted Successfully"


