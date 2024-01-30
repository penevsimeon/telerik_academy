from commands.base_command import BaseCommand
from core.application_data import ApplicationData


class ShowVehiclesCommand(BaseCommand):
    def __init__(self, app_data: ApplicationData):
        super().__init__(app_data)

    def execute(self, params):
        super().execute(params)
        user = self._app_data.find_user_by_username(params[0])

        return user.print_vehicles()

    def _requires_login(self) -> bool:
        return True

    def _expected_params_count(self) -> int:
        return 1
