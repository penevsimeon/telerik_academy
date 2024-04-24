from errors.application_error import ApplicationError
from models.test import Test


class TestGroup:
    def __init__(self, id: int, name: str):
        if name is None or name == '':
            raise ApplicationError('Invalid value for TestGroup name')

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

    def add_test(self, test: Test):
        if not any(t.id == test.id for t in self.tests):
            self._tests.append(test)

    def view(self):
        return '\n'.join([f'{self}'] + [f'  {test}' for test in self.tests])

    def __str__(self):
        return f'#{self.id}. {self.name} ({len(self.tests)} tests)'
