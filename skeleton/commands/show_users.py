from commands.base_command import BaseCommand


class ShowUsersCommand(BaseCommand):
    def __init__(self, app_data):
        super().__init__(app_data)

    def execute(self, params):
        super().execute(params)
        if not self._app_data.logged_in_user.is_admin:
            raise ValueError('You are not an admin!')

        return self._app_data.show_users()

    def _expected_params_count(self) -> int:
        return 0

    def _requires_login(self) -> bool:
        return True
