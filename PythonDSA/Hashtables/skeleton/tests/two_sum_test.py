import unittest

from src.tasks import two_sum

class TwoSum_Test(unittest.TestCase):
    def test_one(self):
        # Arrange
        numbers, target_sum = [1, 2, 3], 5
        expected = (1, 2)

        # Act
        actual = two_sum(numbers, target_sum)

        # Assert
        self.assertEqual(expected, actual)

    def test_two(self):
        # Arrange
        numbers, target_sum = [2, 0, 1, 3, 2], 4
        expected = (2, 3)

        # Act
        actual = two_sum(numbers, target_sum)

        # Assert
        self.assertEqual(expected, actual)

    def test_three(self):
        # Arrange
        numbers, target_sum = [2, 0, 1, 4, 2], 4
        expected = (1, 3)

        # Act
        actual = two_sum(numbers, target_sum)

        # Assert
        self.assertEqual(expected, actual)

    def test_four(self):
        # Arrange
        numbers, target_sum = [2, 0, 1, 5, 2], 4
        expected = (0, 4)

        # Act
        actual = two_sum(numbers, target_sum)

        # Assert
        self.assertEqual(expected, actual)

    def test_five(self):
        # Arrange
        numbers, target_sum = [1, 2, 3], 6
        expected = (-1, -1)

        # Act
        actual = two_sum(numbers, target_sum)

        # Assert
        self.assertEqual(expected, actual)
