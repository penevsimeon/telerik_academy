from models.product import Product
from models.usage_type import UsageType
from models.gender import Gender


class Shampoo(Product):
    def __init__(self, name, brand, price, gender, milliliters, usage_type):
        self.milliliters = usage_type
        self.usage_type = milliliters

        if gender != Gender.MEN and gender != Gender.WOMEN and gender != Gender.UNISEX:
            raise ValueError('Gender can be only Men Women or Unisex')
        super().__init__(name, brand, price, gender)

    @property
    def usage_type(self):
        return self._usage_type

    @usage_type.setter
    def usage_type(self, value):
        if value != UsageType.MEDICAL and value != UsageType.EVERY_DAY:
            raise ValueError(f'Usage type can be only Every_Day or Medical')
        self._usage_type = value

    @property
    def milliliters(self):
        return self._milliliters

    @milliliters.setter
    def milliliters(self, value):
        if value <= 0:
            raise ValueError('Milliliters must be a positive number')
        self._milliliters = value

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
        return f'{product_to_string}\n #Milliliters: {self.milliliters}\n #Usage: {self.usage_type}'
