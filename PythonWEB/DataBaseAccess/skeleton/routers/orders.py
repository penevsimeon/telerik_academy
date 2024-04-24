from fastapi import APIRouter, Response
from data.models import Order
from services import order_service
from services import product_service

orders_router = APIRouter(prefix='/orders')


@orders_router.get('/')
def get_orders(sort: str | None = None):
    orders = order_service.all()

    if sort and (sort == 'asc' or sort == 'desc'):
        return order_service.sort(orders, reverse=sort == 'desc')
    else:
        return orders


@orders_router.get('/{id}')
def get_order_by_id(id: int):
    order = order_service.get_by_id(id)

    if order is None:
        return Response(status_code=404)
    else:
        return order


@orders_router.post('/')
def create_order(order: Order):
    return order_service.create(order)


@orders_router.put('/{id}')
def update_order(id: int, order: Order):
    if order.product_ids == []:
        return Response(status_code=400, content='Must contain at least one product')

    if not all(product_service.exists(id) for id in order.product_ids):
        return Response(status_code=400, content='Must contain existing products')

    existing_order = order_service.get_by_id(id)
    if existing_order is None:
        return Response(status_code=404)

    existing_order = order_service.update(existing_order, order)
    return order_service.create_response_object(existing_order)


@orders_router.delete('/{id}')
def delete_order(id: int):
    order = order_service.get_by_id(id)

    if order is None:
        return Response(status_code=404)

    order_service.delete(order)

    return Response(status_code=204)
