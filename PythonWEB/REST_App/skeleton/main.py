import uvicorn
from fastapi import FastAPI, Response
from data import Product, products, orders, Order

app = FastAPI()


@app.get('/products')
def get_products(
        sort: str | None = None,
        search: str | None = None
):
    result = products

    if search:
        result = [p for p in result if (search.lower() in p.name.lower())]

    if sort and (sort == 'asc' or sort == 'desc'):
        result = sorted(result, key=lambda p: p.price, reverse=sort == 'desc')

    return result


@app.get('/products/{id}')
def get_product_by_id(id: int):
    product = next((p for p in products if p.id == id), None)

    if product is None:
        return Response(status_code=404)
    else:
        return product


@app.post('/products', status_code=201)
def create_product(product: Product):
    max_id = max(p.id for p in products)

    product.id = max_id + 1
    products.append(product)

    return product


@app.put('/products/{id}')
def update_product(id: int, product: Product):
    existing_product = next((p for p in products if p.id == id), None)

    if existing_product is None:
        return Response(status_code=404)
    else:
        existing_product.name = product.name
        existing_product.description = product.description
        existing_product.price = product.price

        return existing_product


@app.get('/orders')
def get_orders(sort: str | None = None):
    result = orders

    if sort and (sort == 'asc' or sort == 'desc'):
        result = sorted(result, key=lambda o: o.delivery_date, reverse=sort == 'desc')

    return result


@app.get('/orders/{id}')
def get_order_by_id(id: int):
    order = next((o for o in orders if id == o.id), None)

    if order is None:
        return Response(status_code=404, content='Must enter valid order ID')

    ordered_products = [p for p in products if p.id in order.product_ids]
    ordered_product_total = sum(p.price for p in ordered_products)

    if not ordered_products:
        return {
            'id': order.id,
            'customer': order.customer,
            'products': 'No products',
            'delivery_date': order.delivery_date
        }

    return {
        'id': order.id,
        'customer': order.customer,
        'products': ordered_products,
        'delivery_date': order.delivery_date,
        'order_total': ordered_product_total
    }


@app.post('/orders', status_code=201)
def create_order(order: Order):
    max_id = max(o.id for o in orders)
    order.id = max_id + 1

    valid_product_ids = [p.id for p in products]

    for product_id in order.product_ids:
        if product_id not in valid_product_ids:
            return Response(status_code=400, content='Must enter a valid product id')

    ordered_products = [p for p in products if p.id in order.product_ids]
    ordered_product_total = sum(p.price for p in ordered_products)

    orders.append(order)

    return {
        'id': order.id,
        'customer': order.customer,
        'products': ordered_products,
        'delivery_date': order.delivery_date,
        'order_total': ordered_product_total
    }


@app.put('/orders/{id}')
def edit_order(id: int, order: Order):
    existing_order = next((o for o in orders if o.id == id), None)

    if existing_order is None:
        return Response(status_code=404)
    else:
        existing_order.product_ids = order.product_ids
        existing_order.delivery_date = order.delivery_date

        return existing_order


# server start with uvicorn
if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8000)
