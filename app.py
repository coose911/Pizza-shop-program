from flask import Flask, render_template
from controllers.pizza_shop_controller import pizza_shop_blueprint

app = Flask(__name__)

app.register_blueprint(pizza_shop_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug = True)