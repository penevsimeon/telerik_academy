"""
Minimum category name’s length is 2 symbols and maximum is 15 symbols.
products property getter should return an immutable collection (tuple)
Products in category should be displayed in insertion order
When removing product from category, 
if the product is not found you should raise an error.
Category’s to_string() should return text in the following format:
#Category: {category name}
 #{Name} {Brand}
 #Price: ${price}
 #Gender: {genderType}
 ===
 #{Name} {Brand}
 #Price: ${price}
 #Gender: {genderType}
#Category: {category name}
 #No products in this category
"""


def name_len_checker(value: str):
    if len(value) < 2 or len(value) > 15:
        raise ValueError("Name of the category has to be between 2 and 15 symbols")
    else:
        return value


class Category:
    def __init__(self, name: str):
        # raise NotImplementedError()
        self._name = name_len_checker(name)
        self._products = []

    @property
    def name(self):
        # raise NotImplementedError()
        return self._name

    @name.setter
    def name(self, value):
        # raise NotImplementedError()
        new_name = name_len_checker(value)
        self._name = new_name
        return self._name

    @property
    def products(self):
        # raise NotImplementedError()
        return tuple(self._products)

    def add_product(self, product):
        if product in self._products:
            raise ValueError("This product exists!")
        self._products.append(product)

    def remove_product(self, product):
        # raise NotImplementedError()
        if product not in self._products:
            raise ValueError("This product does not exist!")

        self._products.remove(product)

    def to_string(self):
        new_line = "\n ===\n"
        if len(self._products) > 0:
            product_strings = [p.to_string() for p in self._products]
            return f"#Category: {self._name}\n{new_line.join(product_strings)}"
        else:
            return f"#Category: {self._name}\n #No products in this category"
   