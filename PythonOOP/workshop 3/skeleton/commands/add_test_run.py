from commands.base.base_command import BaseCommand
from core.application_data import ApplicationData


class AddTestRun(BaseCommand):
    def __init__(self, params: list[str], app_data: ApplicationData):
        super().__init__(params, app_data)

    def execute(self):
        test_id = int(self._params[0])
        result = self._params[1]
        runtime = int(self._params[2])
        test_run = self.app_data.add_test_run(test_id, result, runtime)
        if test_run:
            return "TestRun registered"

