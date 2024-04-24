<img src="https://webassets.telerikacademy.com/images/default-source/logos/telerik-academy.svg" alt="logo" width="300px" style="margin-top: 20px;"/>

# Ordering App

_Part 4_

### 1. Description
The Ordering app has some of its functionality already implemented
- Product endpoints:
    - ✔ GET /products (*with optional query params*)
    - ✔ GET /products/{id}
    - ✔ POST /products
    - ✔ PUT /products/{id}
- Order endpoints:
    - ✔ GET /orders (*with optional query params*)
    - ✔ GET /orders/{id}
    - ✔ POST /orders
    - ✔ PUT /orders/{id}
    - ✔ DELETE /orders/{id}
    - ✖ PUT /orders/{id}/products
    - ✖ DELETE /orders/{id}/products
- Category endpoints:
    - ✔ GET /categories
    - ✔ GET /categories/{id}
    - ✔ POST /categories
- Missing functionality:
    - Web client (*will be added later by the Frontend team*)
    - Console client (*will be added later by whoever is available*)

### 2. Goals  
- Practice database design
- Practice writing SQL queries
- Practice connecting Python code with a relational database

### 3. Tasks for today:
- Install mariadb connector
- Add additional database tables
- Rewrite the order_service to use read/write database data



### 4. Before you start
Python uses a **connector** for executing SQL queries. Install it with
```
pip install mariadb
```

Look at the refactored `product_service` and `category_service` to get a basic idea of how python code is integrated with SQL. Also check the `data.database` module and inspect the code there. You can use the `read_query`, `insert_query`, `update_query` functions in your `order_service`.

### 5. Alter the database schema

Currently, orders data resides in-memory in the `data.in_memory` module. Study the data attributes and decide on what columns the additional table(s) will need. There is a relation between the products and the orders. To determine its type, think of the answer to the following questions:
- How many products can an order have?
- Each product can be part of how many orders?

### 6. Rewrite the `order_service`

Change the implementation of the order service to query data from the database. Study the existing `product_service` and `category_service` functionality to get a basic idea of how that can be achieved.

The mariadb connector returns queried rows as a list of tuples:
```python
data = read_query(
            '''SELECT id, name, description, price, category_id
               FROM products''')

# data:
[
    (1,'TV','LCD 40 Inch',749.99,2),
    ...,
    (7,'Headphones','Black, Wireless',39,1)
]
```
You can write logic to convert the list of tuples to a list of Pydantic models for a more understandable abstraction. An example of how that can be achieved is present in the existing services and models.

You are allowed to change the existing function signatures where necessary.

### 7. Refactor the `PUT` `/orders/{id}` endpoint

In order to provide a more flixible API, split the endpoint into three parts
- `PUT /orders/{id}` - change the endpoint to accept only delivery_date and delivery_address. You will need to add the new column delivery_address to the orders table in the database.
- `PUT /orders/{id}/products`- adds more products to the order. You may accept the new products as a list of ids, for example. Decide what happens if some of the product ids are already part of the order, or do not exist in the database at all.
- `DELETE /orders/{id}/products`- removes products from the order. Decide what response to return if some of the ids are not part of the actual order.

