from models.test_group import TestGroup
from models.test import Test
from core.application_data import ApplicationData
import unittest


class ApplicationData_Should(unittest.TestCase):

    def test_propertyGroups_whenReturnCorrectType(self):
        # arrange & act & assert
        data = ApplicationData()
        self.assertIsInstance(data.groups, tuple)

    def test_addGroupMethod_whenAppendTestGroupCorrectly(self):
        # arrange
        data = ApplicationData()

        test_group = TestGroup(1, 'test')

        test = Test(1, 'test')

        test_group.add_test(test)

        # act & assert
        self.assertEqual(True, data.add_group(test_group))
        self.assertEqual(1, len(data.groups))

    def test_addGroupMethod_whenTestGroupAlreadyExist(self):
        # arrange
        data = ApplicationData()

        test_group = TestGroup(1, 'test')

        # act & assert
        data.add_group(test_group)
        self.assertEqual(False, data.add_group(test_group))
        self.assertEqual(1, len(data.groups))

    def test_removeGroupMethod_whenRemoveGroupCorrectly(self):
        data = ApplicationData()

        test_group_1 = TestGroup(1, 'test')
        test_group_2 = TestGroup(2, 'test2')

        data.add_group(test_group_1)  # adding a first test group to data.groups
        data.add_group(test_group_2)  # adding a second test group to data.groups

        self.assertEqual(2, len(data.groups))  # check if the len of data.groups is 2 after adding 2 test groups in it

        result = data.remove_group(test_group_1.id)  # removes test group with id 1 from data.groups

        self.assertEqual(True, result)  # checks if remove.group method returns correctly True
        self.assertEqual(1, len(data.groups))  # checks if the len of data.groups is 1 after removing 1 test group
        self.assertEqual(data.groups[0].id, 2)  # additional check that the remaining group is exactly the one we expect

    def test_removeGroupMethod_whenGroupIsNotExist(self):
        data = ApplicationData()

        test_group_1 = TestGroup(1, 'test')
        test_group_2 = TestGroup(2, 'test2')

        data.add_group(test_group_1)  # adding a first test group to data.groups
        data.add_group(test_group_2)  # adding a second test group to data.groups

        self.assertEqual(2, len(data.groups))  # check if the len of data.groups is 2 after adding 2 test groups in it

        result = data.remove_group(3)  # trying to remove not existing test group, it returns False

        self.assertEqual(False, result)  # checks if remove.group method returns correctly False
        self.assertEqual(2, len(data.groups))  # len of data.groups is 2 after trying to remove not existing group

    def test_findGroupMethod_whenWantedGroupIsFound(self):
        # arrange
        data = ApplicationData()

        test_group_1 = TestGroup(1, 'test')
        test_group_2 = TestGroup(2, 'test2')

        data.add_group(test_group_1)  # adding a first test group to data.groups
        data.add_group(test_group_2)  # adding a second test group to data.groups

        # act
        result = data.find_group(test_group_1.id)  # trying to find existing test group in data.groups

        # assert
        self.assertEqual(test_group_1, result)

    def test_findGroupMethod_whenWantedGroupDoesNotExist(self):
        # arrange
        data = ApplicationData()

        test_group_1 = TestGroup(1, 'test')
        test_group_2 = TestGroup(2, 'test2')

        data.add_group(test_group_1)  # adding a first test group to data.groups
        data.add_group(test_group_2)  # adding a second test group to data.groups

        # act
        result = data.find_group(3)  # try to find not existing test group in data.groups, it returns None

        # assert
        self.assertEqual(None, result)  # checks find.group method returns correctly None

    def test_findTestMethod_whenWantedTestExistsInTestGroup(self):
        # arrange
        data = ApplicationData()

        test_group_1 = TestGroup(1, 'test')
        test_group_2 = TestGroup(2, 'test2')

        test_1 = Test(1, 'test')
        test_2 = Test(2, 'test')

        test_group_1.add_test(test_1)  # adding a test to test group with id 1
        test_group_2.add_test(test_2)  # adding a test to test group with id 2

        data.add_group(test_group_1)  # adding a first test group to data.groups with id 1
        data.add_group(test_group_2)  # adding a second test group to data.groups with id 2

        # act
        result = data.find_test(test_1.id)

        # assert
        self.assertEqual(test_1, result)

    def test_findTestMethod_whenWantedTestDoesNotExistInTestGroupAndReturnsNone(self):
        # arrange
        data = ApplicationData()

        test_group_1 = TestGroup(1, 'test')
        test_group_2 = TestGroup(2, 'test2')

        test_1 = Test(1, 'test')
        test_2 = Test(2, 'test')

        test_group_1.add_test(test_1)  # adding a test to test group with id 1
        test_group_2.add_test(test_2)  # adding a test to test group with id 2

        data.add_group(test_group_1)  # adding a first test group to data.groups with id 1
        data.add_group(test_group_2)  # adding a second test group to data.groups with id 2

        # act
        result = data.find_test(3)  # trying to find a test that does not exist in concrete test group in data.groups

        # assert
        self.assertEqual(None, result)  # it returns None when test is not found
