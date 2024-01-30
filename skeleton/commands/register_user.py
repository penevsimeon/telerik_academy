from commands.base_command import BaseCommand
from core.application_data import ApplicationData
from models.constants.user_role import UserRole


class RegisterUserCommand(BaseCommand):
    def __init__(self, app_data: ApplicationData):
        super().__init__(app_data)

    def execute(self, params):
        super().execute(params)
        self._throw_if_user_logged_in()

        username, firstname, lastname, password, *rest = params

        if rest == []:
            user_role = UserRole.NORMAL
        else:
            user_role = UserRole.from_string(rest[0])

        user = self._app_data.create_user(
            username, firstname, lastname, password, user_role)
        self._app_data.login(user)

        return f'User {user.username} registered successfully!'

    def _requires_login(self) -> bool:
        return False

    def _expected_params_count(self) -> int:
        return 4
