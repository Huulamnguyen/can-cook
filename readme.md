# Inventory Management System

## Project Idea:
- As a member of a retailer in New York. I experienced difficulty managing inventory without using any technology.
- My idea is inspired by a cloud application named VEND, which is a big inventory management system software in New Zealand. You can find more at [VENDHQ.com](https://www.vendhq.com/) and images below.

## Website Goal
- Product mangement
- Order and Inventory

## User Demographics
- Retailer who want to organize product, inventory and order in one place.

## API Data
- Data will be sourced from [ECart API](https://ecartapi.com/). Learn more at [ECart API document](https://docs.ecartapi.com/)
- The API has free version for academic

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
- **<span style="color:blue">some *blue* text</span>** `/categories/{{id}}` Category Update. Actualize the selected category information.
