from fastapi import FastAPI
from models import Product
from config import Session

app = FastAPI()

@app.get("/")
def greet():
    return "FastApi project"

products = [
    Product(id=1, name="Phone", description="A smartphone", price=699.99, quantity=50),
    Product(id=2, name="Laptop", description="A powerful laptop", price=999.99, quantity=30),
    Product(id=3, name="Pen", description="A blue ink pen", price=1.99, quantity=100),
    Product(id=4, name="Table", description="A wooden table", price=199.99, quantity=20),
]

@app.get("/products")
def get_all_products():
    db = Session()
    db.query()
    return products

@app.get("/product/{id}")
def get_product_by_id(id: int):
    for product in products:
        if product.id == id:
            return product
        
    return "product not found"

@app.post("/products")
def create_product(product: Product):
    products.append(product)
    return {"message": "Product created successfully", "product": product}

@app.put("/product")
def update_product( id : int , product : Product):
    for i in range(len(products)):
        if products[i].id == id:
            products[i] = product
            return "product added"
        
    return "no product found"

@app.delete("/product")
def delete_product(id : int):
    for i in range(len(products)):
        if products[i].id == id:
            del products[i]
            return "product deleted"
        
    return "product not deleted"

