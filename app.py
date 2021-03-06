import os
import math
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = 'my_cookbook'
app.config["MONGO_URI"] = os.getenv('MONGO_URI')


mongo = PyMongo(app)

# Get landing page
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

# Search by categories
@app.route('/search_categories/<get_category_name>/<int:page>')
def search_categories(get_category_name, page):
    category = mongo.db.recipe_info.find({'category_name': get_category_name})

    recipes_count = category.count()

    limit = 6
    offset = int((page)-1)*6

    recipe_pages_total = math.ceil(recipes_count/limit)

    recipe_page = category.sort([('_id', -1)]).skip(offset).limit(limit)

    return render_template('search_categories.html', category=category, page=page,
                             recipe_page=recipe_page, recipes_count=recipes_count,
                            recipe_pages_total=recipe_pages_total)

# Get single Recipe
@app.route('/get_recipe/<recipe_id>')
def get_recipe(recipe_id):
    the_recipe = mongo.db.recipe_info.find_one({"_id": ObjectId(recipe_id)})
    return render_template('get_recipe.html', recipe=the_recipe)

# Add Recipe
@app.route('/add_recipe')
def add_recipe():
    categories = mongo.db.categories.find()
    allergen_free_label = mongo.db.allergen_free_label.find()
    allergens = mongo.db.allergens.find()
    skill_level = mongo.db.skill_level.find()

    return render_template('add_recipe.html',categories=categories, allergen_free_label=allergen_free_label,
                            allergens=allergens, skill_level=skill_level)


@app.route('/insert_recipe', methods=['POST'])
def insert_recipe():
    recipes = mongo.db.recipe_info

    new_recipe = {
        'recipe_name': request.form.get('recipe_name'),
        'recipe_img': request.form.get('recipe_img'),
        'recipe_description': request.form.get('recipe_description'),
        'category_name': request.form.get('category_name'),
        'allergen_free_label': request.form.getlist('allergen_free_label'),
        'allergen_type': request.form.getlist('allergen_type'),
        'recipe_prep_time': request.form.get('recipe_prep_time'),
        'recipe_cook_time': request.form.get('recipe_cook_time'),
        'recipe_serves': request.form.get('recipe_serves'),
        'recipe_level': request.form.get('recipe_level'),
        'recipe_ingredients': request.form.getlist('recipe_ingredients'),
        'recipe_method': request.form.get('recipe_method'),
        'rating': request.form.get('rating'),
        'date': request.form.get('date'),
        'author_name': request.form.get('author_name')
    }
    recipes.insert_one(new_recipe)
    return redirect(url_for('index'))

# Edit Recipe
@app.route('/edit_recipe/<recipe_id>')
def edit_recipe(recipe_id):
    the_recipe = mongo.db.recipe_info.find_one({'_id': ObjectId(recipe_id)})
    categories = mongo.db.categories.find()
    allergen_free_label = mongo.db.allergen_free_label.find()
    allergens = mongo.db.allergens.find()
    skill_level = mongo.db.skill_level.find()
    return render_template('edit_recipe.html', recipe=the_recipe,
                            categories=categories, allergen_free_label=allergen_free_label,
                            allergens=allergens, skill_level=skill_level)


@app.route('/update_recipe/<recipe_id>', methods=['POST'])
def update_recipe(recipe_id):
    recipes = mongo.db.recipe_info

    recipes.update({'_id': ObjectId(recipe_id)},
    {
        'recipe_name': request.form.get('recipe_name'),
        'recipe_img': request.form.get('recipe_img'),
        'recipe_description': request.form.get('recipe_description'),
        'category_name': request.form.get('category_name'),
        'allergen_free_label': request.form.getlist('allergen_free_label'),
        'allergen_type': request.form.getlist('allergen_type'),
        'recipe_prep_time': request.form.get('recipe_prep_time'),
        'recipe_cook_time': request.form.get('recipe_cook_time'),
        'recipe_serves': request.form.get('recipe_serves'),
        'recipe_level': request.form.get('recipe_level'),
        'recipe_ingredients': request.form.getlist('recipe_ingredients'),
        'recipe_method': request.form.get('recipe_method'),
        'rating': request.form.get('rating'),
        'date': request.form.get('date'),
        'author_name': request.form.get('author_name')
    })
    return redirect(url_for('index'))


# Delete Recipe
@app.route('/delete_recipe/<recipe_id>')
def delete_recipe(recipe_id):
    mongo.db.recipe_info.remove({'_id': ObjectId(recipe_id)})
    return redirect(url_for('index'))


# Search keyword
@app.route('/keyword_result', methods=['POST'])
def keyword_result():
    keyword = request.form.get('keyword')
    return redirect(url_for('search_keyword', keyword=keyword, page=1))


@app.route('/search_keyword/<keyword>/<int:page>', methods=['GET'])
def search_keyword(keyword, page):
        recipes = mongo.db.recipe_info
        recipes.create_index([('recipe_name', 'text'), ('recipe_ingredients', 'text'),
                        ('recipe_method', 'text'), ('recipe_description', 'text'), ('recipe_category', 'text')])

        recipes_search_result = recipes.find({'$text': {'$search': keyword}}).sort([('date', -1), ('_id', -1)])
        recipes_count = recipes_search_result.count()
        limit = 6
        offset = int((page)-1)*6

        recipe_pages_total = math.ceil(recipes_count/limit)
        recipe_page = recipes_search_result.sort([('_id', -1)]).skip(offset).limit(limit)

        return render_template('search_keyword.html', recipes_search_result=recipes_search_result, keyword=keyword,
                                page=page, recipe_page=recipe_page, recipes_count=recipes_count,
                                recipe_pages_total=recipe_pages_total)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get("PORT")), debug=False)