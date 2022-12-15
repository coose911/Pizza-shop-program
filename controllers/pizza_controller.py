from flask import render_template, Blueprint, redirect, request
import repositories.pizza_repository as pizza_repository
import repositories.pizza_shop_repository as pizza_shop_repository
from models.pizza import Pizza

pizza_blueprint = Blueprint("pizza", __name__)

@pizza_blueprint.route("/pizza")
def pizza():
    pizzas = pizza_repository.select_all()
    return render_template("pizza/index.html", all_pizzas = pizzas)

