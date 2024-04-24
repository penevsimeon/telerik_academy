<img src="https://webassets.telerikacademy.com/images/default-source/logos/telerik-academy.svg" alt="logo" width="300px" style="margin-top: 20px;"/>

## Workshop - Doubly Linked List

### 1. Project information

You are provided with unit tests. Use them to measure your progress and get a better understanding of the behavior of the doubly linked list methods.

### 2. Description

In most programming interviews, linked list themed tasks are given in order to test the ability of the candidate to **maintain and update references**. The LinkedList methods `add`, `insert` and `remove` are excellent tasks to practice your skills with references.

### 3. Goal

You must implement the most commonly used methods of the DoublyLinkedList data structure.

The `LinkedListNode` class is already provided. Study it carefully. You are **not allowed to modify it**.

### 4. Doubly Linked List
#### Description
The DoublyLinkedList is a very useful data structure providing very fast insertion and removals at the cost of random access. They are useful for implementing features such as browser history and text editors.

#### Task
Finish the DoublyLinkedList class by providing the following functionality:
- `add_first(value)` - adds an element to the head of the list
- `add_last(value)` - adds an element to the tail of the list
- `remove_first()` - removes the first node and returns its value
- `remove_last()` - removes the last node and returns its value
- `insert_before(node, value)` - insert an element with the given value before the given node
- `insert_after(node, value)` - insert an element with the given value after the given node
- `find(val)` - returns the first node that has the given value or null if no such value exists
- `values()` - returns all values as a tuple
- `head` - reference to the head node
- `tail` - reference to the tail node
- `count` - returns the number of nodes

Note that some of the required implementations are methods and others are properties. Do not change the names, because the unit tests depend on them.
