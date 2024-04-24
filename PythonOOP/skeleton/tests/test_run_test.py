import unittest
from models.constants.test_result import TestResult
from models.test_run import TestRun
from errors.application_error import ApplicationError


class TestRun_Should(unittest.TestCase):
    def test_initializer_whenAllAttributesAreCorrect(self):
        # arrange
        test_result_pass = TestResult.PASS
        runtime_ms = 5
        # act
        test_run = TestRun(test_result_pass, runtime_ms)
        # assert
        self.assertIsInstance(test_result_pass, TestResult)
        self.assertIsInstance(runtime_ms, int)
        self.assertEqual(test_result_pass, test_run.test_result)
        self.assertEqual(runtime_ms, test_run.runtime_ms)

    def test_raiseError_whenRuntimeMsIsNegativeNumber(self):
        # arrange
        test_result_pass = TestResult.PASS
        invalid_runtime = -3
        # act & assert
        with self.assertRaises(ApplicationError):
            TestRun(test_result_pass, invalid_runtime)

    def test_raiseAttributeError_whenTryToChangeValueOnReadOnlyPropertyTestResult(self):
        # arrange
        test_result = TestResult.PASS
        runtime_ms = 5
        # act
        test_run = TestRun(test_result, runtime_ms)
        # assert
        with self.assertRaises(AttributeError):
            test_run.test_result = 'wrong_test_result'

    def test_raiseAttributeError_whenTryToChangeValueOnReadOnlyPropertyRuntimeMs(self):
        # arrange
        test_result = TestResult.PASS
        runtime_ms = 5
        # act
        test_run = TestRun(test_result, runtime_ms)
        # assert
        with self.assertRaises(AttributeError):
            test_run.runtime_ms = 10
