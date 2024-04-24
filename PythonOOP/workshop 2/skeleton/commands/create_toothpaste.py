from core.application_data import ApplicationData
from models.gender import Gender
from commands.validation_helpers import validate_params_count, try_parse_float


class CreateToothpasteCommand:

    def __init__(self, params, app_data: ApplicationData):
        validate_params_count(params, 5)
        self._params = params
        self._app_data = app_data

    def execute(self):
        toothpaste_name = self._params[0]
        toothpaste_brand = self._params[1]
        toothpaste_price = try_parse_float(self._params[2])

        toothpaste_gender = self._params[3]
        if toothpaste_gender not in [Gender.MEN, Gender.WOMEN, Gender.UNISEX]:
            raise ValueError('Gender should be Men, Women, Unisex')

        toothpaste_ingredients = self._params[4].split(',')

        if self._app_data.product_exists(toothpaste_name):
            raise ValueError(f'Toothpaste with name {toothpaste_name} already exists!')

        self._app_data.create_toothpaste(toothpaste_name, toothpaste_brand, toothpaste_price, toothpaste_gender,
                                         toothpaste_ingredients)

        return f'Toothpaste with name {toothpaste_name} was created!'
