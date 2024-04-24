from models.gender import Gender


def len_checker(start: int, end: int, value: str, property: str):
    if len(value) < start or len(value) > end:
        raise ValueError(
            f"Length of the {property} has to be minimum from {start} symbols and maximum to {end} symbols"
        )
    else:
        return value


def price_checker(value: float):
    if isinstance(value, str):
        raise ValueError("Price must be POSITIVE NUMBER")
    elif value < 0:
        raise ValueError("Price must be POSITIVE NUMBER")
    else:
        return value


def gender_checker(value: str):
    if value == Gender.MEN or value == Gender.WOMEN or value == Gender.UNISEX:
        return value
    else:
        raise ValueError("Gender should be Man, Women or Unisex!")


class Product:
    def __init__(self, name: str, brand, price: float, gender: str):
        self._name = len_checker(3, 10, name, "name")
        self._brand = len_checker(2, 10, brand, "brand")
        self._price = price_checker(price)
        self._gender = gender_checker(gender)
        #

    @property
    def name(self):
        # raise NotImplementedError()
        return self._name

    @name.setter
    def name(self, value):
        new_name = len_checker(3, 10, value, "name")
        if new_name == self._name:
            raise ValueError("That product exists! Try different!")
        self._name = new_name
        return self._name

    @property
    def brand(self):
        # raise NotImplementedError()
        return self._brand

    @brand.setter
    def brand(self, value):
        # raise NotImplementedError()
        new_brand = len_checker(2, 10, value, "brand")
        self._brand = new_brand
        return self._brand

    @property
    def price(self):
        # raise NotImplementedError()
        return self._price

    @price.setter
    def price(self, value):
        # raise NotImplementedError()
        new_price = price_checker(value)
        self._price = new_price
        return self._price

    @property
    def gender(self):
        # raise NotImplementedError()
        return self._gender

    def to_string(self):
        # raise NotImplementedError()
        string = f" #{self._name} {self._brand}\n #Price: ${self._price:.2f}\n #Gender: {self._gender}"
        return string
