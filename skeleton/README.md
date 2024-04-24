<img src="https://webassets.telerikacademy.com/images/default-source/logos/telerik-academy.svg" alt="logo" width="300px" style="margin-top: 20px;"/>

## Workshop - Queue and Stack

### 1. Description

The workshop has tests which cover the functionality of both Queue and Stack. Use them to track your progress.
The purpose of the workshop is for you to practice your ability to implement queue and stack using linked-list approach. This is a **common interview task**.

### 2. Goal

You must implement the most common methods which the Abstract Data Types Queue and Stack provide. 

The `LinkedListNode` class is already provided. Study it carefully. You are **not allowed to modify it**.

### 3. Queue
#### Description
The queue is a very useful data structure providing *first-in first-out* element access. It is most useful when an algorithm depends on such an access (such as Scheduling and BFS).
#### Task
Finish the Queue class by providing the following functionality:
- `enqueue()` - adds an element to the end of the queue
- `dequeue()` - removes the element from the front of the queue
- `peek()` - returns the value of the front element without removing it
- `count` - returns the number of elements in the queue
- `is_empty` - returns a bool indicating whether the queue is empty

Note that some of the required implementations are methods and others are properties. Do not change the names, because the unit tests depend on them.

### 5. Stack
#### Description
Similar to the queue, the stack is a very useful data structure, providing *last-in first-out* element access. As with the queue, it is most useful when an algorithm depends on such an access (such as DFS, Undo/Redo functionality, the Call Stack).
#### Task
Finish the Stack class by providing the following functionality:
- `push()` - adds an element to the top of the stack
- `pop()` - removes the element from the top of the stack
- `peek()` - returns the value of the top element without removing it
- `count` - returns the number of elements in the stack
- `is_empty` - returns a boolean indicating whether the stack is empty

Note that some of the required implementations are methods and others are properties. Do not change the names, because the unit tests depend on them.