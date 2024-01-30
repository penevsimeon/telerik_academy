import unittest
from unittest.mock import Mock
import tests.test_data as td
from models.user import User


class User_Should(unittest.TestCase):
    def test_init_setProperties(self):
        # Arrange & Act
        user = User(td.VALID_USERNAME, td.VALID_FIRSTNAME,
                    td.VALID_LASTNAME, td.VALID_PASSWORD, td.NORMAL_ROLE)

        # Assert
        self.assertEqual(td.VALID_USERNAME, user.username)
        self.assertEqual(td.VALID_FIRSTNAME, user.firstname)
        self.assertEqual(td.VALID_LASTNAME, user.lastname)
        self.assertEqual(td.VALID_PASSWORD, user.password)
        self.assertEqual(td.NORMAL_ROLE, user.user_role)
        self.assertIsInstance(user.vehicles, tuple)

    def test_init_raiseError_usernameTooShort(self):
        with self.assertRaises(ValueError):
            User('a', td.VALID_FIRSTNAME,
                 td.VALID_LASTNAME, td.VALID_PASSWORD, td.NORMAL_ROLE)

    def test_init_raiseError_usernameTooLong(self):
        with self.assertRaises(ValueError):
            User('a' * 21, td.VALID_FIRSTNAME,
                 td.VALID_LASTNAME, td.VALID_PASSWORD, td.NORMAL_ROLE)

    def test_init_raiseError_usernameInvalidSymbol(self):
        with self.assertRaises(ValueError):
            User('testusern@me', td.VALID_FIRSTNAME,
                 td.VALID_LASTNAME, td.VALID_PASSWORD, td.NORMAL_ROLE)

    def test_init_raiseError_passwordTooShort(self):
        with self.assertRaises(ValueError):
            User(td.VALID_USERNAME, td.VALID_FIRSTNAME,
                 td.VALID_LASTNAME, 'asdf', td.NORMAL_ROLE)

    def test_init_raiseError_passwordTooLong(self):
        with self.assertRaises(ValueError):
            User(td.VALID_USERNAME, td.VALID_FIRSTNAME,
                 td.VALID_LASTNAME, 'a' * 31, td.NORMAL_ROLE)

    def test_init_raiseError_passwordInvalidSymbol(self):
        with self.assertRaises(ValueError):
            User(td.VALID_USERNAME, td.VALID_FIRSTNAME,
                 td.VALID_LASTNAME, 'testpa$$word', td.NORMAL_ROLE)

    def test_init_raiseError_firstnameTooLong(self):
        with self.assertRaises(ValueError):
            User(td.VALID_USERNAME, 'a',
                 td.VALID_LASTNAME, td.VALID_PASSWORD, td.NORMAL_ROLE)

    def test_init_raiseError_firstnameTooLong(self):
        with self.assertRaises(ValueError):
            User(td.VALID_USERNAME, 'a' * 21,
                 td.VALID_LASTNAME, td.VALID_PASSWORD, td.NORMAL_ROLE)

    def test_init_raiseError_lastnameTooLong(self):
        with self.assertRaises(ValueError):
            User(td.VALID_USERNAME, td.VALID_FIRSTNAME,
                 'a', td.VALID_PASSWORD, td.NORMAL_ROLE)

    def test_init_raiseError_lastnameTooLong(self):
        with self.assertRaises(ValueError):
            User(td.VALID_USERNAME, td.VALID_FIRSTNAME,
                 'a' * 21, td.VALID_PASSWORD, td.NORMAL_ROLE)

    def test_isadmin_returnsTrue_whenAdmin(self):
        # Arrange
        user = User(td.VALID_USERNAME, td.VALID_FIRSTNAME,
                    td.VALID_LASTNAME, td.VALID_PASSWORD, td.ADMIN_ROLE)

        # Act & Assert
        self.assertTrue(user.is_admin)

    def test_isadmin_returnsFalse_whenNotAdmin(self):
        # Arrange
        user = User(td.VALID_USERNAME, td.VALID_FIRSTNAME,
                    td.VALID_LASTNAME, td.VALID_PASSWORD, td.VIP_ROLE)

        # Act & Assert
        self.assertFalse(user.is_admin)

    def test_addvehicle_addsVehicleSuccessfully(self):
        # Arrange
        user = User(td.VALID_USERNAME, td.VALID_FIRSTNAME,
                    td.VALID_LASTNAME, td.VALID_PASSWORD, td.VIP_ROLE)
        vehicle = Mock()

        # Act
        user.add_vehicle(vehicle)

        # Assert
        self.assertEqual(tuple([vehicle]), user.vehicles)

    def test_addvehicle_raisesError_whenAdmin(self):
        # Arrange
        user = User(td.VALID_USERNAME, td.VALID_FIRSTNAME,
                    td.VALID_LASTNAME, td.VALID_PASSWORD, td.ADMIN_ROLE)
        vehicle = Mock()

        # Act & Assert
        with self.assertRaises(ValueError):
            user.add_vehicle(vehicle)

    def test_addvehicle_raisesError_whenNotVipAndLimitReached(self):
        # Arrange
        user = User(td.VALID_USERNAME, td.VALID_FIRSTNAME,
                    td.VALID_LASTNAME, td.VALID_PASSWORD, td.NORMAL_ROLE)
        for _ in range(5):
            user.add_vehicle(Mock())

        # Act & Assert
        with self.assertRaises(ValueError):
            user.add_vehicle(Mock())

    def test_addvehicle_addsSuccessfully_whenVipAndLimitReached(self):
        # Arrange
        user = User(td.VALID_USERNAME, td.VALID_FIRSTNAME,
                    td.VALID_LASTNAME, td.VALID_PASSWORD, td.VIP_ROLE)
        for _ in range(5):
            user.add_vehicle(Mock())

        # Act
        user.add_vehicle(Mock())

        # Assert
        self.assertEqual(6, len(user.vehicles))

    def test_getvehicle_returnsSuccessfully_validIndex(self):
        # Arrange
        user = User(td.VALID_USERNAME, td.VALID_FIRSTNAME,
                    td.VALID_LASTNAME, td.VALID_PASSWORD, td.VIP_ROLE)
        vehicle = Mock()
        user.add_vehicle(vehicle)

        # Act
        actual = user.get_vehicle(0)

        # Assert
        self.assertEqual(vehicle, actual)

    def test_getvehicle_raisesError_invalidIndex(self):
        # Arrange
        user = User(td.VALID_USERNAME, td.VALID_FIRSTNAME,
                    td.VALID_LASTNAME, td.VALID_PASSWORD, td.VIP_ROLE)
        vehicle = Mock()
        user.add_vehicle(vehicle)

        # Act & Assert
        with self.assertRaises(ValueError):
            user.get_vehicle(1)

    def test_removevehicle_removesSuccessfully_whenExists(self):
        # Arrange
        user = User(td.VALID_USERNAME, td.VALID_FIRSTNAME,
                    td.VALID_LASTNAME, td.VALID_PASSWORD, td.VIP_ROLE)
        vehicle = Mock()
        user.add_vehicle(vehicle)

        # Act
        user.remove_vehicle(vehicle)

        # Assert
        self.assertEqual(tuple(), user.vehicles)

    def test_removevehicle_doesNothing_whenVehicleDoesNotExist(self):
        # Arrange
        user = User(td.VALID_USERNAME, td.VALID_FIRSTNAME,
                    td.VALID_LASTNAME, td.VALID_PASSWORD, td.VIP_ROLE)
        vehicle = Mock()
        user.add_vehicle(vehicle)

        # Act
        user.remove_vehicle(Mock())

        # Assert
        self.assertEqual(tuple([vehicle]), user.vehicles)

        # def add_comment(self, content: str, vehicle: Vehicle):
        # comment = Comment(content, self.username)
        # vehicle.add_comment(comment)

    def test_addcomment_addsComment(self):
        # Arrange
        user = User(td.VALID_USERNAME, td.VALID_FIRSTNAME,
                    td.VALID_LASTNAME, td.VALID_PASSWORD, td.NORMAL_ROLE)
        fake_vehicle = Mock()

        def fake_vehicle_add(comment):
            fake_vehicle.comments = [comment]
        fake_vehicle.add_comment = fake_vehicle_add
        fake_news = 'fake_news'

        # Act
        user.add_comment(fake_news, fake_vehicle)

        # Assert
        self.assertTrue(fake_news, fake_vehicle.comments[0].content)
        self.assertTrue(td.VALID_USERNAME, fake_vehicle.comments[0].author)

    def test_removecomment_removesComment_whenCorrectAuthor(self):
        # Arrange
        user = User(td.VALID_USERNAME, td.VALID_FIRSTNAME,
                    td.VALID_LASTNAME, td.VALID_PASSWORD, td.NORMAL_ROLE)
        fake_vehicle = Mock()

        def fake_vehicle_remove(comment):
            fake_vehicle.comments.remove(comment)
        fake_vehicle.remove_comment = fake_vehicle_remove
        fake_comment = Mock()
        fake_comment.author = td.VALID_USERNAME
        fake_vehicle.comments = [fake_comment]

        # Act
        user.remove_comment(fake_comment, fake_vehicle)

        # Assert
        self.assertEqual([], fake_vehicle.comments)

    def test_removecomment_raisesError_wrongAuthor(self):
        # Arrange
        user = User(td.VALID_USERNAME, td.VALID_FIRSTNAME,
                    td.VALID_LASTNAME, td.VALID_PASSWORD, td.NORMAL_ROLE)
        fake_vehicle = Mock()

        def fake_vehicle_remove(comment):
            fake_vehicle.comments.remove(comment)
        fake_vehicle.remove_comment = fake_vehicle_remove
        fake_comment = Mock()
        fake_comment.author = 'Another Author'
        fake_vehicle.comments = [fake_comment]

        # Act
        with self.assertRaises(ValueError):
            user.remove_comment(fake_comment, fake_vehicle)

    def test_printvehicles_correctOutput_noVehicles(self):
        # Arrange
        user = User(td.VALID_USERNAME, td.VALID_FIRSTNAME,
                    td.VALID_LASTNAME, td.VALID_PASSWORD, td.NORMAL_ROLE)
        expected = '\n'.join([
            f'--USER {td.VALID_USERNAME}--',
            '--NO VEHICLES--'
        ])

        # Act
        actual = user.print_vehicles()

        # Assert
        self.assertEqual(expected, actual)

    def test_printvehicles_correctOutput_withVehicles(self):
        # Arrange
        user = User(td.VALID_USERNAME, td.VALID_FIRSTNAME,
                    td.VALID_LASTNAME, td.VALID_PASSWORD, td.NORMAL_ROLE)
        expected = '\n'.join([
            f'--USER {td.VALID_USERNAME}--',
            '1. fake_vehicle_str',
            '2. fake_vehicle_str'
        ])
        fake_vehicle = Mock()
        fake_vehicle.__str__ = lambda self: 'fake_vehicle_str'
        user.add_vehicle(fake_vehicle)
        user.add_vehicle(fake_vehicle)

        # Act
        actual = user.print_vehicles()

        # Assert
        self.assertEqual(expected, actual)

    def test_str_correctlyFormattedOutput(self):
        # Arrange
        user = User(td.VALID_USERNAME, td.VALID_FIRSTNAME,
                    td.VALID_LASTNAME, td.VALID_PASSWORD, td.NORMAL_ROLE)
        expected = f'Username: {td.VALID_USERNAME}, FullName: {td.VALID_FIRSTNAME} {td.VALID_LASTNAME}, Role: {td.NORMAL_ROLE}'

        # Act
        stringified = str(user)

        # Assert
        self.assertEqual(expected, stringified)