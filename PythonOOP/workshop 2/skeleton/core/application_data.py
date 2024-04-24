from models.category import Category
from models.product import Product
from models.shampoo import Shampoo
from models.shopping_cart import ShoppingCart
from models.toothpaste import Toothpaste


def format_usage_type(usage_type):
    words = usage_type.split('_')
    formatted = ''.join(word.capitalize() for word in words)
    return formatted


class ApplicationData:
    def __init__(self):
        self._products = []
        self._categories = []
        self._shopping_cart = ShoppingCart()

    @property
    def products(self):
        return tuple(self._products)

    @property
    def categories(self):
        return tuple(self._categories)

    @property
    def shopping_cart(self) -> ShoppingCart:
        return self._shopping_cart

    def find_product_by_name(self, name) -> Product:
        for product in self._products:
            if product.name == name:
                return product

        raise ValueError(f'Product {name} does not exist!')

    def find_category_by_name(self, name) -> Category:
        for category in self._categories:
            if category.name == name:
                return category

        raise ValueError(f'Category {name} does not exist!')

    def create_category(self, name) -> None:
        if self.category_exists(name):
            raise ValueError(f'Category {name} already exists!')

        category = Category(name)
        self._categories.append(category)

    def create_shampoo(self, name, brand, price, gender, usage_type, milliliters) -> Shampoo:
        if self.product_exists(name):
            raise ValueError('This shampoo already exists!')
        shampoo = Shampoo(name, brand, price, gender, usage_type, milliliters)
        self._products.append(shampoo)
        return shampoo

    def create_toothpaste(self, name, brand, price, gender, ingredients) -> Toothpaste:
        if self.product_exists(name):
            raise ValueError('This toothpaste already exists!')
        toothpaste = Toothpaste(name, brand, price, gender, ingredients)
        self._products.append(toothpaste)
        return toothpaste

    def category_exists(self, name) -> bool:
        return name in [c.name for c in self._categories]

    def product_exists(self, name) -> bool:
        return name in [p.name for p in self._products]
