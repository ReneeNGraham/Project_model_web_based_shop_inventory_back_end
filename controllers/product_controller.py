from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.product import Product
from repositories.product_repository import product_repository

products_blueprint = Blueprint("products", __name__)