from commands.base_command import BaseCommand
from core.application_data import ApplicationData


class RemoveCommentCommand(BaseCommand):
    def __init__(self, app_data: ApplicationData):
        super().__init__(app_data)

    def execute(self, params):
        super().execute(params)
        vehicle_id = self._try_parse_int(
            params[0], 'Invalid vehicle index. Expected a number.') - 1
        comment_id = self._try_parse_int(
            params[1], 'Invalid comment index. Expected a number.') - 1
        username = params[2]

        user = self._app_data.find_user_by_username(username)
        logged_user = self._app_data.logged_in_user

        vehicle = user.get_vehicle(vehicle_id)
        comment = vehicle.get_comment(comment_id)

        logged_user.remove_comment(comment, vehicle)

        return f'{logged_user.username} removed comment successfully!'

    def _requires_login(self) -> bool:
        return True

    def _expected_params_count(self) -> int:
        return 3
