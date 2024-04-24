from errors.application_error import ApplicationError
from models.constants.test_result import TestResult
from core.models_factory import ModelsFactory
import unittest


class ModelsFactory_Should(unittest.TestCase):

    def test_create_group(self):
        models_factory = ModelsFactory()

        group = models_factory.create_group("Group 1")

        self.assertEqual(group.id, 1)
        self.assertEqual(group.name, "Group 1")

        next_group = models_factory.create_group("Group 2")

        self.assertEqual(next_group.id, 2)

    def test_create_test(self):
        models_factory = ModelsFactory()

        test = models_factory.create_test("Test 1")

        self.assertEqual(test.id, 1)
        self.assertEqual(test.description, "Test 1")

        next_test = models_factory.create_test("Test 2")

        self.assertEqual(next_test.id, 2)

    def test_create_test_run_valid_input(self):
        models_factory = ModelsFactory()

        test_run = models_factory.create_test_run("pass", "100")

        self.assertEqual(test_run.test_result, TestResult.PASS)
        self.assertEqual(test_run.runtime_ms, 100)

    def test_create_test_run_invalid_test_result(self):
        models_factory = ModelsFactory()
        with self.assertRaises(ApplicationError):
            models_factory.create_test_run("INVALID", "100")

    def test_create_test_run_invalid_runtime_ms(self):
        models_factory = ModelsFactory()
        with self.assertRaises(ApplicationError):
            models_factory.create_test_run("pass", "invalid")
