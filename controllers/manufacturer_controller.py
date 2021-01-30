from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.manufacturer import Manufacturer
from repositories.manufacturer_repository import manufacturer_repository

manufacturers_blueprint = Blueprint("manufacturers", __name__)


