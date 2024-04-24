from core.application_data import ApplicationData
from commands.base.base_command import BaseCommand


class TestReportCommand(BaseCommand):
    def __init__(self, params: list[str], app_data: ApplicationData):
        super().__init__(params, app_data)

    def execute(self):
        test_id = int(self._params[0])
        return self.app_data.get_test_report(test_id)
