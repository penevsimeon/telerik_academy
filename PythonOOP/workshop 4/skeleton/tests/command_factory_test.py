from models.test_group import TestGroup
from models.constants.test_result import TestResult
from core.application_data import ApplicationData
from core.models_factory import ModelsFactory
from errors.application_error import ApplicationError
from core.command_factory import CommandFactory
import unittest


class CommandFactory_Should(unittest.TestCase):
    def test_raiseError_whenInvalidCommandName(self):
        data = ApplicationData()
        factory = CommandFactory(data)
        input_line = 'createsomething 1'

        with self.assertRaises(ApplicationError):
            factory.create(input_line)

    def test_addTestCommand_execution(self):
        data = ApplicationData()

        test_group = TestGroup(1, 'test')

        data.add_group(test_group)

        factory = CommandFactory(data)

        input_line = 'addtest 1 Description'

        command = factory.create(input_line)

        result = command.execute()

        self.assertEqual(result, 'Test #1 added to group #1')
        self.assertEqual(len(test_group.tests), 1)
        self.assertEqual(test_group.tests[0].description, 'Description')

    def test_addTestCommand_executionWhenReturnsNone(self):
        data = ApplicationData()

        test_group = TestGroup(1, 'test')

        data.add_group(test_group)

        factory = CommandFactory(data)

        input_line = 'addtest 2 Description'

        command = factory.create(input_line)

        result = command.execute()

        self.assertEqual(result, 'Group #2 not found')

    def test_addTestGroup_execution(self):
        data = ApplicationData()

        models_factory = ModelsFactory()

        test_group = models_factory.create_group('test')

        factory = CommandFactory(data)

        input_line = 'addtestgroup test'

        command = factory.create(input_line)

        result = command.execute()

        self.assertEqual(result, f'Group #{test_group.id} created')

    def test_AddTestRun_execution(self):
        data = ApplicationData()
        models_factory = ModelsFactory()
        command_factory = CommandFactory(data)

        group = models_factory.create_group('test')

        data.add_group(group)

        test = models_factory.create_test('test')

        group.add_test(test)

        input_line = 'addtestrun 1 pass 5'

        command = command_factory.create(input_line)

        result = command.execute()

        self.assertEqual(result, "TestRun registered")

        self.assertEqual(test.test_runs[0].test_result, TestResult.PASS)

        self.assertEqual(test.test_runs[0].runtime_ms, 5)

    def test_removeGroup_execution(self):
        data = ApplicationData()

        models_factory = ModelsFactory()

        test_group_1 = models_factory.create_group('test1')
        test_group_2 = models_factory.create_group('test2')

        data.add_group(test_group_1)
        data.add_group(test_group_2)

        input_line = 'removegroup 1'

        factory = CommandFactory(data)

        command = factory.create(input_line)  # removes group with id 1

        result = command.execute()

        self.assertEqual(result, 'Group #1 removed')
        self.assertEqual(len(data.groups), 1)  # check if len of data.groups is decreased by 1
        self.assertEqual(data.groups[0].id, 2)  # check if existing group is with id 2

    def test_removeGroup_whenNotFound(self):
        data = ApplicationData()

        factory = CommandFactory(data)

        input_line = 'removegroup 1'

        command = factory.create(input_line)

        result = command.execute()

        self.assertEqual(result, 'Group #1 not found')

    def test_generate_test_report(self):
        data = ApplicationData()
        models_factory = ModelsFactory()
        command_factory = CommandFactory(data)

        group = models_factory.create_group('test')
        test = models_factory.create_test('test')
        test_run_1 = models_factory.create_test_run('pass', '100')
        test_run_2 = models_factory.create_test_run('fail', '50')
        group.add_test(test)
        data.add_group(group)

        test.add_test_run(test_run_1)
        test.add_test_run(test_run_2)
        input_line = "testreport 1"
        command = command_factory.create(input_line)
        result = command.execute()

        expected_report = '\n'.join([
            '#1. [test]: 2 runs',
            '- Passing: 1',
            '- Failing: 1',
            '- Total runtime: 150ms',
            '- Average runtime: 75.0ms'
        ])

        self.assertEqual(result, expected_report)

    def test_view_group_success(self):
        data = ApplicationData()
        models_factory = ModelsFactory()
        command_factory = CommandFactory(data)

        group = models_factory.create_group('test')

        test1 = models_factory.create_test('test1')
        test2 = models_factory.create_test('test2')

        group.add_test(test1)
        group.add_test(test2)

        data.add_group(group)

        input_line = "viewgroup 1"

        command = command_factory.create(input_line)

        result = command.execute()

        view_group_str = '\n'.join([
            f'#{group.id}. {group.name} ({len(group.tests)} tests)',
            f'  #{test1.id}. [{test1.description}]: {len(test1.test_runs)} runs',
            f'  #{test2.id}. [{test2.description}]: {len(test2.test_runs)} runs'
        ])

        self.assertEqual(result, view_group_str)

    def test_view_group_not_found(self):
        data = ApplicationData()
        models_factory = ModelsFactory()
        command_factory = CommandFactory(data)

        group = models_factory.create_group('test')

        test1 = models_factory.create_test('test1')
        test2 = models_factory.create_test('test2')

        group.add_test(test1)
        group.add_test(test2)

        data.add_group(group)

        input_line = "viewgroup 9"

        command = command_factory.create(input_line)

        result = command.execute()

        self.assertEqual(result, "Group #9 not found")

    def test_view_system_no_groups(self):
        data = ApplicationData()
        command_factory = CommandFactory(data)

        input_line = "viewsystem"

        command = command_factory.create(input_line)

        result = command.execute()

        self.assertEqual(result, "No test groups in the system")

    def test_view_system_with_groups(self):
        data = ApplicationData()
        models_factory = ModelsFactory()
        command_factory = CommandFactory(data)

        group1 = models_factory.create_group('test1')
        group2 = models_factory.create_group('test2')

        data.add_group(group1)
        data.add_group(group2)

        input_line = "viewsystem"
        command = command_factory.create(input_line)
        result = command.execute()

        expected_result = '\n'.join([
            'Test Reporter System (2 test groups)',
            f'  {str(group1)}',
            f'  {str(group2)}'
        ])
        self.assertEqual(result, expected_result)
