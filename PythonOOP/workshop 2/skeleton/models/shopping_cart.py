class ShoppingCart:
    def __init__(self):
        self._products = []

    @property
    def products(self):
        return tuple(self._products)

    def add_product(self, product):
        self._products.append(product)

    def remove_product(self, product):
        names = [p.name for p in self._products]
        if product.name not in names:
            raise ValueError(
                f'Product {product.name} not found in ShoppingCart')

        idx = names.index(product.name)
        self._products.pop(idx)

    def contains_product(self, product):
        return product.name in [p.name for p in self._products]

    def total_price(self):
        return sum((p.price for p in self._products))
