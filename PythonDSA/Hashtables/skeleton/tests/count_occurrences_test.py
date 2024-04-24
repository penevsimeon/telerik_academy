import unittest

from src.tasks import count_occurrences


class CountOccurrences_Tests(unittest.TestCase):
    def test_one(self):
        # Arrange
        test = ['gosho', 'pesho', 'gosho']
        expected = {'gosho': 2, 'pesho': 1}

        # Act
        actual = count_occurrences(test)

        # Assert
        self.assertDictEqual(expected, actual)

    def test_two(self):
        # Arrange
        test = ['python', 'is', 'awesome']
        expected = {'python': 1, 'is': 1, 'awesome': 1}

        # Act
        actual = count_occurrences(test)

        # Assert
        self.assertDictEqual(expected, actual)

    def test_three(self):
        # Arrange
        test = ['must', 'learn', 'hash tables', '...',
                'must', 'learn', 'hash tables', '!']
        expected = {'must': 2, 'learn': 2, 'hash tables': 2, '!': 1, '...': 1}

        # Act
        actual = count_occurrences(test)

        # Assert
        self.assertDictEqual(expected, actual)
