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
- Data will be sourced from [ECart API](https://ecartapi.com/)

## Back-end Outline

### Database Schema

### Languages and Framework
- Python
- Flask
- PostgreSQL

### Features / Endpoint:
- `/` homepage shows application's introduction
- `/register` GET:show form to register - POST:create an account
- `/login` GET: show form - POST: login existing users
- `/logout` POST: logout user
- `/products` GET: show all active products and form to filter - POST: filter product
- `/product/add` GET: show form to add new product - POST: handle form
- `/product/<product_id/update` GET: show form to update existing product - POST: handle form
- `/product/type` GET: show all product types - POST: Update product type - DELETE: delete product type
- `/product/supplier` GET: show all supplier - POST: Update supplier - DELETE: delete supplier
- `/procuct/brand` GET: show all brands - POST: Update brand - DELETE: delete brand
- `/procuct/tag` GET: show all tags - POST: Update tag - DELETE: delete tag
