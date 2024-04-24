import unittest
from unittest.mock import Mock
import tests.test_data as td
from models.car import Car


class Car_Should(unittest.TestCase):
    def test_init_setProperties(self):
        # Arrange & Act
        car = Car(td.VALID_MAKE, td.VALID_MODEL,
                      td.VALID_PRICE, td.VALID_SEATS)

        # Assert
        self.assertEqual(td.VALID_MAKE, car.make)
        self.assertEqual(td.VALID_MODEL, car.model)
        self.assertEqual(td.VALID_PRICE, car.price)
        self.assertEqual(td.VALID_SEATS, car.seats)
        self.assertEqual(4, car.wheels)
        self.assertIsInstance(car.comments, tuple)

    def test_init_raiseError_makeTooShort(self):
        with self.assertRaises(ValueError):
            Car('a', td.VALID_MODEL, td.VALID_PRICE, td.VALID_SEATS)

    def test_init_raiseError_makeTooLong(self):
        with self.assertRaises(ValueError):
            Car('a' * 16, td.VALID_MODEL, td.VALID_PRICE, td.VALID_SEATS)

    def test_init_raiseError_modelTooShort(self):
        with self.assertRaises(ValueError):
            Car(td.VALID_MODEL, '', td.VALID_PRICE, td.VALID_SEATS)

    def test_init_raiseError_makeTooLong(self):
        with self.assertRaises(ValueError):
            Car(td.VALID_MODEL, 'a' * 16, td.VALID_PRICE, td.VALID_SEATS)

    def test_init_raiseError_priceTooLow(self):
        with self.assertRaises(ValueError):
            Car(td.VALID_MODEL, td.VALID_MODEL, -5, td.VALID_SEATS)

    def test_init_raiseError_priceTooHigh(self):
        with self.assertRaises(ValueError):
            Car(td.VALID_MODEL, td.VALID_MODEL, 1000001, td.VALID_SEATS)

    def test_init_raiseError_seatsTooFew(self):
        with self.assertRaises(ValueError):
            Car(td.VALID_MODEL, td.VALID_MODEL, td.VALID_PRICE, 0)

    def test_init_raiseError_seatsTooMuch(self):
        with self.assertRaises(ValueError):
            Car(td.VALID_MODEL, td.VALID_MODEL, td.VALID_PRICE, 11)

    def test_addcomment_addsComment(self):
        # Arrange
        car = Car(td.VALID_MAKE, td.VALID_MODEL,
                      td.VALID_PRICE, td.VALID_SEATS)
        comment = Mock()

        # Act
        car.add_comment(comment)

        # Assert
        self.assertEqual(tuple([comment]), car.comments)

    def test_getComment_returnsCorrectly(self):
        # Arrange
        car = Car(td.VALID_MAKE, td.VALID_MODEL,
                      td.VALID_PRICE, td.VALID_SEATS)
        comment = Mock()
        car.add_comment(comment)

        # Act
        actual = car.get_comment(0)

        # Assert
        self.assertEqual(comment, actual)

    def test_getComment_raisesError_invalidIndex(self):
        # Arrange
        car = Car(td.VALID_MAKE, td.VALID_MODEL,
                      td.VALID_PRICE, td.VALID_SEATS)
        comment = Mock()
        car.add_comment(comment)

        # Act & Assert
        with self.assertRaises(ValueError):
            car.get_comment(2)

    def test_removecomment_removesCorrectly(self):
        # Arrange
        car = Car(td.VALID_MAKE, td.VALID_MODEL,
                      td.VALID_PRICE, td.VALID_SEATS)
        comment = Mock()
        car.add_comment(comment)

        # Act
        car.remove_comment(comment)

        # Assert
        self.assertEqual(tuple(), car.comments)

    def test_removecomment_doesNothing_whenCommentDoesNotExist(self):
        # Arrange
        car = Car(td.VALID_MAKE, td.VALID_MODEL,
                      td.VALID_PRICE, td.VALID_SEATS)
        comment = Mock()
        car.add_comment(comment)

        # Act
        car.remove_comment(Mock())

        # Assert
        self.assertEqual(tuple([comment]), car.comments)

    def test_str_returnsCorrectlyFormatted_whenNoComments(self):
        # Arrange
        expected = '\n'.join([
            'Car:',
            f'Make: {td.VALID_MAKE}',
            f'Model: {td.VALID_MODEL}',
            f'Wheels: 4',
            f'Price: ${td.VALID_PRICE:.2f}',
            f'Seats: {td.VALID_SEATS}',
            '--NO COMMENTS--'
        ])
        car = Car(td.VALID_MAKE, td.VALID_MODEL,
                      td.VALID_PRICE, td.VALID_SEATS)

        # Act
        stringified = str(car)

        # Assert
        self.assertEqual(expected, stringified)

    def test_str_returnsCorrectlyFormatted_whenHasComments(self):
        # Arrange
        this_is_fake_news = 'fake comment'
        expected = '\n'.join([
            'Car:',
            f'Make: {td.VALID_MAKE}',
            f'Model: {td.VALID_MODEL}',
            f'Wheels: 4',
            f'Price: ${td.VALID_PRICE:.2f}',
            f'Seats: {td.VALID_SEATS}',
            '--COMMENTS--',
            f'{this_is_fake_news}',
            '--COMMENTS--'
        ])
        car = Car(td.VALID_MAKE, td.VALID_MODEL,
                      td.VALID_PRICE, td.VALID_SEATS)
        comment = Mock()
        comment.__str__ = lambda _: this_is_fake_news
        car.add_comment(comment)

        # Act
        stringified = str(car)

        # Assert
        self.assertEqual(expected, stringified)