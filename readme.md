# Inventory Management System

## Project Idea:
- As a member of a retailer in New York. I experienced difficulty managing inventory without using any technology.
- My idea is inspired by a cloud application named VEND, which is a big inventory management system software in New Zealand. 
- You can find more at [VENDHQ.com](https://www.vendhq.com/) and images below.

## Website Goal
- Product mangement
- Order and Inventory Management
- Customer Management

## User Demographics
- Restaurant and retailer who want to organize product, inventory, order, and customer in one place.

## API Data
- Data will be sourced from [ECart API](https://ecartapi.com/). Learn more at [ECart API document](https://docs.ecartapi.com/)
- The API has free version, but limit 1000 Requests.

## Back-end Outline

### Languages and Framework
- Python
- Flask
- PostgreSQL

### Features / Endpoint:

#### User
- **GET** `/` homepage shows application's introduction
- **GET** `/register` show form to register 
- **POST** `/register` create an account
- **GET** `/login` show form 
- **POST** `/login` login existing users
- **POST** `/logout` logout user
(* User **must** log in to access to endpoints below)

#### Products: 
This resource represents the store's inventory.
- **GET** `/products` Get all products.
- **GET** `/products/count` Count all products.
- **GET** `products/{{id}}` Get single product. Searches for a selected product and shows the detailed information.
- **GET** `/products/{{productId}}/variants` Get all product variants. Searches for all the registered variants of a single product.
- **GET** `/products/{{productId}}/variants/{{id}}` Get single product variant. Searches for the selected variant and shows the detailed information.
- **GET** `/products/{{productId}}/images` Get all product images. Searches for all the images of a single product.
- **GET** `/products/{{productId}}/images/{{id}}` Get a single product image. Searches for the selected image of a product.
- **POST** `/products` add new product to the API
- **POST** `/products/{{productId}}/variants` Variants. Creates a variation of an available product.
- **POST** `/products/{{productId}}/images` Images. Adds a new image to an existing product.
- **PUT** `/products/{{id}}` Product Update. Updates the product information, according to new detailed information.
- **PUT** `/products/{{productId}}/variants/{{id}}` Variant Update. Updates the information of an already existing product variant.
- **DEL** `/products/{{id}}` Delete product. Permanently delete the selected product.
- **DEL** `/products/{{productId}}/variants/{{id}` Delete variant. Permanently deletes a product's variation.
- **DEL** `/products/{{productId}}/images/{{id}}` Delete image. Permanently deletes the selected image of a product.

#### Categories:
This resource represents the categories the store has.
- **GET** `/categories` Searches for all the available categories.
- **GET** `/categories/count` Count all categories
- **GET** `/categories/{{id}}` Get a single category. Searches for the selected category and shows detailed information.
- **POST** `/categories` Create a new category.
- **PUT** `/categories/{{id}}` Category Update. Actualize the selected category information.
- **DEL** `/categories/{{id}}` Delete Category. Permanently deletes the selected category.

#### Customers:
This resource shows and manages the saved information about the store's customers.
- **GET** `/customers` Get all customers.
- **GET** `/customers/count` Count all costumers.
- **GET** `/customers/{{id}}` Get a single customer. Searches for the selected customer and shows detailed information.
- **POST** `/customers` Registers a new costumer.
- **PUT** `/customers/{{id}}` Customers Update. Update the selected costumer's information.
- **DEL** `/customers/{{id}}` delete Customer. Permanently deletes the selected customer.

#### Orders
This resource shows and manages the saved information about the store's orders.
- **GET** `/orders` get all orders.
- **GET** `/orders/count` Count all orders.
- **GET** `/orders/{{id}}` Get a single order
- **POST** `/orders` Creates new orders.
- **PUT** `/orders/{{id}}` Order update. Update an order's information.
- **DEL** `/orders/{{id}}` delete order. Permanently deletes the selected order.
- **POST** `/orders/{{id}}/cancel` cancel order. 

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
- User can only access to homepage to view the app introduction
- To access to endpoints/feature, user must register

### Registered Users
- User can view three main functions: Sell, Product, Customer.

#### Sell
- User can search product on a search bar -> Create a new order -> Add selected product to a order -> Add quantity or unchose selected product -> cancel order or process to payment
- User can view all categories on Sell view.
- Order history -> edit order or cancel order.

#### Products
- User can search or filter product by name, productType, tags, vendor.
- Then, it will show list of  appropriate products or all products.
- Add new product.
- Edit or delete existing product.

#### Customer
- View all customers
- Add new customer
- Edit or delete existing customer
- View customer with order history

## Testing:
- Using [unittest](https://docs.python.org/3/library/unittest.html) - Python unit test framework

## Deployment:
- [Heroku with Python](https://devcenter.heroku.com/articles/getting-started-with-python)

## Additional Details:

### Features beyond simple CRUD
- Interactive Point-of-sale to make new order

### Stretch goals / possible features
- Allow user to add image for product.
- Can connect to many e-commerce platforms such as Shopify, Woocommerce, Wix, Kometia, Mercado Libre, Ebay, TradeGecko
- Update to API paid version to access more Requests.
