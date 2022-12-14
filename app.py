from flask import Flask, render_template
from controllers.pizza_shop_controller import pizzas_blueprint

app = Flask(__name__)

app.register_blueprint(pizzas.blueprint)

@app.route('/')
def home():
    return render_template('pizzas.html')

if __name__ == '__main__':
    app.run(debug = True)