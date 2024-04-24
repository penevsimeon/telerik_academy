from core.application_data import ApplicationData
from commands.validation_helpers import validate_params_count


class RemoveFromShoppingCartCommand:

    def __init__(self, params, app_data: ApplicationData):
        validate_params_count(params,1)
        self._params = params
        self._app_data = app_data

    def execute(self):
        product_name = self._params[0]
        product = self._app_data.find_product_by_name(product_name)
        self._app_data.shopping_cart.remove_product(product)

        return f'Product {product_name} was removed from the shopping cart!'
