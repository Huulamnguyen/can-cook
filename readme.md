# Inventory Management System

## Project Idea:
- Food Suggestion for people who love cooking.
- People can search many receipes base on what they have on their refrigerator.

## Website Goal
- Receipe management.
- Search ad filter for receipe.
- Create and manage favorite receipes list.

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
- **GET** `/` homepage shows application's landing page.
- **GET** `/register` show form to register 
- **POST** `/register` create an account
- **GET** `/login` show form 
- **POST** `/login` login existing users
- **POST** `/logout` logout user
(* User **must** log in to access to endpoints below)

### Issue with Ecart API
- For free version 1,000 API Requests License

### Sensitive Information
- passwords will be hashed with bcrypt
- use session or JWT to keep track of authenticated user
- API keys need to be protected

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
