import unittest
from unittest.mock import Mock

from models.shopping_cart import ShoppingCart


def fake_product(name='top shampoo'):
    product = Mock()
    product.name = name
    product.price = 2.5

    return product


class ShoppingCart_Should(unittest.TestCase):
    def test_constructor_initializesProducts_asCorrectType_when_shoppingCartCreated(self):
        cart = ShoppingCart()
        self.assertIsInstance(cart.products, tuple)

    def test_addProduct_should_addProductToList(self):
        # Arrange
        cart = ShoppingCart()

        # Act
        cart.add_product(fake_product())

        # Assert
        self.assertEqual(1, len(cart.products))

    def test_removeProduct_removesProductFromList(self):
        # Arrange
        cart = ShoppingCart()
        product = fake_product()
        cart.add_product(product)

        # Act
        cart.remove_product(product)

        # Assert
        self.assertEqual(0, len(cart.products))

    def test_containsProduct_returnsTrue_when_productFound(self):
        # Arrange
        cart = ShoppingCart()
        product = fake_product()
        cart.add_product(product)

        # Act & Assert
        self.assertTrue(cart.contains_product(product))

    def test_containsProduct_returnsFalse_when_productFound(self):
        # Arrange
        cart = ShoppingCart()
        cart.add_product(fake_product())

        # Act & Assert
        self.assertFalse(cart.contains_product(fake_product('another name')))

    def test_totalPrice_returnsCorrectSum_when_cartHasProducts(self):
        # Arrange
        cart = ShoppingCart()
        cart.add_product(fake_product())
        cart.add_product(fake_product())
        cart.add_product(fake_product())

        # Act & Assert
        self.assertEqual(7.5, cart.total_price())

    def test_totalPrice_returnsZero_when_cartHasNoProducts(self):
        # Arrange
        cart = ShoppingCart()

        # Act & Assert
        self.assertEqual(0, cart.total_price())
