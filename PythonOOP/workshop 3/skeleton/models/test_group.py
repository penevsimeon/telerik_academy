from models.test import Test


class TestGroup:
    def __init__(self, id: int, name: str):
        self._id = id
        self._name = name
        self._tests: list[Test] = []

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def tests(self):
        return tuple(self._tests)
