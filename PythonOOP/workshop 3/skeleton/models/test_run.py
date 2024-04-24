from models.constants.test_result import TestResult


class TestRun:
    def __init__(self, test_result: str, runtime_ms: int):
        if test_result not in [TestResult.PASS, TestResult.FAIL]:
            raise ValueError('Invalid test result value')

        self._test_result = test_result
        self._runtime_ms = runtime_ms

    @property
    def test_result(self):
        return self._test_result

    @property
    def runtime_ms(self):
        return self._runtime_ms
