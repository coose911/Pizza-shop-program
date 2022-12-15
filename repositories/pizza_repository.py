from db.run_sql import run_sql

from models.pizza import Pizza
from models.pizza_shop import Pizza_shop
import repositories.pizza_shop_repository as pizza_shop_repository

def save(pizza):
    sql = "INSERT INTO pizzas (name, toppings, pizza_shop_id, spice_lvl) VALUES (%s, %s, %s, %s) RETURNING * "
    values = [pizza.name, pizza.toppings, pizza.pizza_shop.id, pizza.spice_lvl]
    results = run_sql(sql, values)
    id = results[0]['id']
    pizza.id = id
    return pizza

def select_all():
    pizzas = []
    sql = "SELECT * FROM pizzas"
    results = run_sql(sql)
    
    for row in results:
        pizza_shop = pizza_shop_repository.select(row['pizza_shop_id'])
        pizza = Pizza(row['name'], row['toppings'], pizza_shop, row['id'])
        pizzas.append(pizza)
    return pizzas


def select(id):
    pizza = None
    sql = "SELECT * FROM pizzas WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        pizza_shop = pizza_shop_repository.select(result['pizza_id'])
        pizza = Pizza(result['name'], pizza_shop , result['toppings'], result['spice_lvl'], result['id'] )
    return pizza

