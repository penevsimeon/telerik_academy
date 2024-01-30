from models.comment import Comment


class Car:
    MAKE_LEN_MIN = 2
    MAKE_LEN_MAX = 15
    MAKE_LEN_ERR = f'Make must be between {MAKE_LEN_MIN} and {MAKE_LEN_MAX} characters long!'

    MODEL_LEN_MIN = 1
    MODEL_LEN_MAX = 15
    MODEL_LEN_ERR = f'Model must be between {MODEL_LEN_MIN} and {MODEL_LEN_MAX} characters long!'

    PRICE_MIN = 0
    PRICE_MAX = 1000000
    PRICE_ERR = f'Price must be between {PRICE_MIN:.1f} and {PRICE_MAX:.2f}!'

    CAR_SEATS_MIN = 1
    CAR_SEATS_MAX = 10
    CAR_SEATS_ERR = f'Seats must be between {CAR_SEATS_MIN} and {CAR_SEATS_MAX}!'

    WHEELS_COUNT = 4

    def __init__(self, make, model, price, seats):
        self.make = make
        self.model = model
        self.price = price
        self.seats = seats
        self._wheels = 4
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
        if len(value) < int(Car.MAKE_LEN_MIN) or len(value) > int(Car.MAKE_LEN_MAX):
            raise ValueError(f'{Car.MAKE_LEN_ERR}')
        self._make = value

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, value):
        if len(value) < int(Car.MODEL_LEN_MIN) or len(value) > int(Car.MODEL_LEN_MAX):
            raise ValueError(f'{Car.MODEL_LEN_ERR}')
        self._model = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < Car.PRICE_MIN or value > Car.PRICE_MAX:
            raise ValueError(f'{Car.PRICE_ERR}')
        self._price = value

    @property
    def seats(self):
        return self._seats

    @seats.setter
    def seats(self, value):
        if value < Car.CAR_SEATS_MIN or value > Car.CAR_SEATS_MAX:
            raise ValueError(f'{Car.CAR_SEATS_ERR}')
        self._seats = value

    def add_comment(self, comment: Comment):
        self._comments.append(comment)

    def get_comment(self, index):
        if index < 0 or index >= len(self._comments):
            raise ValueError('There is no comment on this index.')
        return self._comments[index]

    def remove_comment(self, comment: Comment):
        if comment in self._comments:
            self._comments.remove(comment)

    def __str__(self):
        car_str = f'Car:\n' \
                  f'Make: {self.make}\n' \
                  f'Model: {self.model}\n' \
                  f'Wheels: {self.wheels}\n' \
                  f'Price: ${self.price:.2f}\n' \
                  f'Seats: {self.seats}\n'
        if len(self._comments) > 0:
            car_str += '--COMMENTS--\n'
            for comment in self._comments:
                car_str += f'{comment}\n'
            car_str += '--COMMENTS--'
        else:
            car_str += '--NO COMMENTS--'
        return car_str
