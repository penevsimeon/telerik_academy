import unittest

from src.tasks import special_coins


class SpecialCoins_Test(unittest.TestCase):
    def test_one(self):
        # Arrange, Act & Assert
        self.assertEqual(2, special_coins('abcD', 'abd'))

    def test_two(self):
        # Arrange, Act & Assert
        self.assertEqual(3, special_coins('abcDD', 'cDfg'))

    def test_three(self):
        # Arrange, Act & Assert
        self.assertEqual(8, special_coins('aaaCCcccd', 'acCe'))

    def test_four(self):
        # Arrange, Act & Assert
        self.assertEqual(3, special_coins('aaBBbbbc', 'Bc'))

