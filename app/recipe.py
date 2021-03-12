import requests
from secret import API_KEY

# Food API BASE URL
API_BASE_URL = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/"

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
number_per_page = str(10)

def get_random_joke():
    """ Get Random Food Jokes """
    response = requests.request("GET", API_BASE_URL+random_joke_route, headers=headers)
    random_joke = response.json()
    return random_joke['text']

def get_random_recipes():
    """ Get random recipes """
    querystring = {"number":number_per_page}
    response = requests.request("GET", API_BASE_URL+random_recipes_route, headers=headers, params=querystring)
    random_recipes = response.json()
    return random_recipes['recipes']