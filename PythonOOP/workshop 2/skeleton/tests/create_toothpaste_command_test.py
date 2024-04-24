import unittest
from unittest.mock import Mock

from commands.create_toothpaste import CreateToothpasteCommand


def _create_fake_params(
        *,
        name='White',
        brand='AlsoDestroysYourTeethBrand',
        price='10.99',
        gender='Men',
        ingredients='calcium,fluorid',):
    return [name, brand, price, gender, ingredients]


def _create_mock(*, product_exists_return_value: bool):
    fake_data = Mock()

    def product_exists(name):
        return product_exists_return_value

    def create_toothpaste(name, brand, price, gender, ingredients):
        product = Mock()
        product.name = name
        fake_data.products.append(product)

        return product

    fake_data.products = []
    fake_data.product_exists = product_exists
    fake_data.create_toothpaste = create_toothpaste

    return fake_data


class CreateToothPasteCommandTest_Should(unittest.TestCase):
    def test_initializer_raisesError_tooFewParamsCount(self):
        # Arrange, Act & Assert
        with self.assertRaises(ValueError):
            cmd = CreateToothpasteCommand(['a'] * 4, Mock())

    def test_initializer_raisesError_tooManyParamsCount(self):
        # Arrange, Act & Assert
        with self.assertRaises(ValueError):
            cmd = CreateToothpasteCommand(['a'] * 6, Mock())

    def test_initializer_passes_validParamsCount(self):
        # Arrange & Act
        CreateToothpasteCommand(['a'] * 5, Mock())

        # Assert
        # nothing to assert

    def test_execute_createsShampoo_validParams(self):
        # Arrange
        fake_params = _create_fake_params()
        cmd = CreateToothpasteCommand(
            fake_params,
            _create_mock(product_exists_return_value=False))

        # Act
        output = cmd.execute()

        # Assert
        self.assertEqual(
            f'Toothpaste with name {fake_params[0]} was created!', output)

    def test_execute_raisesError_productExists(self):
        # Arrange
        cmd = CreateToothpasteCommand(
            _create_fake_params(),
            _create_mock(product_exists_return_value=True))

        # Act & Assert
        with self.assertRaises(ValueError):
            cmd.execute()

    def test_execute_raisesError_invalidPrice(self):
        # Arrange
        cmd = CreateToothpasteCommand(
            _create_fake_params(price='not a float'),
            _create_mock(product_exists_return_value=False))

        # Act & Assert
        with self.assertRaises(ValueError):
            cmd.execute()

    def test_execute_raisesError_invalidGender(self):
        # Arrange
        cmd = CreateToothpasteCommand(
            _create_fake_params(gender='not a gender'),
            _create_mock(product_exists_return_value=False))

        # Act & Assert
        with self.assertRaises(ValueError):
            cmd.execute()

