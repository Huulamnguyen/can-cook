[![Maintainability](https://api.codeclimate.com/v1/badges/cc0fbf96872d2e85c524/maintainability)](https://codeclimate.com/github/Huulamnguyen/can-cook/maintainability)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/6429759713614b98bbae79457218f5ed)](https://app.codacy.com/gh/Huulamnguyen/can-cook?utm_source=github.com&utm_medium=referral&utm_content=Huulamnguyen/can-cook&utm_campaign=Badge_Grade_Settings)
[![Coverage Status](https://coveralls.io/repos/github/Huulamnguyen/can-cook/badge.svg?branch=main)](https://coveralls.io/github/Huulamnguyen/can-cook?branch=main)
[![Build Status](https://www.travis-ci.com/Huulamnguyen/can-cook.svg?branch=main)](https://www.travis-ci.com/Huulamnguyen/can-cook)
# CanCook

## Project Idea:
- Name: CanCook
- Food Suggestion for people who love cooking.
- People can search many recipes base on what available ingredients on their refrigerators.
- Learn how to cook step-by-step with images.
- Get a estimated cost for a recipe.

## Website Goal
- Searching for recipes by name and ingredients.
- Create and manage favorite recipes list.
- Learn how to cook step by step with ingredient images and equipments images.
- Get a estimated cost for a recipe.

## User Demographics
- People who are looking for recipes.
- Cooking learner.
- Food lover.
## Database Schema
 ![cancook EER Diagram](/asset/eer-cancook.png)

## API Data
- Food API. Learn more about Food API Docs [here](https://spoonacular.com/food-api/docs)

## Back-end Outline

### Languages and Framework
- Python
- Flask
- PostgreSQL

### Features / Endpoint:

#### User
- **GET** `/` show homepage, random Food Joke, random recipes
- **GET** `/register` show form to register 
- **POST** `/register` create an account
- **GET** `/login` show form 
- **POST** `/login` login existing users
- **POST** `/logout` logout user
- **GET** `/user` show user details and favorite recipes.
- **GET** `/user/edit` show user details edit form.
- **POST** `/user/edit` edit or update user's information.
- **DELETE** `/user/delete` delete entire user account and appropriated favorite recipes.

#### Searching Recipe by Name And Ingredients.
- **GET** `/recipes` show recipes by name. OR, recipes by ingredients. OR, random recipes if user don't search any name.
- **GET** `/recipes/{recipe_id}` Show recipe's information, includes: image of the recipe, recipe equipment, recipe ingredient, and get analyzed recipe instruction.
#### Endpoint For Authorized Users.
- **GET** `/user/favorites` Show all favorite recipes on the navbar and under under detail page.
- **POST** `/recipes/{recipe_id}/like` Add recipe to favorite list. 
- **DELETE** `/recipes/{recipe_id}/remove` Remove favorite recipe from favorites list.

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
- User without authorized registration can search recipe by name and ingredients.
- User can view recipe's information such as: Image, Ingredients, Equipment, Instruction.

### Registered Users
- Authorized Users can add, edit, delete recipes to personal favorite collection.
- Authorized Users can view recipe's ingredient price breakdown.

## Testing:
- Using [unittest](https://docs.python.org/3/library/unittest.html) - Python unit test framework
- Travis CI 

## Deployment:
- [Heroku with Python](https://devcenter.heroku.com/articles/getting-started-with-python)

## Workflow:
- Git workflow
- CI/CD Pipeline

## Additional Details:

### Features beyond simple CRUD
- Recommend recipes by user's interest.

### Stretch goals / possible features
- Allows user to change password.
- Improve font-end.
- Live interactive Chat Box.
- Develop shopping list.
- Get Similar Recipes.