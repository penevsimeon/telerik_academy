from models.test_group import TestGroup
from models.test import Test
from models.test_run import TestRun
from models.constants.test_result import TestResult


class ApplicationData:
    def __init__(self):
        self._test_groups: list[TestGroup] = []
        self._id = 1
        self._test_id = 1
        self._test_run_counter = 0
        self._passed_test_runs = 0
        self._failed_test_runs = 0
        self._total_runtime = 0

    @property
    def groups(self):
        return tuple(self._test_groups)

    def add_test_group(self, name):
        test_group = TestGroup(self._id, name)
        self._test_groups.append(test_group)
        self._id += 1
        return test_group

    def add_test(self, group_id, description):
        for group in self._test_groups:
            if group.id == group_id:
                new_test = Test(self._test_id, description)
                group._tests.append(new_test)
                self._test_id += 1
                return new_test

    def add_test_run(self, test_id, result, runtime):

        for group in self._test_groups:
            for test in group.tests:
                if test.id == test_id:

                    test_run = TestRun(result, runtime)

                    test.add_test_run(test_run)
                    self._test_run_counter += 1
                    if result == TestResult.PASS:
                        self._passed_test_runs += 1
                    elif result == TestResult.FAIL:
                        self._failed_test_runs += 1
                    self._total_runtime += runtime
                    return "TestRun registered"

    def remove_test_group(self, group_id):
        for group in self._test_groups:
            if group.id == group_id:
                self._test_groups.remove(group)
                return "Group removed"

    def get_test_report(self, test_id):
        for group in self._test_groups:
            for test in group.tests:
                if test.id == test_id:
                    return f'#{test.id}. [{test.description}]: {self._test_run_counter} runs' \
                           f'\n# - Passing: {self._passed_test_runs}\n# - Falling: {self._failed_test_runs}' \
                           f'\n# - Total runtime: {self._total_runtime}ms' \
                           f'\n# - Average runtime: {self._total_runtime / (self._passed_test_runs + self._failed_test_runs)}ms'
