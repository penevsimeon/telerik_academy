from commands.base_command import BaseCommand
from core.application_data import ApplicationData


class LoginCommand(BaseCommand):
    def __init__(self, app_data: ApplicationData):
        super().__init__(app_data)

    def execute(self, params):
        super().execute(params)
        self._throw_if_user_logged_in()

        username, password = params
        user = self._app_data.find_user_by_username(username)
        if user.password != password:
            raise ValueError('Wrong username or password!')
        else:
            self._app_data.login(user)

            return f'User {user.username} successfully logged in!'

    def _requires_login(self) -> bool:
        return False

    def _expected_params_count(self) -> int:
        return 2
