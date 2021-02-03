from controllers.manufacturer_controller import manufacturers
from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.product import Product
import repositories.product_repository as product_repository
import repositories.manufacturer_repository as manufacturer_repository 

products_blueprint = Blueprint("products", __name__)

@products_blueprint.route("/products")
def products():
    products  = product_repository.select_all()
    return render_template("products/index.html", products=products)

@products_blueprint.route("/products/new", methods=['GET'])
def new_product():
    products = product_repository.select_all()
    return render_template("/products/new.html", products=products)

@products_blueprint.route("/products", methods=['POST'])
def create_product():
    name              = request.form['name']
    manufacturer_id   = request.form['manufacturer_id']
    description       = request.form['description']
    quantity_in_stock = request.form['quantity_in_stock']
    cost_to_purchase  = request.form['cost_to_purchase']
    selling_price     = request.form['selling_price']
    manufacturer      = manufacturer_repository.select(manufacturer_id)
    product           = Product(name, manufacturer, description, quantity_in_stock, cost_to_purchase, selling_price)
    product_repository.save(product)
    return redirect("/products")


@products_blueprint.route("/products/<id>", methods=['GET'])
def show_product(id):
    product = product_repository.select(id)
    return render_template("products/show.html", product=product)

#EDIT 

@products_blueprint.route("/products/<id>/edit", methods=['GET'])
def edit_product(id):
    product = product_repository.select(id)
    manufacturers = manufacturer_repository.select_all()
    return render_template("products/edit.html", product = product, manufacturers = manufacturers)

#UPDATE 

@products_blueprint.route("/products/<id>", methods=['POST'])
def update_product(id):
    name              = request.form['name']
    manufacturer_id   = request.form['manufacturer_id']
    description       = request.form['description']
    quantity_in_stock = request.form['quantity_in_stock']
    cost_to_purchase  = request.form['cost_to_purchase']
    selling_price     = request.form['selling_price']
    manufacturer      = manufacturer_repository.select(manufacturer_id)
    product           = Product(name, manufacturer, description, quantity_in_stock, cost_to_purchase, selling_price, id)
    product_repository.update(product)
    return redirect("/products")


#DELETE
    
@products_blueprint.route("/products/<id>/delete", methods=['POST'])
def delete_product(id):
    product_repository.delete(id)
    return redirect("/products")
    