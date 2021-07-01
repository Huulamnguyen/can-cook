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
}

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