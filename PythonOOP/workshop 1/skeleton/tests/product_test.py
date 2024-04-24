import unittest

from models.gender import Gender
from models.product import Product

VALID_NAME = 'TestName'
VALID_BRAND = 'TestBrand'
VALID_PRICE = 3.5
VALID_GENDER = Gender.UNISEX

EXPECTED_OUTPUT = f''' #{VALID_NAME} {VALID_BRAND}
 #Price: ${VALID_PRICE:.2f}
 #Gender: {VALID_GENDER}'''


class Product_Should(unittest.TestCase):
    def test_constructor_raisesError_when_nameLengthOutOfBounds(self):
        with self.assertRaises(ValueError):
            _ = Product('_', VALID_BRAND, VALID_PRICE, VALID_GENDER)

    def test_constructor_raisesError_when_brandLengthOutOfBounds(self):
        with self.assertRaises(ValueError):
            _ = Product(VALID_NAME, '_', VALID_PRICE, VALID_GENDER)

    def test_constructor_raiseError_when_priceIsNegative(self):
        with self.assertRaises(ValueError):
            _ = Product(VALID_NAME, VALID_BRAND, -1.5, VALID_GENDER)

    def test_constructor_setsProperties_whenArgumentsAreValid(self):
        product = Product(VALID_NAME, VALID_BRAND, VALID_PRICE, VALID_GENDER)
        self.assertEqual(VALID_NAME, product.name)
        self.assertEqual(VALID_BRAND, product.brand)
        self.assertEqual(VALID_PRICE, product.price)
        self.assertEqual(VALID_GENDER, product.gender)

    def test_toString_returnsCorrectlyFormattedString(self):
        # Arrange
        product = Product(VALID_NAME, VALID_BRAND, VALID_PRICE, VALID_GENDER)

        # Act & Assert
        self.assertEqual(EXPECTED_OUTPUT ,product.to_string())
       
