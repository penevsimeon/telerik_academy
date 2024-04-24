from core.application_data import ApplicationData
from commands.validation_helpers import validate_params_count


class RemoveFromCategoryCommand:

    def __init__(self, params, app_data: ApplicationData):
        validate_params_count(params, 2)
        self._params = params
        self._app_data = app_data

    def execute(self):
        category_name, product_name = self._params
        category = self._app_data.find_category_by_name(category_name)
        product = self._app_data.find_product_by_name(product_name)

        category.remove_product(product)

        return f'Product {product_name} removed from category {category_name}!'
