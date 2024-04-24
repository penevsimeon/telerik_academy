import unittest
from unittest.mock import Mock

from models.category import Category

VALID_NAME = 'Shampoo'


def fake_product():
    product = Mock()
    product.name = 'top shampoo'

    return product


class Category_Should(unittest.TestCase):
    def test_constructor_raisesError_when_nameLengthOutOfBounds(self):
        with self.assertRaises(ValueError):
            _ = Category('x')

    def test_constructor_createsCategory_when_nameIsValid(self):
        category = Category(VALID_NAME)
        self.assertEqual(VALID_NAME, category.name)

    def test_constructor_initializesCorrectProductsType_when_categoryCreated(self):
        category = Category(VALID_NAME)
        self.assertIsInstance(category.products, tuple)

    def test_addProduct_addsProductToList(self):
        # Arrange
        category = Category(VALID_NAME)
        # Act
        category.add_product(fake_product())

        # Assert
        self.assertEqual(1, len(category.products))

    def test_addProduct_raisesError_whenSameProductAddedMoreThanOnce(self):
        # Arrange
        category = Category(VALID_NAME)
        product = fake_product()
        category.add_product(product)
       
        with self.assertRaises(ValueError):
            # Act & Assert
            category.add_product(product)

    def test_removeProduct_removesProductFromList(self):
        # Arrange
        category = Category(VALID_NAME)
        product = fake_product()
        category.add_product(product)

        # Act
        category.remove_product(product)

        # Assert
        self.assertEqual(0, len(category.products))

    def test_removeProduct_raiseError_whenProductDoesNotExist(self):
        with self.assertRaises(ValueError):
            category = Category(VALID_NAME)
            category.remove_product(fake_product())

