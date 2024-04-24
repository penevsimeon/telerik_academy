from errors.application_error import ApplicationError
from models.constants.test_result import TestResult


class TestRun:
    def __init__(self, test_result: TestResult, runtime_ms: int):
        if runtime_ms <= 0:
            raise ApplicationError('Invalid value for runtime_ms')

        self._test_result = test_result
        self._runtime_ms = runtime_ms

    @property
    def test_result(self):
        return self._test_result

    @property
    def runtime_ms(self):
        return self._runtime_ms


