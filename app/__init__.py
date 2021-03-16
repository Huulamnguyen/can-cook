""" Application """
from flask import Flask, render_template
from config import config
from .recipe import get_random_joke, get_random_recipes

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
