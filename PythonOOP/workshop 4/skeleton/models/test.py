from errors.application_error import ApplicationError
from models.constants.test_result import TestResult
from models.test_run import TestRun


class Test:
    def __init__(self, id: int, description: str):
        if description is None or description == '':
            raise ApplicationError('Invalid value for Test description')

        self._id = id
        self._description = description
        self._test_runs: list[TestRun] = []

    @property
    def id(self):
        return self._id

    @property
    def description(self):
        return self._description

    @property
    def test_runs(self):
        return tuple(self._test_runs)

    @property
    def passing_test_runs(self):
        return tuple(t for t in self.test_runs if t.test_result == TestResult.PASS)

    @property
    def failed_test_runs(self):
        return tuple(t for t in self.test_runs if t.test_result == TestResult.FAIL)

    @property
    def total_runtime(self):
        return sum(t.runtime_ms for t in self.test_runs)

    @property
    def avg_runtime(self):
        if len(self.test_runs) == 0:
            return 0.0

        return self.total_runtime / len(self.test_runs)

    def add_test_run(self, test_run: TestRun):
        self._test_runs.append(test_run)

    def generate_report(self):
        if len(self.test_runs) == 0:
            return f'{self}'

        return '\n'.join([
            f'{self}',
            f'- Passing: {len(self.passing_test_runs)}',
            f'- Failing: {len(self.failed_test_runs)}',
            f'- Total runtime: {self.total_runtime}ms',
            f'- Average runtime: {self.avg_runtime:.1f}ms'
        ])

    def __str__(self):
        return f'#{self.id}. [{self.description}]: {len(self.test_runs)} runs'
