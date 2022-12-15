from db.run_sql import run_sql

from models.pizza import Pizza
from models.pizza_shop import Pizza_shop

def save(pizza_shops):
    sql = "INSERT INTO pizza_shop (name) VALUES (%s) RETURNING *"
    values = [pizza_shops.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    pizza_shops.id = id
    return pizza_shops

def select_all():
    pizzas = []
    sql = "SELECT * FROM pizzas"
    results = run_sql(sql)

    for pizza in results:
        pizza_shop = Pizza_shop(pizza['name'], pizza['id'])
        pizzas.append(pizza_shop)

    return pizzas

def select(id):
    pizza_shop = None
    sql = "SELECT * FROM pizza_shop WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

    if results:
        result = results[0]
        pizza_shop = pizza_shop(result['name'], result['id'] )
    return pizza_shop
