from commands.base.base_command import BaseCommand
from core.application_data import ApplicationData
from core.models_factory import ModelsFactory


class AddTestRunCommand(BaseCommand):
    def __init__(self,
                 params: list[str],
                 app_data: ApplicationData,
                 models_factory: ModelsFactory):
        super().__init__(params, app_data)
        self._models_factory = models_factory

    @property
    def models_factory(self):
        return self._models_factory

    def execute(self):
        test_id = int(self.params[0])
        test = self.app_data.find_test(test_id)

        if test is None:
            return f'Test #{test_id} not found'

        test_run = self.models_factory \
            .create_test_run(self.params[1], self.params[2])
        test.add_test_run(test_run)

        return 'TestRun registered'
