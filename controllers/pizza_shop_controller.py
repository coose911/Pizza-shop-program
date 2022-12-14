from flask import render_template, Blueprint, redirect, request
from repositories import pizza_repositorie
from repositories import pizza_shop_repositorie
# from models.pizza import pizza

pizza__shop_blueprint = Blueprint("pizza_shop", __name__)

@pizza__shop_blueprint.route("/pizza_shop")
def pizza_shop():
    pizza_shop = pizza_shop_repositorie.select_all()
    return render_template("pizza_shop/index.html", all_pizzas = pizza_shop)

