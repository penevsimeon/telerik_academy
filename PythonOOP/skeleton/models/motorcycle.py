from models.comment import Comment


class Motorcycle:
    MAKE_LEN_MIN = 2
    MAKE_LEN_MAX = 15
    MAKE_LEN_ERR = f'Make must be between {MAKE_LEN_MIN} and {MAKE_LEN_MAX} characters long!'

    MODEL_LEN_MIN = 1
    MODEL_LEN_MAX = 15
    MODEL_LEN_ERR = f'Model must be between {MODEL_LEN_MIN} and {MODEL_LEN_MAX} characters long!'

    PRICE_MIN = 0
    PRICE_MAX = 1000000
    PRICE_ERR = f'Price must be between {PRICE_MIN:.1f} and {PRICE_MAX:.2f}!'

    CATEGORY_LEN_MIN = 3
    CATEGORY_LEN_MAX = 10
    CATEGORY_LEN_ERR = f'Category must be between {CATEGORY_LEN_MIN} and {CATEGORY_LEN_MAX} characters long!'

    WHEELS_COUNT = 2

    def __init__(self, make, model, price, category):
        self.make = make
        self.model = model
        self.price = price
        self.category = category
        self._wheels = Motorcycle.WHEELS_COUNT
        self._comments: list[Comment] = []

    @property
    def comments(self):
        return tuple(self._comments)

    @property
    def wheels(self):
        return self._wheels

    @property
    def make(self):
        return self._make

    @make.setter
    def make(self, value):
        if len(value) < int(Motorcycle.MAKE_LEN_MIN) or len(value) > int(Motorcycle.MAKE_LEN_MAX):
            raise ValueError(f'{Motorcycle.MAKE_LEN_ERR}')
        self._make = value

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        if len(value) < int(Motorcycle.MODEL_LEN_MIN) or len(value) > int(Motorcycle.MODEL_LEN_MAX):
            raise ValueError(f'{Motorcycle.MODEL_LEN_ERR}')
        self._model = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < int(Motorcycle.PRICE_MIN) or value > int(Motorcycle.PRICE_MAX):
            raise ValueError(f'{Motorcycle.PRICE_ERR}')
        self._price = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if len(value) < int(Motorcycle.CATEGORY_LEN_MIN) or len(value) > int(Motorcycle.CATEGORY_LEN_MAX):
            raise ValueError(f'{Motorcycle.CATEGORY_LEN_ERR}')
        self._category = value

    def add_comment(self, comment: Comment):
        self._comments.append(comment)

    def get_comment(self, index):
        if index < 0 or index >= len(self._comments):
            raise ValueError('There is no comment on this index.')
        return self._comments[index]

    def remove_comment(self, comment):
        if comment in self._comments:
            self._comments.remove(comment)

    def __str__(self):
        motorcycle_str = f'Motorcycle:\n' \
                         f'Make: {self.make}\n' \
                         f'Model: {self.model}\n' \
                         f'Wheels: {self.wheels}\n' \
                         f'Price: ${self.price:.2f}\n' \
                         f'Category: {self.category}\n'

        if len(self._comments) > 0:
            motorcycle_str += '--COMMENTS--\n'

            for comment in self._comments:
                motorcycle_str += f'{comment}\n'

            motorcycle_str += '--COMMENTS--'

        else:
            motorcycle_str += '--NO COMMENTS--'

        return motorcycle_str
