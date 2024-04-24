from data.models import Order
from data.in_memory import orders
from services import product_service
from data.database import read_query, insert_query, update_query


def _create_orders_dict(data):
    orders_dict = {}

    for oid, ocustomer, oproducts_id, odelivery_date in data:
        if oid not in orders_dict:
            orders_dict[oid] = Order.from_query_result(oid, ocustomer, [], odelivery_date)

        orders_dict[oid].product_ids.append(oproducts_id)

    return orders_dict


def _create_orders_list(orders_dict: dict):
    orders_list = []

    for obj in orders_dict.values():
        orders_list.append(obj)

    return orders_list


def all():
    data = read_query('''SELECT o.id, o.customer, op.products_id, o.delivery_date FROM orders o JOIN orders_has_products op ON o.id=op.orders_id
''')
    orders_dict = _create_orders_dict(data)
    orders_list = _create_orders_list(orders_dict)

    return orders_list


def sort(lst: list[Order], reverse=False):
    return sorted(
        lst,
        key=lambda o: o.delivery_date,
        reverse=reverse)


def get_by_id(id: int):
    data = read_query('''SELECT o.id, o.customer, op.products_id, o.delivery_date FROM orders o JOIN orders_has_products op ON o.id=op.orders_id
where o.id = ?''', (id,))

    orders_dict = {}

    for oid, ocustomer, oproducts, odelivery_date in data:
        if oid not in orders_dict:
            orders_dict[oid] = Order.from_query_result(oid, ocustomer, [], odelivery_date)

        orders_dict[oid].product_ids.append(oproducts)

    products = [product_service.get_by_id(pid) for pid in orders_dict[id].product_ids]
    products_total = sum(p.price for p in products)

    return {
        'id': orders_dict[id].id,
        'customer': orders_dict[id].customer,
        'products': products,
        'delivery_date': orders_dict[id].delivery_date,
        'order_total': products_total
    }


def create(order: Order):
    data = read_query('''select max(id) from orders''')  # [(4,)]
    new_id = data[0][0] + 1
    new_data = insert_query('''INSERT INTO orders (id, customer, delivery_date) VALUES (?, ?, ?)''',
                            (new_id, order.customer, order.delivery_date,))
    product_ids = read_query('''select id from products''')
    valid_product_ids = []
    for i in range(len(product_ids)):
        valid_product_ids.append(product_ids[i][0])

    for product_id in order.product_ids:
        if product_id in valid_product_ids:
            insert_query('''insert into orders_has_products (orders_id, products_id) values (?,?)''',
                         (new_id, product_id,))

    products = [product_service.get_by_id(pid) for pid in order.product_ids]
    products_total = sum(p.price for p in products)

    return ('Order successfully added!',
            {
                'id': new_id,
                'customer': order.customer,
                'products': products,
                'delivery_date': order.delivery_date,
                'order_total': products_total
            })


def update(old: Order, new: Order):
    pass


def delete(order):
    pass


def create_response_object(order: Order):
    FREE_SHIPPING_LIMIT = 125.0
    SHIPPING_FEE = 1.02

    order_products = [product_service.get_by_id(id)
                      for id in order.product_ids]

    order_total = sum(p.price for p in order_products)
    if order_total > FREE_SHIPPING_LIMIT:
        order_total = order_total * SHIPPING_FEE

    return {
        'id': order.id,
        'customer': order.customer,
        'products': order_products,
        'delivery_date': order.delivery_date,
        'order_total': order_total
    }
