import unittest

from src.stack import CustomStack


def stack_from_list(*lst):
    stack = CustomStack()
    for element in lst:
        stack.push(element)

    return stack


class CustomStack_Should(unittest.TestCase):
    def test_count_returnsZero_whenStackEmpty(self):
        # Arrange
        stack = stack_from_list()

        # Act & Assert
        self.assertEqual(0, stack.count)

    def test_count_returnsCorrectValue_whenStackNotEmpty(self):
        # Arrange
        stack = stack_from_list(1, 2, 3)

        # Act & Assert
        self.assertEqual(3, stack.count)

    def test_isempty_returnsTrue_whenStackEmpty(self):
        # Arrange
        stack = stack_from_list()

        # Act & Assert
        self.assertTrue(stack.is_empty)

    def test_isempty_returnsFalse_whenStackNotEmpty(self):
        # Arrange
        stack = stack_from_list(123)

        # Act & Assert
        self.assertFalse(stack.is_empty)

    def test_peek_raisesError_whenStackIsEmpty(self):
        # Arrange
        stack = stack_from_list()

        with self.assertRaises(ValueError):
            stack.peek()

    def test_peek_returnsCorrectItem_whenStackIsNotEmpty(self):
        # Arrange
        stack = stack_from_list(1,2,3,4)

        # Act & Assert
        self.assertEqual(4, stack.peek())

    def test_peek_doesNotRemoveItem(self):
        # Arrange
        stack = stack_from_list(1,2,3,4)

        # Act 
        _ = stack.peek()
        self.assertEqual(4, stack.count)

    def test_pop_raisesError_whenStackIsEmpty(self):
        # Arrange
        stack = stack_from_list()

        # Act & Assert
        with self.assertRaises(ValueError):
            stack.pop()

    def test_pop_returnCorrectItems(self):
        # Arrange
        stack = stack_from_list(1,2,3)

        # Act & Assert
        self.assertEqual(3, stack.pop())

    def test_pop_removesItem(self):
        # Arrange
        stack = stack_from_list(1,2,3)

        # Act
        _ = stack.pop()

        self.assertEqual(2, stack.count)

    def test_push_addsItems(self):
        # Arrange
        stack = stack_from_list()

        # Act
        stack.push(123)

        # Assert
        self.assertEqual(1, stack.count)