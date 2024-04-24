from models.product import Product
from models.gender import Gender


class Toothpaste(Product):
    def __init__(self, name: str, brand: str, price: float, gender: str, ingredients: list):
        self.ingredients = ingredients
        if gender != Gender.MEN and gender != Gender.WOMEN and gender != Gender.UNISEX:
            raise ValueError('Gender can be only Men Women or Unisex')
        super().__init__(name, brand, price, gender)

    @property
    def ingredients(self):
        return tuple(self._ingredients)

    @ingredients.setter
    def ingredients(self, value: list):
        if len(value) < 0:
            raise ValueError('Ingredients must be more than 0')
        self._ingredients = value

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        if len(value) < 2 or len(value) > 10:
            raise ValueError("Brand has to be between 2 and 10 symbols")
        self._brand = value

    def to_string(self):
        product_to_string = super().to_string()
        joined_ingredients_string = ", ".join(self._ingredients)
        return f'{product_to_string}\n #Ingredients: [{joined_ingredients_string}]'
