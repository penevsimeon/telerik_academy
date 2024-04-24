class ShoppingCart:
    def __init__(self):
        self._products = []

    @property
    def products(self):
        return tuple(self._products)

    def add_product(self, product):
        self._products.append(product)

    def remove_product(self, product):
        self._products.remove(product)

    def contains_product(self, product):
        return product in self._products

    def total_price(self):
        return sum(x.price for x in self._products)

