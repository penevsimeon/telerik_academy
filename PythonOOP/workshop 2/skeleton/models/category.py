class Category:
    def __init__(self, name):
        self.name = name
        self._products = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if len(value) < 2 or len(value) > 15:
            raise ValueError('Name should be between 2 and 15 symbols.')

        self._name = value

    @property
    def products(self):
        return tuple(self._products)

    def add_product(self, product):
        if product.name in [p.name for p in self._products]:
            raise ValueError(
                f'Product {product.name} already added to category {self.name}')
        
        self._products.append(product)

    def remove_product(self, product):
        names = [p.name for p in self._products]
        if product.name not in names:
            raise ValueError(
                f'Product {product.name} not found in category {self.name}')

        idx = names.index(product.name)
        self._products.pop(idx)

    def to_string(self):
        new_line = '\n'
        if len(self._products) > 0:
            product_strings = [p.to_string() for p in self._products]
            return f'#Category: {self.name}{new_line}{new_line.join(product_strings)}'
        else:
            return f'#Category: {self.name}{new_line} #No products in this category'
