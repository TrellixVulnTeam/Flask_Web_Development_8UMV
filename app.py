from flask import Flask, request, render_template, jsonify, abort
from flask import make_response
from datetime import datetime

app = Flask(__name__)

#Restful API
tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]

#GET Method
@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})

#Error Handler
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

#GET ONLY ROUTES
# @ signifies a decorator - way to wrap a function and modify it's behavior
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/hello/<name>")
def hello_there(name):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )

# New functions
@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route('/shopping')
def shopping():
    food = ['Cheese', 'Tuna', 'Beef']
    return render_template("shopping.html", food=food)

@app.route('/profile/<name>')
def profile(name):
    return render_template("profile.html", name=name)

@app.route('/product/<int:product_id>')
def product(product_id):
    return '<h2>Product ID is %s!</h2>' %product_id

#POST
@app.route("/login", methods=['GET', 'POST'])
def login():
    return "Method used: %s" % request.method

#Get data from the API
@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")

if  __name__ == "__main__":
    app.run(debug=True)