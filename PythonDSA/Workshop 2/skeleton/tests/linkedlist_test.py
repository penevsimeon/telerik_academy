import unittest
from src.doubly_linked_list import DoublyLinkedList


class DoublyLinkedList_Should(unittest.TestCase):
    def test_addfirst_updatesCount(self):
        # Arrange
        test_list = DoublyLinkedList()
        test_list.add_first(300)

        # Act & Assert
        self.assertEqual(1, test_list.count)

    def test_addfirst_updatesHead_whenListIsEmpty(self):
        # Arrange
        test_list = DoublyLinkedList()
        test_list.add_first(300)

        # Act & Assert
        self.assertEqual(300, test_list.head.value)

    def test_addfirst_updatesTail_whenListIsEmpty(self):
        # Arrange
        test_list = DoublyLinkedList()
        test_list.add_first(300)

        # Act & Assert
        self.assertEqual(300, test_list.tail.value)

    def test_addfirst_updatesHead_whenListIsNotEmpty(self):
        # Arrange
        test_list = DoublyLinkedList()
        test_list.add_first(300)
        test_list.add_first(400)

        # Act & Assert
        self.assertEqual(400, test_list.head.value)

    def test_addfirst_maintainsCorrectOrder(self):
        # Arrange
        test_list = DoublyLinkedList()
        test_list.add_first(4)
        test_list.add_first(5)
        test_list.add_first(6)

        # Act & Assert
        self.assertEqual((6, 5, 4), test_list.values())

    def test_addlast_updatesCount(self):
        # Arrange
        test_list = DoublyLinkedList()
        test_list.add_last(300)

        # Act & Assert
        self.assertEqual(1, test_list.count)

    def test_addlast_updatesTail_whenListIsEmpty(self):
        # Arrange
        test_list = DoublyLinkedList()
        test_list.add_last(300)

        # Act & Assert
        self.assertEqual(300, test_list.tail.value)

    def test_addlast_updatesHead_whenListIsEmpty(self):
        # Arrange
        test_list = DoublyLinkedList()
        test_list.add_last(300)

        # Act & Assert
        self.assertEqual(300, test_list.head.value)

    def test_addlast_updatesTail_whenListIsNotEmpty(self):
        # Arrange
        test_list = DoublyLinkedList()
        test_list.add_last(300)
        test_list.add_last(400)

        # Act & Assert
        self.assertEqual(400, test_list.tail.value)

    def test_addlast_maintainsCorrectOrder(self):
        # Arrange
        test_list = DoublyLinkedList()
        test_list.add_last(4)
        test_list.add_last(5)
        test_list.add_last(6)

        # Act & Assert
        self.assertEqual((4, 5, 6), test_list.values())

    def test_count_returnsZero_whenListIsEmpty(self):
        # Arrange
        test_list = DoublyLinkedList()

        # Act & Assert
        self.assertEqual(0, test_list.count)

    def test_count_returnsCorrect_whenListIsNotEmpty(self):
        # Arrange
        test_list = DoublyLinkedList()
        times = 10
        for i in range(times):
            test_list.add_last(i)
            test_list.add_first(i)

        # Act & Assert
        self.assertEqual(times * 2, test_list.count)

    def test_values_returnsEmptyTuple_whenEmptyList(self):
        # Arrange
        test_list = DoublyLinkedList()

        # Act & Assert
        self.assertEqual((), test_list.values())

    def test_values_returnsValuesAsTuple_whenNonEmptyList(self):
        # Arrange
        test_list = DoublyLinkedList()
        for i in range(3):
            test_list.add_last(i)
            test_list.add_first(i)

        # Act & Assert
        self.assertEqual((2, 1, 0, 0, 1, 2), test_list.values())

    def test_find_returnsCorrectNode(self):
        # Arrange
        test_list = DoublyLinkedList()
        test_list.add_first(2)
        test_list.add_first(4)

        # Act
        node = test_list.find(4)

        # Assert
        self.assertEqual(4, node.value)

    def test_find_returnsNodeAsReference(self):
        # Arrange
        test_list = DoublyLinkedList()
        test_list.add_first(2)
        test_list.add_first(4)

        # Act
        node = test_list.find(2)

        # Assert
        self.assertEqual(test_list.head.next, node)

    def test_find_returnsNone_whenEmptyList(self):
        # Arrange
        test_list = DoublyLinkedList()

        # Act
        node = test_list.find(1234)

        # Assert
        self.assertIsNone(node)

    def test_find_returnsNone_whenNotPresent(self):
        # Arrange
        test_list = DoublyLinkedList()
        test_list.add_first(2)
        test_list.add_first(4)
        test_list.add_first(7)

        # Act
        node = test_list.find(300)

        # Assert
        self.assertIsNone(node)

    def test_head_isNone_whenListEmpty(self):
        # Arrange
        test_list = DoublyLinkedList()

        # Act & Assert
        self.assertIsNone(test_list.head)

    def test_head_isNone_afterLastRemoval(self):
        # Arrange
        test_list = DoublyLinkedList()
        test_list.add_first(2)

        # Act
        test_list.remove_first()

        # Assert
        self.assertIsNone(test_list.head)

    def test_head_returnCorrectValue_whenNotNone(self):
        # Arrange
        test_list = DoublyLinkedList()
        test_list.add_first(4)
        test_list.add_first(8)

        # Act & Assert
        self.assertEqual(8, test_list.head.value)

    def test_tail_isNone_whenListEmpty(self):
        # Arrange
        test_list = DoublyLinkedList()

        # Act & Assert
        self.assertIsNone(test_list.tail)

    def test_tail_isNone_afterLastRemoval(self):
        # Arrange
        test_list = DoublyLinkedList()
        test_list.add_last(2)

        # Act
        test_list.remove_last()

        # Assert
        self.assertIsNone(test_list.tail)

    def test_tail_returnCorrectValue_whenNotNone(self):
        # Arrange
        test_list = DoublyLinkedList()
        test_list.add_first(4)
        test_list.add_first(8)

        # Act & Assert
        self.assertEqual(4, test_list.tail.value)

    def test_insertafter_insertsInMiddle(self):
        # Arrange
        test_list = DoublyLinkedList()
        test_list.add_last(1)
        test_list.add_last(2)
        test_list.add_last(4)
        node = test_list.find(2)

        # Act
        test_list.insert_after(node, 3)

        # Assert
        self.assertEqual((1, 2, 3, 4), test_list.values())

    def test_insertafter_insertsAtEnd(self):
        # Arrange
        test_list = DoublyLinkedList()
        test_list.add_last(1)
        test_list.add_last(2)
        test_list.add_last(3)
        node = test_list.find(3)

        # Act
        test_list.insert_after(node, 4)

        # Assert
        self.assertEqual((1, 2, 3, 4), test_list.values())

    def test_insertafter_updatesTail(self):
        # Arrange
        test_list = DoublyLinkedList()
        test_list.add_last(1)
        test_list.add_last(2)
        test_list.add_last(3)
        node = test_list.find(3)

        # Act
        test_list.insert_after(node, 4)

        # Assert
        self.assertEqual(4, test_list.tail.value)

    def test_insertafter_updatesCount(self):
        # Arrange
        test_list = DoublyLinkedList()
        test_list.add_last(1)
        test_list.add_last(2)
        test_list.add_last(3)
        node = test_list.find(3)

        # Act
        test_list.insert_after(node, 4)

        # Assert
        self.assertEqual(4, test_list.count)

    def test_insertafter_throwsWhenNodeIsNone(self):
        # Arrange
        test_list = DoublyLinkedList()

        # Act & Assert
        with self.assertRaises(ValueError):
            test_list.insert_after(None, 2)

    def test_insertbefore_insertsInMiddle(self):
        # Arrange
        test_list = DoublyLinkedList()
        test_list.add_last(1)
        test_list.add_last(2)
        test_list.add_last(4)
        node = test_list.find(4)

        # Act
        test_list.insert_before(node, 3)

        # Assert
        self.assertEqual((1, 2, 3, 4), test_list.values())

    def test_insertbefore_insertsAtStart(self):
        # Arrange
        test_list = DoublyLinkedList()
        test_list.add_last(2)
        test_list.add_last(3)
        test_list.add_last(4)
        node = test_list.find(2)

        # Act
        test_list.insert_before(node, 1)

        # Assert
        self.assertEqual((1, 2, 3, 4), test_list.values())

    def test_insertbefore_updatesHead(self):
        # Arrange
        test_list = DoublyLinkedList()
        test_list.add_last(1)
        test_list.add_last(2)
        test_list.add_last(3)
        node = test_list.find(1)

        # Act
        test_list.insert_before(node, 4)

        # Assert
        self.assertEqual(4, test_list.head.value)

    def test_insertbefore_updatesCount(self):
        # Arrange
        test_list = DoublyLinkedList()
        test_list.add_last(1)
        test_list.add_last(2)
        test_list.add_last(3)
        node = test_list.find(3)

        # Act
        test_list.insert_before(node, 4)

        # Assert
        self.assertEqual(4, test_list.count)

    def test_insertbefore_throwsWhenNodeIsNone(self):
        # Arrange
        test_list = DoublyLinkedList()

        # Act & Assert
        with self.assertRaises(ValueError):
            test_list.insert_before(None, 2)

    def test_removefirst_returnsCorrectValue_whenOneNodeList(self):
        # Arrange
        test_list = DoublyLinkedList()
        test_list.add_last(2)

        # Act & Assert
        self.assertEqual(2, test_list.remove_first())

    def test_removefirst_returnsCorrectValue_whenMultipleNodesInList(self):
        # Arrange
        test_list = DoublyLinkedList()
        test_list.add_last(3)
        test_list.add_first(2)
        test_list.add_last(4)
        test_list.add_last(5)
        test_list.add_first(1)
        test_list.add_last(6)

        # Act & Assert
        self.assertEqual(1, test_list.remove_first())

    def test_removefirst_updatesCount(self):
        # Arrange
        test_list = DoublyLinkedList()
        test_list.add_last(3)
        test_list.add_last(2)

        # Act
        _ = test_list.remove_first()

        # Assert
        self.assertEqual(1, test_list.count)

    def test_removefirst_updatesHead(self):
        # Arrange
        test_list = DoublyLinkedList()
        test_list.add_last(3)

        # Act
        _ = test_list.remove_first()

        # Assert
        self.assertIsNone(test_list.head)

    def test_removefirst_raisesValueError_emptyList(self):
        # Arrange
        test_list = DoublyLinkedList()

        # Act & Assert
        with self.assertRaises(ValueError):
            test_list.remove_first()

    def test_removelast_returnsCorrectValue_whenOneNodeList(self):
        # Arrange
        test_list = DoublyLinkedList()
        test_list.add_first(2)

        # Act & Assert
        self.assertEqual(2, test_list.remove_last())

    def test_removelast_returnsCorrectValue_whenMultipleNodesInList(self):
        # Arrange
        test_list = DoublyLinkedList()
        test_list.add_last(3)
        test_list.add_first(2)
        test_list.add_last(4)
        test_list.add_first(5)
        test_list.add_first(1)

        # Act & Assert
        self.assertEqual(4, test_list.remove_last())

    def test_removelast_updatesCount(self):
        # Arrange
        test_list = DoublyLinkedList()
        test_list.add_last(3)
        test_list.add_last(5)

        # Act
        _ = test_list.remove_last()

        # Assert
        self.assertEqual(1, test_list.count)

    def test_removelast_updatesTail(self):
        # Arrange
        test_list = DoublyLinkedList()
        test_list.add_last(3)

        # Act
        _ = test_list.remove_last()

        # Assert
        self.assertIsNone(test_list.tail)

    def test_removelast_raisesValueError_emptyList(self):
        # Arrange
        test_list = DoublyLinkedList()

        # Act & Assert
        with self.assertRaises(ValueError):
            test_list.remove_last()
