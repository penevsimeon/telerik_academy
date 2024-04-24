from commands.base.base_command import BaseCommand


class RemoveGroupCommand(BaseCommand):
    def execute(self):
        group_id = int(self.params[0])

        if self.app_data.remove_group(group_id):
            return f'Group #{group_id} removed'
        else:
            return f'Group #{group_id} not found'
