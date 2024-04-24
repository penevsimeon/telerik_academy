from core.application_data import ApplicationData
from models.gender import Gender
from commands.validation_helpers import try_parse_int, validate_params_count, try_parse_float
from models.usage_type import UsageType


class CreateShampooCommand:

    def __init__(self, params, app_data: ApplicationData):
        validate_params_count(params, 6)
        self._params = params
        self._app_data = app_data

    def execute(self):
        shampoo_name = self._params[0]
        shampoo_brand = self._params[1]
        shampoo_price = try_parse_float(self._params[2])

        shampoo_gender = self._params[3]
        if shampoo_gender not in [Gender.MEN, Gender.WOMEN, Gender.UNISEX]:
            raise ValueError('Gender should be Men, Women or Unisex!')

        shampoo_usage_type = self._params[5]
        if shampoo_usage_type not in [UsageType.MEDICAL, UsageType.EVERY_DAY]:
            raise ValueError('Usage type should be Medical or Every_Day')


        shampoo_milliliters = try_parse_int(self._params[4])

        if self._app_data.product_exists(shampoo_name):
            raise ValueError(f'Shampoo with name {shampoo_name} already exists!')

        self._app_data.create_shampoo(shampoo_name, shampoo_brand, shampoo_price, shampoo_gender, shampoo_usage_type,
                                      shampoo_milliliters)

        return f'Shampoo with name {shampoo_name} was created!'
