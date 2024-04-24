import unittest

from src.tasks import are_isomorphic


class AreIsomorphic_Test(unittest.TestCase):
    def test_one(self):
        # Arrange, Act & Assert
        self.assertTrue(are_isomorphic('egg', 'add'))

    def test_two(self):
        # Arrange, Act & Assert
        self.assertFalse(are_isomorphic('aab', 'xyz'))

    def test_three(self):
        # Arrange, Act & Assert
        self.assertTrue(are_isomorphic('paper', 'title'))

    def test_four(self):
        # Arrange, Act & Assert
        self.assertFalse(are_isomorphic('tidal', 'paper'))

    def test_five(self):
        # Arrange, Act & Assert
        self.assertFalse(are_isomorphic('JavaScript', 'Python'))

    def test_six(self):
        # Arrange, Act & Assert
        self.assertTrue(are_isomorphic('listen', 'silent'))

    def test_seven(self):
        # Arrange, Act & Assert
        self.assertFalse(are_isomorphic('theeyes', 'theysee'))
