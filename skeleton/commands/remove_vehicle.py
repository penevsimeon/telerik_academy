from commands.base_command import BaseCommand
from core.application_data import ApplicationData


class RemoveVehicleCommand(BaseCommand):
    def __init__(self, app_data: ApplicationData):
        super().__init__(app_data)

    def execute(self, params):
        super().execute(params)
        vehicle_id = self._try_parse_int(
            params[0], 'Invalid vehicle index. Expected a number.')
        logged_user = self._app_data.logged_in_user

        vehicle = logged_user.get_vehicle(vehicle_id)
        logged_user.remove_vehicle(vehicle)

        return f'{logged_user.username} removed vehicle successfully!'

    def _requires_login(self) -> bool:
        return True

    def _expected_params_count(self) -> int:
        return 1
