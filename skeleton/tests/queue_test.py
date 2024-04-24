import unittest

from src.queue import CustomQueue


def queue_from_list(*lst):
    q = CustomQueue()
    for element in lst:
        q.enqueue(element)

    return q


class CustomQueue_Should(unittest.TestCase):
    def test_count_returnsZero_whenQueueEmpty(self):
        # Arrange
        q = queue_from_list()

        # Act & Assert
        self.assertEqual(0, q.count)

    def test_count_returnsCorrectValue_whenQueueNotEmpty(self):
        # Arrange
        q = queue_from_list(1, 2, 3)

        # Act & Assert
        self.assertEqual(3, q.count)

    def test_isempty_returnsTrue_whenQueueEmpty(self):
        # Arrange
        q = queue_from_list()

        # Act & Assert
        self.assertTrue(q.is_empty)

    def test_isempty_returnsFalse_whenQueueNotEmpty(self):
        # Arrange
        q = queue_from_list(123)

        # Act & Assert
        self.assertFalse(q.is_empty)

    def test_peek_raisesError_whenQueueIsEmpty(self):
        # Arrange
        q = queue_from_list()

        with self.assertRaises(ValueError):
            q.peek()

    def test_peek_returnsCorrectItem_whenQueueIsNotEmpty(self):
        # Arrange
        q = queue_from_list(1,2,3,4)

        # Act & Assert
        self.assertEqual(1, q.peek())

    def test_peek_doesNotRemoveItem(self):
        # Arrange
        q = queue_from_list(1,2,3,4)

        # Act 
        _ = q.peek()
        self.assertEqual(4, q.count)

    def test_dequeue_raisesError_whenQueueIsEmpty(self):
        # Arrange
        q = queue_from_list()

        # Act & Assert
        with self.assertRaises(ValueError):
            q.dequeue()

    def test_dequeue_returnCorrectItems(self):
        # Arrange
        q = queue_from_list(1,2,3)

        # Act & Assert
        self.assertEqual(1, q.dequeue())

    def test_dequeue_removesItem(self):
        # Arrange
        q = queue_from_list(1,2,3)

        # Act
        _ = q.dequeue()

        self.assertEqual(2, q.count)

    def test_enqueue_addsItems(self):
        # Arrange
        q = queue_from_list()

        # Act
        q.enqueue(123)

        # Assert
        self.assertEqual(1, q.count)