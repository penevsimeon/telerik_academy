from core.application_data import ApplicationData
from commands.validation_helpers import validate_params_count


class CreateCategoryCommand:

    def __init__(self, params, app_data: ApplicationData):
        validate_params_count(params, 1)
        self._params = params
        self._app_data = app_data

    def execute(self):
        category_name = self._params[0]
        if self._app_data.category_exists(category_name):
            raise ValueError(f'Category with name {category_name} already exists!')

        self._app_data.create_category(category_name)

        return f'Category with name {category_name} was created!'
