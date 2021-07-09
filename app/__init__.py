""" Application """
from flask import Flask, render_template, request
from config import config
from .recipe import get_random_joke, get_random_recipes, search_recipes, get_recipe_detail, visualize_recipe_equipments, visualize_recipe_ingredients, get_analyzed_recipe_instructions
from .parser import strip_tags

app = Flask(__name__)

def create_app(config_name):
    app.config.from_object(config[config_name])
    return app

# todo: HOMEPAGE
@app.route('/', methods=['GET'])
def homepage():
    """ Show Home Page - Navbar - Random Food Joke - Random Recipes"""
    random_recipes = get_random_recipes()
    random_joke = get_random_joke()
    return render_template('home.html', random_recipes = random_recipes, random_joke=random_joke)


# todo: /recipes - return recipes by searching name
@app.route('/recipes', methods=['GET'])
def recipes():
    """Page with listing of recipes. Can take a 'q' param in querystring to search by that name."""
    name = request.args.get('q')
    recipes = search_recipes(name)
    return render_template('recipes/recipes.html', recipes=recipes)

# todo: /recipes/id - return recipe detail including title, image, summary, equipments, ingredients and other information
@app.route('/recipes/<int:recipe_id>', methods=['GET'])
def recipe_detail(recipe_id):
    """ Show recipe detail by id"""
    recipe_detail = get_recipe_detail(recipe_id)
    recipe_equipments = visualize_recipe_equipments(recipe_id)
    recipe_ingredients = visualize_recipe_ingredients(recipe_id)
    analyzed_instructions = get_analyzed_recipe_instructions(recipe_id)
    return render_template('recipes/recipe_detail.html', 
                            recipe_detail = recipe_detail,
                            recipe_summary = strip_tags(recipe_detail['summary']),
                            recipe_equipments = recipe_equipments,
                            recipe_ingredients = recipe_ingredients,
                            analyzed_instructions = analyzed_instructions)