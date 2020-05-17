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

recipe_info = mongo.db.recipe_info
categories = mongo.db.categories
skill_level = mongo.db.skill_level
allergens = mongo.db.allergens


@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html", recipe_info=mongo.db.recipe_info.find())


@app.route('/get_recipes')
def get_recipes():
    return render_template("all_recipes.html",recipe_info=recipe_info.find().sort('date_time, pymongo.DESCENDING'),
                            categories=categories.find())


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get("PORT")),debug=True)

