import os, math
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
@app.route('/index/<int:page>')
def index(page=1):
    recipes_db = mongo.db.recipe_info

    recipe_all = recipes_db.find().sort([("date", -1)])
    recipes_count = recipe_all.count()

    limit = 6
    offset = int((page)-1)*6

    recipe_pages_total = math.ceil(recipes_count/limit)

    recipe_page = recipe_all.sort([('_id', -1)]).skip(offset).limit(limit)

    return render_template("index.html", recipe_all=recipe_all,
                            page=page, recipe_page=recipe_page, recipes_count=recipes_count,
                            recipe_pages_total=recipe_pages_total)


@app.route('/search_categories/<get_category_name>')
def search_categories(get_category_name):
    category = mongo.db.recipe_info.find({'category_name': get_category_name})
    return render_template('search_categories.html', category=category)


@app.route('/add_recipe')
def add_recipe():
    return render_template('add_recipe.html')


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get("PORT")), debug=True)