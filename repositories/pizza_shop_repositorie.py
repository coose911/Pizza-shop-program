from db.run_sql import run_sql

from models.pizza import Pizza
from models.pizza_shop import Pizza_shop

def save(pizza_shop):
    sql = "INSERT INTO pizzas (name) VALUES (%s) RETURNING *"
    values = [pizza_shop.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    pizza_shop.id = id
    return pizza_shop