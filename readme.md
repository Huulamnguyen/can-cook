# Inventory Management System

## Project Idea:
- Name: CanCook
- Food Suggestion for people who love cooking.
- People can search many receipes base on what they have on their refrigerators.
- Learn how to cook their favorite dishes.

## Website Goal
- Receipe management.
- Search ad filter for recipes and Ingredients.
- Create and manage favorite receipes list.
- Learn how to cook step by step with image.

## User Demographics
- People who is looking for receipes that they love.
- Cooking learner.
- Food lover.

## API Data
- Food API. Learn more about Food API Docs [here](https://spoonacular.com/food-api/docs)

## Back-end Outline

### Languages and Framework
- Python
- Flask
- PostgreSQL

### Features / Endpoint:

#### User
- **GET** `/recipes/random` homepage shows application's landing page, show random receipes.
- **GET** `/register` show form to register 
- **POST** `/register` create an account
- **GET** `/login` show form 
- **POST** `/login` login existing users
- **POST** `/logout` logout user

#### Recipe
- **GET** `/recipes/autocomplete` Autocomplete a partial input to suggest possible recipe names.
- **GET** `/recipes/{id}/information` Show recipe's information, includes: image of the recipe, recipe taste, recipe equipment, recipe ingredient, and analyzed recipe instruction
- **GET** `recipes/findByIngredients` Find recipes that use as many of the given ingredients as possible and require as few additional ingredients as possible.
- **POST** `recipes/{id}/add` Add recipe to favorite collection.
- **PUT** `recipes/{id}/edit` Edit recipe name
- **DELETE** `recipes/{id}/delete` Delete favorite recipe.

### Issue with Ecart API
- Academic purpose only for 3 months

### Sensitive Information
- passwords will be hashed with bcrypt.
- use session or JWT to keep track of authenticated user.
- API keys need to be protected.

## Front-end Outline

### Languages / Frameworks
- JavaScript
- Ajax
- HTML
- CSS
- Jinja
- Bootstrap

## User Flow

### All Users
- User without registration can search recipe and Ingredient.
- User can view recipe's information and Ingredient's information.

### Registered Users
- User can add recipes to favorite collection.


## Testing:
- Using [unittest](https://docs.python.org/3/library/unittest.html) - Python unit test framework
- Travis CI 

## Deployment:
- [Heroku with Python](https://devcenter.heroku.com/articles/getting-started-with-python)

## Workflow:
- Git workflow

## Additional Details:

### Features beyond simple CRUD
- Interactive Point-of-sale to make new order

### Stretch goals / possible features
- Allow user to add image for product.
- Can connect to many e-commerce platforms such as Shopify, Woocommerce, Wix, Kometia, Mercado Libre, Ebay, TradeGecko
- Update to API paid version to access more Requests.
