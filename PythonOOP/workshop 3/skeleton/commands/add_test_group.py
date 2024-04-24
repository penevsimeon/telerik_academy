from commands.base.base_command import BaseCommand


class AddTestGroupCommand(BaseCommand):
    def __init__(self, params: list[str], app_data):
        super().__init__(params, app_data)

    def execute(self):
        group_name = self._params[0]
        test_group = self.app_data.add_test_group(group_name)
        return f"Group #{test_group.id} created"
