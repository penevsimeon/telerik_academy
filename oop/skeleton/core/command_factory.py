
from commands.add_test_group import AddTestGroupCommand
from commands.add_test_run import AddTestRunCommand
from commands.remove_group import RemoveGroupCommand
from commands.test_report import TestReportCommand
from commands.view_group import ViewGroupCommand
from commands.view_system import ViewSystemCommand
from core.application_data import ApplicationData
from commands.add_test import AddTestCommand
from core.models_factory import ModelsFactory
from errors.application_error import ApplicationError


class CommandFactory:
    def __init__(self, data: ApplicationData):
        self._app_data = data
        self._models_factory = ModelsFactory()

    def create(self, input_line: str):
        cmd, *params = input_line.split()

        if cmd.lower() == "addtest":
            return AddTestCommand(params, self._app_data, self._models_factory)
        if cmd.lower() == "addtestgroup":
            return AddTestGroupCommand(params, self._app_data, self._models_factory)
        if cmd.lower() == "removegroup":
            return RemoveGroupCommand(params, self._app_data)
        if cmd.lower() == "addtestrun":
            return AddTestRunCommand(params, self._app_data, self._models_factory)
        if cmd.lower() == "testreport":
            return TestReportCommand(params, self._app_data)
        if cmd.lower() == "viewgroup":
            return ViewGroupCommand(params, self._app_data)
        if cmd.lower() == "viewsystem":
            return ViewSystemCommand(params, self._app_data)

        raise ApplicationError(f'Invalid command name: {cmd}!')
