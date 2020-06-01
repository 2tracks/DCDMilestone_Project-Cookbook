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


@app.route('/get_recipe/<recipe_id>')
def get_recipe(recipe_id):
    the_recipe = mongo.db.recipe_info.find_one({"_id": ObjectId(recipe_id)})
    return render_template('get_recipe.html', recipe=the_recipe)


@app.route('/add_recipe')
def add_recipe():
    categories = mongo.db.categories.find()
    allergen_free = mongo.db.allergen_free_label.find()
    allergens = mongo.db.allergens.find()
    skill_level = mongo.db.skill_level.find()

    return render_template('add_recipe.html',categories=categories, allergen_free=allergen_free,
                            allergens=allergens, skill_level=skill_level)


@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipe_info
    recipes.insert_one(request.form.to_dict())
    return redirect(url_for('index'))


@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipe_info.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get("PORT")), debug=True)