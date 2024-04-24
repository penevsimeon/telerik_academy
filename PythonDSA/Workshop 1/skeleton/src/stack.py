from src.linked_list_node import LinkedListNode


class CustomStack:
    def __init__(self):
        self.top = None
        self._count = 0

    def push(self, value):
        new_node = LinkedListNode(value)

        self.top = new_node

        self._count += 1

    def pop(self):
        if self.is_empty:
            raise ValueError('Cannot pop on empty stack!')

        popped_value = self.top.value

        self.top = self.top.next

        self._count -= 1

        return popped_value

    def peek(self):
        if self.is_empty:
            raise ValueError('Cannot peek on empty stack!')

        return self.top.value

    @property
    def is_empty(self):
        if self._count == 0:
            return True

    @property
    def count(self):
        return self._count
