import unittest
from unittest.mock import Mock
import tests.test_data as td
from models.truck import Truck


class Truck_Should(unittest.TestCase):
    def test_init_setProperties(self):
        # Arrange & Act
        truck = Truck(td.VALID_MAKE, td.VALID_MODEL,
                      td.VALID_PRICE, td.VALID_CAPACITY)

        # Assert
        self.assertEqual(td.VALID_MAKE, truck.make)
        self.assertEqual(td.VALID_MODEL, truck.model)
        self.assertEqual(td.VALID_PRICE, truck.price)
        self.assertEqual(td.VALID_CAPACITY, truck.weight_capacity)
        self.assertEqual(8, truck.wheels)
        self.assertIsInstance(truck.comments, tuple)

    def test_init_raiseError_makeTooShort(self):
        with self.assertRaises(ValueError):
            Truck('a', td.VALID_MODEL, td.VALID_PRICE, td.VALID_CAPACITY)

    def test_init_raiseError_makeTooLong(self):
        with self.assertRaises(ValueError):
            Truck('a' * 16, td.VALID_MODEL, td.VALID_PRICE, td.VALID_CAPACITY)

    def test_init_raiseError_modelTooShort(self):
        with self.assertRaises(ValueError):
            Truck(td.VALID_MODEL, '', td.VALID_PRICE, td.VALID_CAPACITY)

    def test_init_raiseError_makeTooLong(self):
        with self.assertRaises(ValueError):
            Truck(td.VALID_MODEL, 'a' * 16, td.VALID_PRICE, td.VALID_CAPACITY)

    def test_init_raiseError_priceTooLow(self):
        with self.assertRaises(ValueError):
            Truck(td.VALID_MODEL, td.VALID_MODEL, -5, td.VALID_CAPACITY)

    def test_init_raiseError_priceTooHigh(self):
        with self.assertRaises(ValueError):
            Truck(td.VALID_MODEL, td.VALID_MODEL, 1000001, td.VALID_CAPACITY)

    def test_init_raiseError_capacityTooLow(self):
        with self.assertRaises(ValueError):
            Truck(td.VALID_MODEL, td.VALID_MODEL, td.VALID_PRICE, 0)

    def test_init_raiseError_capacityTooHigh(self):
        with self.assertRaises(ValueError):
            Truck(td.VALID_MODEL, td.VALID_MODEL, td.VALID_PRICE, 101)

    def test_addcomment_addsComment(self):
        # Arrange
        truck = Truck(td.VALID_MAKE, td.VALID_MODEL,
                      td.VALID_PRICE, td.VALID_CAPACITY)
        comment = Mock()

        # Act
        truck.add_comment(comment)

        # Assert
        self.assertEqual(tuple([comment]), truck.comments)

    def test_getComment_returnsCorrectly(self):
        # Arrange
        truck = Truck(td.VALID_MAKE, td.VALID_MODEL,
                      td.VALID_PRICE, td.VALID_CAPACITY)
        comment = Mock()
        truck.add_comment(comment)

        # Act
        actual = truck.get_comment(0)

        # Assert
        self.assertEqual(comment, actual)

    def test_getComment_raisesError_invalidIndex(self):
        # Arrange
        truck = Truck(td.VALID_MAKE, td.VALID_MODEL,
                      td.VALID_PRICE, td.VALID_CAPACITY)
        comment = Mock()
        truck.add_comment(comment)

        # Act & Assert
        with self.assertRaises(ValueError):
            truck.get_comment(2)

    def test_removecomment_removesCorrectly(self):
        # Arrange
        truck = Truck(td.VALID_MAKE, td.VALID_MODEL,
                      td.VALID_PRICE, td.VALID_CAPACITY)
        comment = Mock()
        truck.add_comment(comment)

        # Act
        truck.remove_comment(comment)

        # Assert
        self.assertEqual(tuple(), truck.comments)

    def test_removecomment_doesNothing_whenCommentDoesNotExist(self):
        # Arrange
        truck = Truck(td.VALID_MAKE, td.VALID_MODEL,
                      td.VALID_PRICE, td.VALID_CAPACITY)
        comment = Mock()
        truck.add_comment(comment)

        # Act
        truck.remove_comment(Mock())

        # Assert
        self.assertEqual(tuple([comment]), truck.comments)

    def test_str_returnsCorrectlyFormatted_whenNoComments(self):
        # Arrange
        expected = '\n'.join([
            'Truck:',
            f'Make: {td.VALID_MAKE}',
            f'Model: {td.VALID_MODEL}',
            f'Wheels: 8',
            f'Price: ${td.VALID_PRICE:.2f}',
            f'Weight Capacity: {td.VALID_CAPACITY}t',
            '--NO COMMENTS--'
        ])
        truck = Truck(td.VALID_MAKE, td.VALID_MODEL,
                      td.VALID_PRICE, td.VALID_CAPACITY)

        # Act
        stringified = str(truck)

        # Assert
        self.assertEqual(expected, stringified)

    def test_str_returnsCorrectlyFormatted_whenHasComments(self):
        # Arrange
        this_is_fake_news = 'fake comment'
        expected = '\n'.join([
            'Truck:',
            f'Make: {td.VALID_MAKE}',
            f'Model: {td.VALID_MODEL}',
            f'Wheels: 8',
            f'Price: ${td.VALID_PRICE:.2f}',
            f'Weight Capacity: {td.VALID_CAPACITY}t',
            '--COMMENTS--',
            f'{this_is_fake_news}',
            '--COMMENTS--'
        ])
        truck = Truck(td.VALID_MAKE, td.VALID_MODEL,
                      td.VALID_PRICE, td.VALID_CAPACITY)
        comment = Mock()
        comment.__str__ = lambda _: this_is_fake_news
        truck.add_comment(comment)

        # Act
        stringified = str(truck)

        # Assert
        self.assertEqual(expected, stringified)