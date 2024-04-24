<img src="https://webassets.telerikacademy.com/images/default-source/logos/telerik-academy.svg" alt="logo" width="300px" style="margin-top: 20px;"/>

# Ordering App

_Part 2_

### 1. Description
The Ordering app has some of its functionality already implemented
- The product endpoints:
    - ✔ GET /products (*with optional query params*)
    - ✔ GET /products/{id}
    - ✔ POST /products
    - ✔ PUT /products/{id}
- Missing endpoints:
    - ✖ GET /orders (*with optional query params*)
    - ✖ GET /orders/{id}
    - ✖ POST /orders
    - ✖ PUT /orders/{id}
    - ✖ DELETE /orders/{id}
- Missing functionality:
    - Web client (*will be added later by the Frontend team*)
    - Console client (*will be added later by whoever is available*)

### 2. Goals  
- Practice writing GET, POST, PUT, and DELETE requests
- Practice data relations - `Product` <-> `Order`
- Practice using Postman (or other similar tools, if you prefer)

### 3. Tasks for today:
- Create an `Order` model
- Implement all the required **/orders** endpoints

### 4. Setup
You do not have to create new files - write all the code in the `main.py` or `data.py` files - but you are allowed to create new files, if you want to. 

### 5. Order model
Create an `Order` model in the `data.py` file (or a new file) that has the following attributes:

- id &rarr; int or None
- customer &rarr; str
- product_ids &rarr; list of ints
- delivery_date &rarr; date (*import the date type from the datetime module*) 

Look at the existing Product model - it will guide you for Pydantic-specific syntax. Don't forget to inherit from BaseModel. If everything is done correctly, copy and paste this code in the `data.py` file - this will be the collection of orders.

```py
orders = [
    Order(
        id = 1, 
        customer='Steven', 
        product_ids=[2,4], 
        delivery_date=date(2025, 2, 8)
    ),
    Order(
        id = 2, 
        customer='Alice', 
        product_ids=[1], 
        delivery_date=date(2023, 8, 4)
    )
]
```
We have defined two sample orders here, which we will use to test the **GET** endpoints that we will implement soon. The first order contains references for product with ids 2 and 4 - look at the products collection - these are "Laptop" and "Keyboard". The second order is for only one product - "Tv".  

> We use this approach in order not to duplicate data. Also, a change in a product should be reflected everywhere it's used. The same approach will be used when we study relational databases.

### 6. GET /orders

Implement the `GET /orders` endpoint. It should return all existing orders. Example with the sample data that we defined earlier:

REQUEST: `GET http://127.0.0.1:8000/orders`  (*your server may be started on a port that is not 8000*)

RESPONSE:
```json
[
    {
        "id": 1,
        "customer": "Steven",
        "product_ids": [
            2,
            4
        ],
        "delivery_date": "2025-02-08"
    },
    {
        "id": 2,
        "customer": "Alice",
        "product_ids": [
            1
        ],
        "delivery_date": "2023-08-04"
    }
]
```

Enhance the endpoint to accept an optional query parameter `sort`. If it is provided, sort the orders by delivery_date in ascending or descending order. Look at the existing products endpoint for inspiration. Examples of valid requests:
- `/orders`
- `/orders?sort=asc`
- `/orders?sort=desc`

### 7. GET /orders/{id}

Implement the `GET /orders/{id}` endpoint. It returns **additional data** about an order found by id. Return NOT FOUND status if an order with that id does not exist.
Additional information:
- `products` - the collection contains info about the products, not just their ids
- `order_total` - the total cost of the order. If the cost is higher than 125, apply a 2% shipping fee.

In order to return a more **detailed** order response, you can use an additional class, or a dictionary. **Do not even think of modifying existing data, as that will lead to an infinite amount of bugs!!!**

REQUEST: `GET http://127.0.0.1:8000/orders/1`

RESPONSE:
```json
{
    "id": 1,
    "customer": "Steven",
    "products": [
        {
            "id": 2,
            "name": "Laptop",
            "description": "2x2.6 GHz CPU; 6GB RAM; HD Graphics",
            "price": 699.99
        },
        {
            "id": 4,
            "name": "Keyboard",
            "description": "Full-size Layout, Mechanical",
            "price": 99.0
        }
    ],
    "delivery_date": "2025-02-08",
    "order_total": 814.9698000000001
}
```

### 8. POST /order
Create an endpoint that can be used to place a new order. Validate that all the passed product ids actually exist as products, and that at least one product is ordered. As a response, return the newly created order in the same format as the `GET /order/{id}` endpoint. Generate the order's id on the server

REQUEST: `POST http://127.0.0.1:8000/orders`
```json
{
    "customer": "Jill",
    "product_ids": [4],
    "delivery_date": "2022-12-12"
}
```

RESPONSE:
```json
{
    "id": 3,
    "customer": "Jill",
    "products": [
        {
            "id": 4,
            "name": "Keyboard",
            "description": "Full-size Layout, Mechanical",
            "price": 99.0
        }
    ],
    "delivery_date": "2022-12-12",
    "order_total": 99.0
}
```

Example when a product does not exist. For example: no product with id 8

REQUEST: `POST http://127.0.0.1:8000/orders`
```json
{
    "customer": "Jill",
    "product_ids": [8],
    "delivery_date": "2022-12-12"
}
```

RESPONSE:
```none
Status Code: 400
Must contain existing products
```

After implementing the endpoint and creating an order, verify that the `GET /orders` and `GET /orders/{id}` endpoints return the new order


### 9. PUT /order/{id}
Create an endpoint that can be used to edit an order. The endpoint must find the order by id and change the ordered products and or the delivery date. Return NOT FOUND there is no order with such an id. Similar to creating orders, validate that the product ids exist. Return the modified order in the same detailed format as `POST /orders` and `GET /orders/{id}`

REQUEST: `PUT http://127.0.0.1:8000/orders/1`
```json
{
    "customer": "Steven",
    "product_ids": [1,2,3],
    "delivery_date": "2022-12-12"
}
```

RESPONSE:
```json
{
    "id": 1,
    "customer": "Steven",
    "products": [
        {
            "id": 1,
            "name": "TV",
            "description": "LCD 40 Inch",
            "price": 749.99
        },
        {
            "id": 2,
            "name": "Laptop",
            "description": "2x2.6 GHz CPU; 6GB RAM; HD Graphics",
            "price": 699.99
        },
        {
            "id": 3,
            "name": "Smartphone",
            "description": "6.55\" HD+, 5G",
            "price": 1349.9
        }
    ],
    "delivery_date": "2022-12-12",
    "order_total": 2855.8776000000003
}
```

### 10. DELETE /order/{id}
Implement endpoint to delete orders. Return either 204 NO CONTENT or 404 NOT FOUND, depending on whether such an order exists. This request has no body. To delete an order - simply remove it from the orders collection. Use the GET endpoints to verify that the order is deleted.

REQUEST: `DELETE http://127.0.0.1:8000/orders/1`

RESPONSE:
```none
Status Code: 204
```