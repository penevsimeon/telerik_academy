import unittest

from core.application_data import ApplicationData
from models.shopping_cart import ShoppingCart
import category_test
import product_test


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

    def test_categoryExists_returnsFalse_whenCategoryDoesNotExist(self):
        # Arrange
        data = ApplicationData()

        # Act && Assert
        self.assertFalse(data.category_exists(category_test.VALID_NAME))

    def test_productExists_returnsTrue_whenProductExists(self):
        # Arrange
        data = ApplicationData()
        data.create_product(
            product_test.VALID_NAME,
            product_test.VALID_BRAND,
            product_test.VALID_PRICE,
            product_test.VALID_GENDER,
        )

        # Act && Assert
        self.assertTrue(data.product_exists(product_test.VALID_NAME))

    def test_productExists_returnsFalse_whenProductDoesNotExist(self):
        # Arrange
        data = ApplicationData()

        # Act && Assert
        self.assertFalse(data.product_exists(product_test.VALID_NAME))

    def test_createCategory_createsSuccessfully(self):
        # Arrange
        data = ApplicationData()

        # Act
        data.create_category(category_test.VALID_NAME)

        # Assert
        self.assertEqual(1, len(data.categories))

    def test_createProduct_createsSuccessfully(self):
        # Arrange
        data = ApplicationData()

        # Act
        data.create_product(
            product_test.VALID_NAME,
            product_test.VALID_BRAND,
            product_test.VALID_PRICE,
            product_test.VALID_GENDER,
        )

        # Assert
        self.assertEqual(1, len(data.products))

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
        data.create_product(
            product_test.VALID_NAME,
            product_test.VALID_BRAND,
            product_test.VALID_PRICE,
            product_test.VALID_GENDER,
        )

        # Act
        product = data.find_product_by_name(product_test.VALID_NAME)

        # Assert
        self.assertEqual(product_test.VALID_NAME, product.name)

    def test_findProductByName_raisesError_whenProductDoesNotExist(self):
        with self.assertRaises(ValueError):
            data = ApplicationData()
            data.find_product_by_name(product_test.VALID_NAME)
