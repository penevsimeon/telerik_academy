from commands.base.base_command import BaseCommand


class TestReportCommand(BaseCommand):
    def execute(self):
        test_id = int(self.params[0])
        test = self.app_data.find_test(test_id)
        if test is None:
            return f'Test #{test_id} not found'
        else:
            return test.generate_report()
