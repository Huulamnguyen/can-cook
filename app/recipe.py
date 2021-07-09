import requests, os
from dotenv import load_dotenv

# Food API BASE URL
API_BASE_URL = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/"

# Access API_KEY
load_dotenv()
API_KEY = os.environ.get("API_KEY")

# Headers
headers = {
    'x-rapidapi-key': API_KEY,
    'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
};

# Visualized Headers
v_headers = {
        'accept': "text/html",
        'x-rapidapi-key': API_KEY,
        'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com"
};

# Food API Routes
random_joke_route = "food/jokes/random"
random_recipes_route = "recipes/random"
search_by_name_route = "recipes/search"



# Set Up 10 Recipes per search page
number_per_page = str(12)

def get_random_joke():
    """ Get Random Food Jokes """
    querystring = {"number":number_per_page,"tags":"main course, lunch, main dish, dinner"}
    response = requests.request("GET", API_BASE_URL+random_joke_route, headers=headers, params=querystring)
    random_joke = response.json()
    return random_joke['text']

def get_random_recipes():
    """ Get random recipes """
    querystring = {"number":number_per_page}
    response = requests.request("GET", API_BASE_URL+random_recipes_route, headers=headers, params=querystring)
    random_recipes = response.json()
    return random_recipes['recipes']

def search_recipes(q):
    """ Get recipes by searching name """
    querystring = {"query":q, "number":number_per_page, "type":"main course, lunch, main dish, dinner"}
    response = requests.request("GET", API_BASE_URL+search_by_name_route, headers=headers, params=querystring)
    recipes = response.json()
    return recipes['results']

def get_recipe_detail(recipe_id):
    """Get recipes detail/information by id"""
    querystring = {"includeNutrition":"false"}
    url = API_BASE_URL+"recipes/"+str(recipe_id)+"/information"
    recipe_detail = requests.request("GET", url, headers=headers, params=querystring)
    recipe_detail = recipe_detail.json()
    return recipe_detail

def get_analyzed_recipe_instructions(recipe_id):
    """ Get Analyzed Instructions step-by-step by id"""
    url = API_BASE_URL+"recipes/"+str(recipe_id)+"/analyzedInstructions"
    querystring = {"stepBreakdown":"true"}
    analyzed_instructions = requests.request("GET", url, headers=headers, params=querystring)
    return analyzed_instructions.json()

def visualize_recipe_equipments(recipe_id):
    """ Get visualized recipe equipment by id """
    querystring = {"defaultCss":"true", "showBacklink":"false"}
    url = API_BASE_URL+"recipes/"+str(recipe_id)+"/equipmentWidget"
    recipe_equipments = requests.request("GET", url, headers=v_headers, params=querystring).text
    return recipe_equipments

def visualize_recipe_ingredients(recipe_id):
    """ Get Visualized Recipe Ingredient by id"""
    querystring = {"defaultCss":"true"}
    url = API_BASE_URL+"recipes/"+str(recipe_id)+"/ingredientWidget"
    recipe_ingredients = requests.request("GET", url, headers=v_headers, params=querystring).text
    return recipe_ingredients