from commands.base.base_command import BaseCommand
from core.application_data import ApplicationData
from core.models_factory import ModelsFactory


class AddTestGroupCommand(BaseCommand):
    def __init__(self, params: list[str],
                 app_data: ApplicationData,
                 models_factory: ModelsFactory):
        super().__init__(params, app_data)
        self._models_factory = models_factory

    @property
    def models_factory(self):
        return self._models_factory

    def execute(self):
        name = self.params[0]
        group = self.models_factory.create_group(name)
        self.app_data.add_group(group)

        return f'Group #{group.id} created'
