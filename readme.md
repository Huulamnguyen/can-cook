# Inventory Management System

## Project Idea:
- Name: CanCook
- Food Suggestion for people who love cooking.
- People can search many receipes base on what available ingredients on their refrigerators.
- Learn how to cook step-by-step with images.
- Get a estimated cost for a recipe.

## Website Goal
- Searching for recipes by name and ingredients.
- Create and manage favorite recipes list.
- Learn how to cook step by step with ingredient images and equipments images.
- - Get a estimated cost for a recipe.

## User Demographics
- People who is looking for receipes that they love.
- Cooking learner.
- Food lover.
## Database Schema
 ![cancook EER Diagram](/cancook-diagram.png)

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
- **GET** `/recipes/{id}/information` Show recipe's information, includes: image of the recipe, recipe taste, recipe equipment, recipe ingredient, and analyzed recipe instructio, price breakdown.
- **GET** `recipes/findByIngredients` Find recipes that use as many of the given ingredients as possible and require as few additional ingredients as possible.
- **POST** `/user/{id}/recipes/{id}/add` Add recipe to favorite collection. (User must be authorized account)
- **PUT** `/user/{id}/recipes/{id}/edit` Edit recipe name. (User must be authorized account)
- **DELETE** `/user/{id}/recipes/{id}/delete` Delete favorite recipe. (User must be authorized account)

### Issue with Spoocular Food API
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
- User without authorized registration can search recipe by name and ingredients
- User can view recipe's information such as: Image, Ingredients, Equipment, Instruction.

### Registered Users
- User can add, edit, delete recipes to favorite collection.

## Testing:
- Using [unittest](https://docs.python.org/3/library/unittest.html) - Python unit test framework
- Travis CI 

## Deployment:
- [Heroku with Python](https://devcenter.heroku.com/articles/getting-started-with-python)

## Workflow:
- Git workflow

## Additional Details:

### Features beyond simple CRUD
- Recommend recipes by user's interest

### Stretch goals / possible features
- Improve font-end.
- Live interactive Chat Box.
- Add Recipe Price Breakdown with estimated cost and show total cost for the recipe.
- Develop shopping list.
