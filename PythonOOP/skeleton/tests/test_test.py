from errors.application_error import ApplicationError
from models.constants.test_result import TestResult
from models.test_run import TestRun
from models.test import Test
import unittest


class Test_Should(unittest.TestCase):
    def test_initializer_whenAllDataIsCorrect(self):
        # arrange
        test_id = 1
        test_description = 'test'

        # act
        test = Test(test_id, test_description)
        # assert
        self.assertEqual(test_id, test.id)
        self.assertEqual(test_description, test.description)
        self.assertIsInstance(test.test_runs, tuple)

    def test_raiseError_whenDescriptionIsNone(self):
        # arrange
        test_id = 1
        test_description = None
        # act & assert
        with self.assertRaises(ApplicationError):
            Test(test_id, test_description)

    def test_raiseError_whenDescriptionIsEmptyString(self):
        # arrange
        test_id = 1
        test_description = ''
        # act & assert
        with self.assertRaises(ApplicationError):
            Test(test_id, test_description)

    def test_raiseAttributeError_whenReadOnlyPropertyIdIsTryingToChange(self):
        # arrange
        test_id = 1
        test_description = 'test'
        # act
        test = Test(test_id, test_description)
        # assert
        with self.assertRaises(AttributeError):
            test.id = 2

    def test_raiseAttributeError_whenReadOnlyPropertyDescriptionIsTryingToChange(self):
        # arrange
        test_id = 1
        test_description = 'test'
        # act
        test = Test(test_id, test_description)
        # assert
        with self.assertRaises(AttributeError):
            test.description = 'test2'

    def test_raiseAttributeError_whenReadOnlyPropertyTestRunsIsTryingToChangeValueAndType(self):
        # arrange
        test_id = 1
        test_description = 'test'
        # act
        test = Test(test_id, test_description)
        # assert
        with self.assertRaises(AttributeError):
            test.test_runs = [2]

    def test_passingTestRunsProperty_whenAllDataIsCorrect(self):
        # arrange
        test_result_pass = TestResult.PASS
        test_result_fail = TestResult.FAIL
        test_runs = [TestRun(test_result_pass, 5), TestRun(test_result_fail, 5)]
        test_id = 1
        test_description = 'test'
        # act
        test = Test(test_id, test_description)

        test._test_runs = test_runs
        passing_test_runs = test.passing_test_runs
        # assert
        self.assertEqual(passing_test_runs, test.passing_test_runs)

    def test_passingTestRunsProperty_returnEmptyTupleWhenAllTestResultsAreFailed(self):
        # arrange
        test_result_fail = TestResult.FAIL
        test_runs = [TestRun(test_result_fail, 5), TestRun(test_result_fail, 5)]
        test_id = 1
        test_description = 'test'
        # act
        test = Test(test_id, test_description)

        test._test_runs = test_runs
        # assert
        self.assertEqual(tuple(), test.passing_test_runs)

    def test_passingTestRunProperty_whenIsInstanceOfTupleAndReadOnlyProperty(self):
        # arrange
        test_id = 1
        test_description = 'test'
        # act
        test = Test(test_id, test_description)
        # assert
        self.assertIsInstance(test.passing_test_runs, tuple)

        with self.assertRaises(AttributeError):
            test.passing_test_runs = [1, 2]

    def test_failedTestRunsProperty_whenAllDataIsCorrect(self):
        # arrange
        test_result_pass = TestResult.PASS
        test_result_fail = TestResult.FAIL
        test_runs = [TestRun(test_result_pass, 5), TestRun(test_result_fail, 5)]
        test_id = 1
        test_description = 'test'
        # act
        test = Test(test_id, test_description)

        test._test_runs = test_runs
        failed_test_runs = test.failed_test_runs
        # assert
        self.assertEqual(failed_test_runs, test.failed_test_runs)

    def test_failedTestRunsProperty_returnEmptyTupleWhenAllTestResultsArePass(self):
        # arrange
        test_result_pass = TestResult.PASS
        test_runs = [TestRun(test_result_pass, 5), TestRun(test_result_pass, 5)]
        test_id = 1
        test_description = 'test'
        # act
        test = Test(test_id, test_description)

        test._test_runs = test_runs
        # assert
        self.assertEqual(tuple(), test.failed_test_runs)

    def test_failedTestRunProperty_whenIsInstanceOfTupleAndReadOnlyProperty(self):
        # arrange
        test_id = 1
        test_description = 'test'
        # act
        test = Test(test_id, test_description)
        # assert
        self.assertIsInstance(test.failed_test_runs, tuple)

        with self.assertRaises(AttributeError):
            test.failed_test_runs = [1, 2]

    def test_totalRunTimeProperty_whenAllDataIsCorrect(self):
        # arrange
        test_run_runtime = 5
        test_runs = [TestRun(TestResult.PASS, test_run_runtime), TestRun(TestResult.FAIL, test_run_runtime)]
        test_description = 'test'
        test_id = 1
        # act
        test = Test(test_id, test_description)
        test._test_runs = test_runs
        # assert
        self.assertEqual(10, test.total_runtime)

    def test_raiseError_whenTryToChangetotalRunTimeReadOnlyProperty(self):
        # arrange
        test_run_runtime = 5
        test_runs = [TestRun(TestResult.PASS, test_run_runtime), TestRun(TestResult.FAIL, test_run_runtime)]
        test_description = 'test'
        test_id = 1
        # act
        test = Test(test_id, test_description)
        test._test_runs = test_runs
        # assert
        with self.assertRaises(AttributeError):
            test.total_runtime = 5

    def test_avgRunTimeProperty_whenResultIsZero(self):
        # arrange
        test_description = 'test'
        test_id = 1
        # act
        test = Test(test_id, test_description)
        # assert
        self.assertEqual(0.0, test.avg_runtime)

    def test_avgRunTimeProperty_whenAllDataIsCorrect(self):
        # arrange
        test_runs = [TestRun(TestResult.PASS, 5), TestRun(TestResult.FAIL, 5)]
        test_description = 'test'
        test_id = 1
        # act
        test = Test(test_id, test_description)
        test._test_runs = test_runs
        avg_runtime = test.avg_runtime
        # assert
        self.assertEqual(avg_runtime, test.avg_runtime)

    def test_raiseError_whenTryToChangeAvgRuntimeReadOnlyProperty(self):
        # arrange
        test_description = 'test'
        test_id = 1
        # act
        test = Test(test_id, test_description)
        # assert
        with self.assertRaises(AttributeError):
            test.avg_runtime = 5

    def test_AddTestRunFunctionallity_beforeAppendingNewTestRunAndAfterAppendingNewTestRun(self):
        # arrange
        test_result_pass = TestResult.PASS
        test_run_runtime_ms = 5
        test_run = TestRun(test_result_pass, test_run_runtime_ms)

        test_id = 1
        test_description = 'test'
        test = Test(test_id, test_description)
        # act & assert
        self.assertEqual(0, len(test.test_runs))  # len is 0 before appending a test_run to test_runs

        test.add_test_run(test_run)  # appending test_run to test_runs

        self.assertEqual(1, len(test.test_runs))  # len is 1 after successfully appending a test_run to test_runs

    def test_strMethod_whenReturnCorrectlyFormattedString(self):
        # arrange
        test_id = 1
        test_description = 'test'
        # act
        test = Test(test_id, test_description)
        test_str = f'#{test.id}. [{test.description}]: {len(test.test_runs)} runs'
        # assert
        self.assertEqual(test_str, str(test))

    def test_getReportMethod_whenLengthOfTestRunsIsZero(self):
        # arrange
        test_id = 1
        test_description = 'test'
        test = Test(test_id, test_description)
        test_str = f'#{test.id}. [{test.description}]: {len(test.test_runs)} runs'

        # act & assert
        self.assertEqual(test_str, test.generate_report())

    def test_generateReportMethod_whenLengthOfTestRunsIsMoreThanZero(self):
        # arrange
        test_run_1 = TestRun(TestResult.PASS, 5)
        test_run_2 = TestRun(TestResult.FAIL, 5)
        test_id = 1
        test_description = 'test'

        test = Test(test_id, test_description)

        test.add_test_run(test_run_1)
        test.add_test_run(test_run_2)
        # act
        generate_report_str = '\n'.join([
            f'{test}',
            f'- Passing: {len(test.passing_test_runs)}',
            f'- Failing: {len(test.failed_test_runs)}',
            f'- Total runtime: {test.total_runtime}ms',
            f'- Average runtime: {test.avg_runtime:.1f}ms'
        ])
        # assert
        self.assertEqual(generate_report_str, test.generate_report())
