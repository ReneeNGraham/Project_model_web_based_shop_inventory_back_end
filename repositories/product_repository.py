from db.run_sql import run_sql
from models.product import Product
from models.manufacturer import Manufacturer
import repositories.product_repository as product_repository

def save(product):
    sql = "INSERT INTO products (name, manufacturer_id, description, quantity_in_stock, cost_to_purchase, selling_price) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id"
    values = [product.name, product.manufacturer.id, product.description, product.quantity_in_stock, product.cost_to_purchase, product.selling_price]
    results = run_sql(sql, values)
    product.id = results[0]['id']
    return product
    