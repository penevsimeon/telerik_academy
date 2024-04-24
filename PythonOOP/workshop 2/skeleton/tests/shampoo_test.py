import unittest

from models.gender import Gender
from models.shampoo import Shampoo
from models.usage_type import UsageType

VALID_NAME = 'TestName'
VALID_BRAND = 'TestBrand'
VALID_PRICE = 3.5
VALID_GENDER = Gender.UNISEX
VALID_MILLILITERS = 2
VALID_USAGE_TYPE = UsageType.EVERY_DAY
TEST_INGREDIENTS = ['Test1', 'Test2']

EXPECTED_OUTPUT = f''' #{VALID_NAME} {VALID_BRAND}
 #Price: ${VALID_PRICE:.2f}
 #Gender: {VALID_GENDER}
 #Milliliters: {VALID_MILLILITERS}
 #Usage: {VALID_USAGE_TYPE}'''


class Shampoo_Should(unittest.TestCase):
    def test_constructor_raisesError_when_nameLengthOutOfBounds(self):
        with self.assertRaises(ValueError):
            _ = Shampoo('_', VALID_BRAND, VALID_PRICE, VALID_GENDER, VALID_USAGE_TYPE, VALID_MILLILITERS)

    def test_constructor_raisesError_when_brandLengthOutOfBounds(self):
        with self.assertRaises(ValueError):
            _ = Shampoo(VALID_NAME, '_', VALID_PRICE, VALID_GENDER, VALID_USAGE_TYPE, VALID_MILLILITERS)

    def test_constructor_raiseError_when_priceIsNegative(self):
        with self.assertRaises(ValueError):
            _ = Shampoo(VALID_NAME, VALID_BRAND, -1.5, VALID_GENDER, VALID_USAGE_TYPE, VALID_MILLILITERS)

    def test_constructor_raiseError_when_millilitersIsInvalid(self):
        with self.assertRaises(ValueError):
            _ = Shampoo(VALID_NAME, VALID_BRAND, VALID_PRICE, VALID_GENDER, VALID_USAGE_TYPE, -2)

    def test_constructor_setsProperties_whenArgumentsAreValid(self):
        shampoo = Shampoo(VALID_NAME, VALID_BRAND, VALID_PRICE, VALID_GENDER, VALID_USAGE_TYPE, VALID_MILLILITERS)
        self.assertEqual(VALID_NAME, shampoo.name)
        self.assertEqual(VALID_BRAND, shampoo.brand)
        self.assertEqual(VALID_PRICE, shampoo.price)
        self.assertEqual(VALID_GENDER, shampoo.gender)
        self.assertEqual(VALID_MILLILITERS, shampoo.milliliters)
        self.assertEqual(VALID_USAGE_TYPE, shampoo.usage_type)

    def test_toString_returnsCorrectlyFormattedString(self):
        # Arrange
        shampoo = Shampoo(VALID_NAME, VALID_BRAND, VALID_PRICE, VALID_GENDER, VALID_USAGE_TYPE, VALID_MILLILITERS)

        # Act & Assert
        self.assertEqual(EXPECTED_OUTPUT ,shampoo.to_string())
       
