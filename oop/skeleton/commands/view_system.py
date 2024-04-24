from commands.base.base_command import BaseCommand


class ViewSystemCommand(BaseCommand):
    def execute(self):
        if len(self.app_data.groups) == 0:
            return 'No test groups in the system'
        else:
            return '\n'.join(
                [f'Test Reporter System ({len(self.app_data.groups)} test groups)'] +
                [f'  {group}' for group in self.app_data.groups])
