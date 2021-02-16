# CanCook

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
- Get a estimated cost for a recipe.

## User Demographics
- People who is looking for receipes that they love.
- Cooking learner.
- Food lover.
## Database Schema
 ![cancook EER Diagram](/asset/cancook-diagram.png)

## API Data
- Food API. Learn more about Food API Docs [here](https://spoonacular.com/food-api/docs)

## Back-end Outline

### Languages and Framework
- Python
- Flask
- PostgreSQL

### Features / Endpoint:

#### User
- **GET** `/home` homepage shows application's landing page, show random receipes.
- **GET** `/register` show form to register 
- **POST** `/register` create an account
- **GET** `/login` show form 
- **POST** `/login` login existing users
- **POST** `/logout` logout user
- **GET** `/user` show user details and favorite recipes.
- **GET** `/user/edit` show user details edit form.
- **POST** `/user/edit` edit or update user's information.

#### Searching Recipe by Name And Ingredients.
- **GET** `/recipes` Autocomplete a partial input to suggest possible recipe names. 
- **GET** `/recipes/{recipe_id}` Show recipe's information, includes: image of the recipe, recipe taste, recipe equipment, recipe ingredient, and analyzed recipe instruction.
- **GET** `/ingredients` Find recipes that use as many of the given ingredients as possible and require as few additional ingredients as possible.
- **GET** `/ingredients/{ingredient_id}` Show ingredient's information.

#### Endpoint For Authorized Users.
- **GET** `/user/{user_id}/favorite` Show all favorite receipes.
- **GET** `/recipes/{recipe_id}/price` Show recipe's estimated price breakdown for each and total ingredients.
- **POST** `/recipes/{recipe_id}/like` Add recipe to favorite collection. 
- **DELETE** `/recipes/{recipe_id}/unlike` Delete favorite recipe.

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
- Improve font-end.
- Live interactive Chat Box.
- Develop shopping list.
