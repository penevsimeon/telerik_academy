from errors.application_error import ApplicationError
from models.constants.test_result import TestResult
from models.test import Test
from models.test_group import TestGroup
from models.test_run import TestRun


class ModelsFactory:
    def __init__(self):
        self._test_group_id = 1
        self._test_id = 1

    def create_group(self, name: str):
        group_id = self._test_group_id
        self._test_group_id += 1

        return TestGroup(group_id, name)

    def create_test(self, description: str):
        test_id = self._test_id
        self._test_id += 1

        return Test(test_id, description)

    def create_test_run(self, test_result_raw: str, runtime_ms_raw: str):
        try:
            test_result = TestResult(test_result_raw)
        except ValueError:
            raise ApplicationError(
                'Invalid value for TestResult: {test_result_raw}')

        try:
            runtime_ms = int(runtime_ms_raw)
        except ValueError:
            raise ApplicationError(
                '{runtime_ms_raw} is not a valid integer')

        return TestRun(test_result, runtime_ms)
