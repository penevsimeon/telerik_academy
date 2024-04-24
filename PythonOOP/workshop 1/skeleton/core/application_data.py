from models.category import Category
from models.product import Product
from models.shopping_cart import ShoppingCart


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
        raise ValueError("This product does not exist")

    def find_category_by_name(self, name) -> Category:
        for category in self._categories:
            if category.name == name:
                return category
        raise ValueError("This category does not exist")

    def create_category(self, name) -> None:
        if self.category_exists(name):
            raise ValueError("This category already exist")
        self._categories.append(Category(name))

    def create_product(self, name, brand, price, gender) -> None:
        if self.product_exists(name):
            raise ValueError("This product already exist")
        self._products.append(Product(name, brand, price, gender))

    def category_exists(self, name) -> bool:
        return name in [category.name for category in self._categories]

    def product_exists(self, name) -> bool:
        return name in [product.name for product in self._products]
