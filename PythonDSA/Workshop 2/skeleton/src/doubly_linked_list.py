from src.linked_list_node import LinkedListNode


class DoublyLinkedList:
    def __init__(self):
        self._head: LinkedListNode or None = None
        self._tail: LinkedListNode or None = None
        self._count = 0

    @property
    def is_empty(self):
        if self._count == 0:
            return True

    @property
    def count(self):
        return self._count

    @property
    def head(self):
        return self._head

    @property
    def tail(self):
        return self._tail

    def add_first(self, value):
        new_node = LinkedListNode(value)

        if self.is_empty:
            self._head = new_node
            self._tail = new_node
        else:
            new_node.next = self._head
            self._head.prev = new_node
            self._head = new_node

        self._count += 1

    def add_last(self, value):
        new_node = LinkedListNode(value)

        if self.is_empty:
            self._head = new_node
            self._tail = new_node
        else:
            new_node.prev = self._tail
            self._tail.next = new_node
            self._tail = new_node

        self._count += 1

    def insert_after(self, node, value):
        new_node = LinkedListNode(value)

        if node is None:
            raise ValueError('Node cannot be None')

        new_node.prev = node
        new_node.next = node.next

        node.next = new_node

        if node.next.next is None:
            self._tail = new_node

        self._count += 1

    def insert_before(self, node, value):
        if node is None:
            raise ValueError('Node cannot be None')

        new_node = LinkedListNode(value)

        new_node.next = node
        new_node.prev = node.prev

        if node.prev is not None:
            node.prev.next = new_node
        else:
            self._head = new_node

        node.prev = new_node

        self._count += 1

    def remove_first(self):
        if self._head is None:
            raise ValueError('Cannot remove first element of empty list!')
        value = self._head.value
        self._head = self._head.next
        self._count -= 1
        return value

    def remove_last(self):
        if self._head is None:
            raise ValueError('Cannot remove last element of empty list!')
        value = self._tail.value
        self._tail = self._tail.prev
        self._count -= 1
        return value

    def find(self, value):
        curr = self._head

        while curr:
            if curr.value == value:
                break
            curr = curr.next

        return curr

    def values(self):
        vals = []
        curr = self._head

        while curr is not None:
            vals.append(curr.value)
            curr = curr.next

        return tuple(vals)


def _insert_before_head(self, value):
    raise NotImplementedError()


def _insert_after_tail(self, value):
    raise NotImplementedError()
