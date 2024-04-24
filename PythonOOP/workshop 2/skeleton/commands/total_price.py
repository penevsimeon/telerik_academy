from core.application_data import ApplicationData


class TotalPriceCommand:

    def __init__(self, app_data: ApplicationData):
        self._app_data = app_data

    def execute(self):
        if len(self._app_data.shopping_cart.products) == 0:
            return 'No products in shopping cart!'
        else:
            return f'${self._app_data.shopping_cart.total_price():.2f} total price currently in the shopping cart!'
