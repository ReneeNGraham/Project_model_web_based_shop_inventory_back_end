from db.run_sql import run_sql
from models import manufacturer
from models.product import Product 
from models.manufacturer import Manufacturer
import repositories.product_repository as product_repository


def save(manufacturer):
    sql = "INSERT INTO manufacturers (name, description) VALUES (%s, %s) RETURNING id"
    values = [manufacturer.name, manufacturer.description]
    results = run_sql(sql, values)
    manufacturer.id = results[0]['id']
    return manufacturer

def select_all():
    manufacturers = []

    sql = "SELECT * FROM manufacturers"
    results = run_sql(sql)

    for row in results:
        manufacturer = Manufacturer(row['name'], row['description'], row['id'])
        manufacturers.append(manufacturer)
    return manufacturers

def select(id):
    manufacturer = None
    sql = "SELECT * FROM manufacturers WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        manufacturer = Manufacturer(result['name'], result['description'], result['id'])
    return manufacturer

def delete_all():
    sql = "DELETE FROM manufacturers"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM manufacturers WHERE id =%s"
    values = [id]
    run_sql(sql, values)




    




