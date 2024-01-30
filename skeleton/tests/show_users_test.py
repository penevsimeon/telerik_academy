import unittest
from unittest.mock import Mock

from commands.show_users import ShowUsersCommand


class ShowsUsersCommand_Should(unittest.TestCase):
    def test_execute_returnsCorrectOutput_whenAdmin(self):
        # Arrange
        fake_admin = Mock()
        fake_admin.is_admin = True

        fake_user = Mock()
        fake_user.__str__ = lambda self: 'fake user str'

        fake_app_data = Mock()
        fake_app_data.logged_in_user = fake_admin
        fake_app_data.users = [fake_user, fake_user]

        command = ShowUsersCommand(fake_app_data)
        expected = '\n'.join([
            '--USERS--',
            '1. fake user str',
            '2. fake user str'
        ])

        # Act
        output = command.execute([])

        # Assert
        self.assertEqual(expected, output)

    def test_execute_raisesError_whenNotAdmin(self):
        # Arrange
        fake_admin = Mock()
        fake_admin.is_admin = False
        fake_app_data = Mock()
        fake_app_data.logged_in_user = fake_admin
        command = ShowUsersCommand(fake_app_data)

        # Act & Assert
        with self.assertRaises(ValueError):
            command.execute([])

    def test_execute_raisesError_whenNotLoggedIn(self):
        # Arrange
        fake_app_data = Mock()
        fake_app_data.has_logged_in_user = False
        command = ShowUsersCommand(fake_app_data)

        # Act & Assert
        with self.assertRaises(ValueError):
            command.execute([])
