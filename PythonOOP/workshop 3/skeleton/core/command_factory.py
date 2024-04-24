from core.application_data import ApplicationData
from commands.add_test_group import AddTestGroupCommand
from commands.add_test import AddTestCommand
from commands.add_test_run import AddTestRun
from commands.remove_group import RemoveGroupCommand
from commands.test_report import TestReportCommand



class CommandFactory:
    def __init__(self, data: ApplicationData):
        self._app_data = data

    def create(self, input_line):
        cmd, *params = input_line.split()
        if cmd.lower() == 'addtestgroup':
            return AddTestGroupCommand(params, self._app_data)
        if cmd.lower() == 'addtest':
            return AddTestCommand(params, self._app_data)
        if cmd.lower() == 'addtestrun':
            return AddTestRun(params, self._app_data)
        if cmd.lower() == 'removegroup':
            return RemoveGroupCommand(params, self._app_data)
        if cmd.lower() == 'testreport':
            return TestReportCommand(params, self._app_data)