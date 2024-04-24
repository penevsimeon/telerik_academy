from commands.base.base_command import BaseCommand
from core.application_data import ApplicationData
from core.models_factory import ModelsFactory


class AddTestCommand(BaseCommand):
    def __init__(self, params: list[str],
                 app_data: ApplicationData,
                 models_factory: ModelsFactory):
        super().__init__(params, app_data)
        self._models_factory = models_factory

    @property
    def models_factory(self):
        return self._models_factory

    def execute(self):
        group_id = int(self.params[0])
        description = self.params[1]

        group = self.app_data.find_group(group_id)
        if group is None:
            return f'Group #{group_id} not found'

        test = self.models_factory.create_test(description)
        group.add_test(test)

        return f'Test #{test.id} added to group #{group.id}'
