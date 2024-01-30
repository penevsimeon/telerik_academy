from commands.base_command import BaseCommand
from core.application_data import ApplicationData


class AddCommentCommand(BaseCommand):
    def __init__(self, app_data: ApplicationData):
        super().__init__(app_data)

    def execute(self, params):
        car_id, username, *comment_parts = reversed(params)
        comment_text = ' '.join(reversed(comment_parts))[2:-2]

        super().execute([car_id, username, comment_text])

        user = self._app_data.find_user_by_username(username)
        vehicle = user.get_vehicle(self._try_parse_int(car_id) - 1)

        logged_user = self._app_data.logged_in_user
        logged_user.add_comment(comment_text, vehicle)

        return f'{logged_user.username} added comment successfully!'

    def _requires_login(self) -> bool:
        return True

    def _expected_params_count(self) -> int:
        return 3
