import unittest

from models.gender import Gender
from models.toothpaste import Toothpaste

VALID_NAME = 'TestName'
VALID_BRAND = 'TestBrand'
VALID_PRICE = 3.5
VALID_GENDER = Gender.UNISEX
TEST_INGREDIENTS = ['Test1', 'Test2']

EXPECTED_OUTPUT = f''' #{VALID_NAME} {VALID_BRAND}
 #Price: ${VALID_PRICE:.2f}
 #Gender: {VALID_GENDER}
 #Ingredients: [{", ".join(TEST_INGREDIENTS)}]'''


class Toothpaste_Should(unittest.TestCase):
    def test_constructor_raisesError_when_nameLengthOutOfBounds(self):
        with self.assertRaises(ValueError):
            _ = Toothpaste('_', VALID_BRAND, VALID_PRICE, VALID_GENDER, [])

    def test_constructor_raisesError_when_brandLengthOutOfBounds(self):
        with self.assertRaises(ValueError):
            _ = Toothpaste(VALID_NAME, '_', VALID_PRICE, VALID_GENDER, [])

    def test_constructor_raiseError_when_priceIsNegative(self):
        with self.assertRaises(ValueError):
            _ = Toothpaste(VALID_NAME, VALID_BRAND, -1.5, VALID_GENDER, [])

    def test_constructor_setsProperties_whenArgumentsAreValid(self):
        toothpaste = Toothpaste(VALID_NAME, VALID_BRAND, VALID_PRICE, VALID_GENDER, [])
        self.assertEqual(VALID_NAME, toothpaste.name)
        self.assertEqual(VALID_BRAND, toothpaste.brand)
        self.assertEqual(VALID_PRICE, toothpaste.price)
        self.assertEqual(VALID_GENDER, toothpaste.gender)
        self.assertIsInstance(toothpaste.ingredients, tuple)

    def test_toString_returnsCorrectlyFormattedString(self):
        # Arrange
        toothpaste = Toothpaste(VALID_NAME, VALID_BRAND, VALID_PRICE, VALID_GENDER, TEST_INGREDIENTS)

        # Act & Assert
        self.assertEqual(EXPECTED_OUTPUT ,toothpaste.to_string())
       
