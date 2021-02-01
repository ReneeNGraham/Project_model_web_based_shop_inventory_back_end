from db.run_sql import run_sql
from models import manufacturer
from models.product import Product
from models.manufacturer import Manufacturer
import repositories.manufacturer_repository as manufacturer_repository

def save(product):
    sql = "INSERT INTO products (name, manufacturer_id, description, quantity_in_stock, cost_to_purchase, selling_price) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id"
    values = [product.name, product.manufacturer.id, product.description, product.quantity_in_stock, product.cost_to_purchase, product.selling_price]
    results = run_sql(sql, values)
    product.id = results[0]['id']
    return product

def select_all():
    products = []
    
    sql = "SELECT * FROM products"
    results = run_sql(sql)
    
    for row in results:
        manufacturer = manufacturer_repository.select(row['manufacturer_id'])
        product = Product(row['name'], manufacturer, row ['description'], row['quantity_in_stock'], row['cost_to_purchase'], row['selling_price'], row['id'])
        products.append(product)
    return products

def select(id):
    product = None
    sql = "SELECT * FROM products WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        manufacturer = manufacturer_repository.select(result['manufacturer_id'])
        product = Product(result['name'], manufacturer, result['description'], result['quantity_in_stock'], result['cost_to_purchase'], result['selling_price'], result['id'])
    return product

def delete_all():
    sql = "DELETE FROM products"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM products WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(product):
    sql = "UPDATE products SET (name, manufacturer_id, description, quantity_in_stock, cost_to_purchase, selling_price) = (%s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [product.name, product.manufacturer.id, product.description, product.quantity_in_stock, product.cost_to_purchase, product.selling_price, product.id]
    run_sql(sql, values)

def manufacturers(product):
    manufacturers = []

    sql = "SELECT * FROM manufacturers WHERE product_id = %s"
    values = [product.id]
    results = run_sql (sql, values)

    for row in results: 
        manufacturer = Manufacturer(row['name'],row['description'], row['id'])
        manufacturers.append(manufacturer)
    return manufacturers

     
 
