from datetime import date
from data.models import Order


orders = [
    Order(id = 1, customer='Steven', product_ids=[2,4], delivery_date=date(2025, 2, 8)),
    Order(id = 2, customer='Alice', product_ids=[1], delivery_date=date(2023, 8, 4))
]
