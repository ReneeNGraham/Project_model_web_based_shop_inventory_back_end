from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models import manufacturer
from models.manufacturer import Manufacturer
import repositories.manufacturer_repository as manufacturer_repository 
import repositories.product_repository as product_repository 

manufacturers_blueprint = Blueprint("manufacturers", __name__)

@manufacturers_blueprint.route("/manufacturers")
def manufacturers():
    manufacturers = manufacturer_repository.select_all()
    return render_template("manufacturers/index.html", manufacturers = manufacturers)

@manufacturers_blueprint.route("/manufacturers/new", methods=['GET'])
def new_manufacturer():
    manufacturers = manufacturer_repository.select_all()
    return render_template("/manufacturers/new.html",manufacturers=manufacturers)
   

@manufacturers_blueprint.route("/manufacturers", methods=['POST'])
def create_manufacturer():
    name = request.form['name']
    description = request.form['description']
    manufacturer = Manufacturer(name, description)
    manufacturer_repository.save(manufacturer)
    return redirect('/manufacturers')

@manufacturers_blueprint.route("/manufacturers/<id>", methods=['GET'])
def show_manufacturer(id):
    manufacturer = manufacturer_repository.select(id)
    return render_template("manufacturers/show.html", manufacturer=manufacturer)

#EDIT 

@manufacturers_blueprint.route("/manufacturers/<id>/edit", methods=['GET'])
def edit_manufacturer(id):
    manufacturer = manufacturer_repository.select(id)
    products = product_repository.select_all()
    return render_template('manufacturers/edit.html',products=products, manufacturer=manufacturer)

#UPDATE 
@manufacturers_blueprint.route("/manufacturers/<id>", methods=['POST'])
def update_manufacturers(id):
    orig_manufacturer = manufacturer_repository.select(id)
    name              = request.form['name']
    description       = request.form['description']
    orig_manufacturer.name = name
    orig_manufacturer.description = description
    # manufacturer      = Manufacturer(name, description)
    manufacturer_repository.update(orig_manufacturer)
    return redirect('/manufacturers')
             
##DELETE

@manufacturers_blueprint.route("/manufacturers/<id>/delete", methods=['POST'])
def delete_manufacturer(id):
    manufacturer_repository.delete(id)
    return redirect("/manufacturers")
    
    