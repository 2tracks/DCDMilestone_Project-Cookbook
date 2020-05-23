import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'my_cookbook'
app.config["MONGO_URI"] = os.getenv('MONGO_URI')


mongo = PyMongo(app)





@app.route('/')
@app.route('/index')
def index():
    recipe_info = mongo.db.recipe_info.find().sort([("date", -1 )]).limit(6)
    return render_template("index.html", recipe_info=recipe_info)


@app.route('/search_categories/<get_category_name>')
def search_categories(get_category_name):
    category = mongo.db.recipe_info.find({'category_name': get_category_name })
    return render_template('search_categories.html', category = category)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get("PORT")),debug=True)

