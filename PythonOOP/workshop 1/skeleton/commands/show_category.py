from core.application_data import ApplicationData
from commands.validation_helpers import validate_params_count

class ShowCategoryCommand:

    def __init__(self, params, app_data: ApplicationData):
        validate_params_count(params, 1)
        self._params = params
        self._app_data = app_data

    def execute(self):
        category_name = self._params[0]
        category = self._app_data.find_category_by_name(category_name)

        return category.to_string()
