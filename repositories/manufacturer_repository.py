from db.run_sql import run_sql
from models import manufacturer
from models.product import Product 
from models.manufacturer import Manufacturer
import repositories.manufacturer_repository as manufacturer_repository

def save(manufacturer):
    sql = "INSERT INTO manufacturers (name, description) VALUES (%s, %s) RETURNING id"
    values = [manufacturer.name, manufacturer.description]
    results = run_sql(sql, values)
    manufacturer.id = results[0]['id']
    return manufacturer
    



