from errors.application_error import ApplicationError
from models.test import Test
from models.test_group import TestGroup
import unittest

TEST_GROUP_ID = 1
TEST_GROUP_NAME = 'test'


class TestGroup_Should(unittest.TestCase):
    def test_initializer_whenAllAttributesAreCorrect(self):
        # arrange & act
        test_group = TestGroup(TEST_GROUP_ID, TEST_GROUP_NAME)
        # assert
        self.assertEqual(TEST_GROUP_ID, test_group.id)
        self.assertEqual(TEST_GROUP_NAME, test_group.name)

    def test_raiseError_whenAttributeNameIsNone(self):
        # arrange & act & assert
        with self.assertRaises(ApplicationError):
            TestGroup(TEST_GROUP_ID, None)

    def test_raiseError_whenAttributeNameIsEmptyString(self):
        # arrange & act & assert
        with self.assertRaises(ApplicationError):
            TestGroup(TEST_GROUP_ID, '')

    def test_raiseError_whenTryingToChangeReadOnlyPropertyId(self):
        # arrange & act & assert
        with self.assertRaises(AttributeError):
            test_group = TestGroup(TEST_GROUP_ID, TEST_GROUP_NAME)
            test_group.id = 2

    def test_raiseError_whenTryingToChangeReadOnlyPropertyName(self):
        # arrange & act & assert
        with self.assertRaises(AttributeError):
            test_group = TestGroup(TEST_GROUP_ID, TEST_GROUP_NAME)
            test_group.name = 'test'

    def test_raiseError_whenTryingToChangeReadOnlyPropertyTests(self):
        # arrange & act & assert
        with self.assertRaises(AttributeError):
            test_group = TestGroup(TEST_GROUP_ID, TEST_GROUP_NAME)
            test_group.tests = ['test']

    def test_tupleTests_whenIsCorrectInstanceOfTuple(self):
        # arrange & act
        test_group = TestGroup(TEST_GROUP_ID, TEST_GROUP_NAME)
        # assert
        self.assertIsInstance(test_group.tests, tuple)

    def test_tupleTests_whenIsEmptyTuple(self):
        # arrange & act
        test_group = TestGroup(TEST_GROUP_ID, TEST_GROUP_NAME)
        tests = test_group.tests
        # assert
        self.assertEqual((), tests)

    def test_addTestFunctionality_whenAllDataIsCorrect(self):
        # arrange
        test = Test(1, 'test')
        test_group = TestGroup(TEST_GROUP_ID, TEST_GROUP_NAME)
        # act & assert
        self.assertEqual(0, len(test_group.tests))  # len of tests collection in test_group is 0 before adding a test

        test_group.add_test(test)  # adding a test to tests collection

        self.assertEqual(1, len(test_group.tests))  # len of tests collection in test_group is 1 after adding a test

    def test_addTestFunctionality_whenTryToPassTestThatAlreadyExist(self):
        # arrange
        test = Test(1, 'test')
        test_group = TestGroup(TEST_GROUP_ID, TEST_GROUP_NAME)
        # act & assert
        self.assertEqual(0, len(test_group.tests))  # len of tests collection in test_group is 0 before adding a test

        test_group.add_test(test)  # adding a test to tests collection

        self.assertEqual(1, len(test_group.tests))  # len of tests collection in test_group is 1 after adding a test

        test_group.add_test(test)  # try to add test that already exist

        self.assertEqual(1, len(test_group.tests))  # len is not changed because the test already exist

    def test_strMethod_whenStringIsCorrectlyFormatted(self):
        # arrange & act
        test = Test(1, 'test')

        test_group = TestGroup(TEST_GROUP_ID, TEST_GROUP_NAME)

        test_group.add_test(test)

        test_group_str = f'#{test_group.id}. {test_group.name} ({len(test_group.tests)} tests)'

        # assert
        self.assertEqual(test_group_str, str(test_group))

    def test_viewMethod_whenAllDataIsCorrect(self):
        # arrange & act
        test = Test(1, 'test')

        test_group = TestGroup(TEST_GROUP_ID, TEST_GROUP_NAME)

        test_group.add_test(test)

        test_group_view = '\n'.join([f'{test_group}'] + [f'  {test}' for test in test_group.tests])

        # assert
        self.assertEqual(test_group_view, test_group.view())
