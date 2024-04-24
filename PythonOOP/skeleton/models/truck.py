from models.comment import Comment


class Truck:
    MAKE_LEN_MIN = 2
    MAKE_LEN_MAX = 15
    MAKE_LEN_ERR = f'Make must be between {MAKE_LEN_MIN} and {MAKE_LEN_MAX} characters long!'

    MODEL_LEN_MIN = 1
    MODEL_LEN_MAX = 15
    MODEL_LEN_ERR = f'Model must be between {MODEL_LEN_MIN} and {MODEL_LEN_MAX} characters long!'

    PRICE_MIN = 0
    PRICE_MAX = 1000000
    PRICE_ERR = f'Price must be between {PRICE_MIN:.1f} and {PRICE_MAX:.2f}!'

    WEIGHT_CAP_MIN = 1
    WEIGHT_CAP_MAX = 100
    WEIGHT_CAP_ERR = f'Weight capacity must be between {WEIGHT_CAP_MIN} and {WEIGHT_CAP_MAX}!'

    WHEELS_COUNT = 8

    def __init__(self, make, model, price, weight_capacity):
        self.make = make
        self.model = model
        self.price = price
        self.weight_capacity = weight_capacity
        self._wheels = Truck.WHEELS_COUNT
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
        if len(value) < int(Truck.MAKE_LEN_MIN) or len(value) > int(Truck.MAKE_LEN_MAX):
            raise ValueError(f'{Truck.MAKE_LEN_ERR}')
        self._make = value

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        if len(value) < int(Truck.MODEL_LEN_MIN) or len(value) > int(Truck.MODEL_LEN_MAX):
            raise ValueError(f'{Truck.MODEL_LEN_ERR}')
        self._model = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < int(Truck.PRICE_MIN) or value > int(Truck.PRICE_MAX):
            raise ValueError(f'{Truck.PRICE_ERR}')
        self._price = value

    @property
    def weight_capacity(self):
        return self._weight_capacity

    @weight_capacity.setter
    def weight_capacity(self, value):
        if value < int(Truck.WEIGHT_CAP_MIN) or value > int(Truck.WEIGHT_CAP_MAX):
            raise ValueError(f'{Truck.WEIGHT_CAP_ERR}')
        self._weight_capacity = value

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
        truck_str = 'Truck:\n' \
                    f'Make: {self.make}\n' \
                    f'Model: {self.model}\n' \
                    f'Wheels: {self.wheels}\n' \
                    f'Price: ${self.price:.2f}\n' \
                    f'Weight Capacity: {self.weight_capacity}t\n'

        if len(self._comments) > 0:
            truck_str += '--COMMENTS--\n'

            for comment in self._comments:
                truck_str += f'{comment}\n'

            truck_str += '--COMMENTS--'

        else:
            truck_str += '--NO COMMENTS--'

        return truck_str
