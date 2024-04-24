from commands.base.base_command import BaseCommand


class ViewGroupCommand(BaseCommand):
    def execute(self):
        group_id = int(self.params[0])
        group = self.app_data.find_group(group_id)
        if group is None:
            return f'Group #{group_id} not found'
        else:
            return group.view()
