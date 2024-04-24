from models.constants.test_result import TestResult
from models.test_run import TestRun


class Test:
    test_id = 1

    def __init__(self, id: int, description: str):
        self._id = id
        self._description = description
        self._test_runs: list[TestRun] = []
        self._test_id = Test.test_id

    @property
    def id(self):
        return self._id

    @property
    def description(self):
        return self._description

    @property
    def test_runs(self):
        return tuple(self._test_runs)

    def add_test_run(self, test_run: TestRun):
        self._test_runs.append(test_run)
