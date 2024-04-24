import unittest

from core.application_data import ApplicationData
from models.shampoo import Shampoo
from models.shopping_cart import ShoppingCart
import category_test
from models.toothpaste import Toothpaste
import toothpaste_test
import shampoo_test


class ApplicationData_Should(unittest.TestCase):
    def test_properties_returnCorrectTypes(self):
        data = ApplicationData()
        self.assertIsInstance(data.categories, tuple)
        self.assertIsInstance(data.products, tuple)
        self.assertIsInstance(data.shopping_cart, ShoppingCart)

    def test_categoryExists_returnsTrue_whenCategoryExists(self):
        # Arrange
        data = ApplicationData()
        data.create_category(category_test.VALID_NAME)

        # Act && Assert
        self.assertTrue(data.category_exists(category_test.VALID_NAME))

    def test_productExists_returnsTrue_whenProductExists(self):
        # Arrange
        data = ApplicationData()
        data.create_shampoo(shampoo_test.VALID_NAME, shampoo_test.VALID_BRAND, shampoo_test.VALID_PRICE,
                            shampoo_test.VALID_GENDER, shampoo_test.VALID_USAGE_TYPE, shampoo_test.VALID_MILLILITERS)

        # Act && Assert
        self.assertTrue(data.product_exists(shampoo_test.VALID_NAME))

    def test_createCategory_createsSuccessfully(self):
        # Arrange
        data = ApplicationData()

        # Act
        data.create_category(category_test.VALID_NAME)

        # Assert
        self.assertEqual(1, len(data.categories))

    def test_createShampoo_createsSuccessfully(self):
        # Arrange
        data = ApplicationData()

        # Act
        shampoo = data.create_shampoo(shampoo_test.VALID_NAME, shampoo_test.VALID_BRAND, shampoo_test.VALID_PRICE,
                            shampoo_test.VALID_GENDER, shampoo_test.VALID_USAGE_TYPE, shampoo_test.VALID_MILLILITERS)


        # Assert
        self.assertEqual(1, len(data.products))
        self.assertIsInstance(shampoo, Shampoo)

    def test_createToothpaste_createsSuccessfully(self):
        # Arrange
        data = ApplicationData()

        # Act
        toothpaste = data.create_toothpaste(toothpaste_test.VALID_NAME, toothpaste_test.VALID_BRAND, toothpaste_test.VALID_PRICE,
                            toothpaste_test.VALID_GENDER, toothpaste_test.TEST_INGREDIENTS)


        # Assert
        self.assertEqual(1, len(data.products))
        self.assertIsInstance(toothpaste, Toothpaste)

    def test_findCategoryByName_returnsSuccessfully_whenCategoryExists(self):
        # Arrange
        data = ApplicationData()
        data.create_category(category_test.VALID_NAME)

        # Act
        category = data.find_category_by_name(category_test.VALID_NAME)

        # Assert
        self.assertEqual(category_test.VALID_NAME, category.name)

    def test_findCategoryByName_raisesError_whenCategoryDoesNotExist(self):
        with self.assertRaises(ValueError):
            data = ApplicationData()
            data.find_category_by_name(category_test.VALID_NAME)

    def test_findProductByName_returnsSuccessfully_whenProductExists(self):
        # Arrange
        data = ApplicationData()
        data.create_toothpaste(toothpaste_test.VALID_NAME, toothpaste_test.VALID_BRAND, toothpaste_test.VALID_PRICE,
                            toothpaste_test.VALID_GENDER, toothpaste_test.TEST_INGREDIENTS)

        # Act
        product = data.find_product_by_name(toothpaste_test.VALID_NAME)

        # Assert
        self.assertEqual(toothpaste_test.VALID_NAME, product.name)

    def test_findProductByName_raisesError_whenProductDoesNotExist(self):
        with self.assertRaises(ValueError):
            data = ApplicationData()
            data.find_product_by_name(toothpaste_test.VALID_NAME)
