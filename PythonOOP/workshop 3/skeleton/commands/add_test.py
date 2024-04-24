from commands.base.base_command import BaseCommand
from core.application_data import ApplicationData


class AddTestCommand(BaseCommand):
    def __init__(self, params: list[str], app_data: ApplicationData):
        super().__init__(params, app_data)

    def execute(self):
        group_id = int(self._params[0])
        description = self._params[1]
        test = self.app_data.add_test(group_id, description)
        return f"Test #{test._test_id} added to group #{group_id}"
