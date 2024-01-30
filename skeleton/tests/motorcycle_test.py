import unittest
from unittest.mock import Mock
import tests.test_data as td
from models.motorcycle import Motorcycle


class Motorcycle_Should(unittest.TestCase):
    def test_init_setProperties(self):
        # Arrange & Act
        motorcycle = Motorcycle(td.VALID_MAKE, td.VALID_MODEL,
                      td.VALID_PRICE, td.VALID_CATEGORY)

        # Assert
        self.assertEqual(td.VALID_MAKE, motorcycle.make)
        self.assertEqual(td.VALID_MODEL, motorcycle.model)
        self.assertEqual(td.VALID_PRICE, motorcycle.price)
        self.assertEqual(td.VALID_CATEGORY, motorcycle.category)
        self.assertEqual(2, motorcycle.wheels)
        self.assertIsInstance(motorcycle.comments, tuple)

    def test_init_raiseError_makeTooShort(self):
        with self.assertRaises(ValueError):
            Motorcycle('a', td.VALID_MODEL, td.VALID_PRICE, td.VALID_CATEGORY)

    def test_init_raiseError_makeTooLong(self):
        with self.assertRaises(ValueError):
            Motorcycle('a' * 16, td.VALID_MODEL, td.VALID_PRICE, td.VALID_CATEGORY)

    def test_init_raiseError_modelTooShort(self):
        with self.assertRaises(ValueError):
            Motorcycle(td.VALID_MODEL, '', td.VALID_PRICE, td.VALID_CATEGORY)

    def test_init_raiseError_makeTooLong(self):
        with self.assertRaises(ValueError):
            Motorcycle(td.VALID_MODEL, 'a' * 16, td.VALID_PRICE, td.VALID_CATEGORY)

    def test_init_raiseError_priceTooLow(self):
        with self.assertRaises(ValueError):
            Motorcycle(td.VALID_MODEL, td.VALID_MODEL, -5, td.VALID_CATEGORY)

    def test_init_raiseError_priceTooHigh(self):
        with self.assertRaises(ValueError):
            Motorcycle(td.VALID_MODEL, td.VALID_MODEL, 1000001, td.VALID_CATEGORY)

    def test_init_raiseError_categoryTooShort(self):
        with self.assertRaises(ValueError):
            Motorcycle(td.VALID_MODEL, td.VALID_MODEL, td.VALID_PRICE, 'ab')

    def test_init_raiseError_categoryTooLong(self):
        with self.assertRaises(ValueError):
            Motorcycle(td.VALID_MODEL, td.VALID_MODEL, td.VALID_PRICE, 'too_long_category')

    def test_addcomment_addsComment(self):
        # Arrange
        motorcycle = Motorcycle(td.VALID_MAKE, td.VALID_MODEL,
                      td.VALID_PRICE, td.VALID_CATEGORY)
        comment = Mock()

        # Act
        motorcycle.add_comment(comment)

        # Assert
        self.assertEqual(tuple([comment]), motorcycle.comments)

    def test_getComment_returnsCorrectly(self):
        # Arrange
        motorcycle = Motorcycle(td.VALID_MAKE, td.VALID_MODEL,
                      td.VALID_PRICE, td.VALID_CATEGORY)
        comment = Mock()
        motorcycle.add_comment(comment)

        # Act
        actual = motorcycle.get_comment(0)

        # Assert
        self.assertEqual(comment, actual)

    def test_getComment_raisesError_invalidIndex(self):
        # Arrange
        motorcycle = Motorcycle(td.VALID_MAKE, td.VALID_MODEL,
                      td.VALID_PRICE, td.VALID_CATEGORY)
        comment = Mock()
        motorcycle.add_comment(comment)

        # Act & Assert
        with self.assertRaises(ValueError):
            motorcycle.get_comment(2)

    def test_removecomment_removesCorrectly(self):
        # Arrange
        motorcycle = Motorcycle(td.VALID_MAKE, td.VALID_MODEL,
                      td.VALID_PRICE, td.VALID_CATEGORY)
        comment = Mock()
        motorcycle.add_comment(comment)

        # Act
        motorcycle.remove_comment(comment)

        # Assert
        self.assertEqual(tuple(), motorcycle.comments)

    def test_removecomment_doesNothing_whenCommentDoesNotExist(self):
        # Arrange
        motorcycle = Motorcycle(td.VALID_MAKE, td.VALID_MODEL,
                      td.VALID_PRICE, td.VALID_CATEGORY)
        comment = Mock()
        motorcycle.add_comment(comment)

        # Act
        motorcycle.remove_comment(Mock())

        # Assert
        self.assertEqual(tuple([comment]), motorcycle.comments)

    def test_str_returnsCorrectlyFormatted_whenNoComments(self):
        # Arrange
        expected = '\n'.join([
            'Motorcycle:',
            f'Make: {td.VALID_MAKE}',
            f'Model: {td.VALID_MODEL}',
            f'Wheels: 2',
            f'Price: ${td.VALID_PRICE:.2f}',
            f'Category: {td.VALID_CATEGORY}',
            '--NO COMMENTS--'
        ])
        motorcycle = Motorcycle(td.VALID_MAKE, td.VALID_MODEL,
                      td.VALID_PRICE, td.VALID_CATEGORY)

        # Act
        stringified = str(motorcycle)

        # Assert
        self.assertEqual(expected, stringified)

    def test_str_returnsCorrectlyFormatted_whenHasComments(self):
        # Arrange
        this_is_fake_news = 'fake comment'
        expected = '\n'.join([
            'Motorcycle:',
            f'Make: {td.VALID_MAKE}',
            f'Model: {td.VALID_MODEL}',
            f'Wheels: 2',
            f'Price: ${td.VALID_PRICE:.2f}',
            f'Category: {td.VALID_CATEGORY}',
            '--COMMENTS--',
            f'{this_is_fake_news}',
            '--COMMENTS--'
        ])
        motorcycle = Motorcycle(td.VALID_MAKE, td.VALID_MODEL,
                      td.VALID_PRICE, td.VALID_CATEGORY)
        comment = Mock()
        comment.__str__ = lambda _: this_is_fake_news
        motorcycle.add_comment(comment)

        # Act
        stringified = str(motorcycle)

        # Assert
        self.assertEqual(expected, stringified)