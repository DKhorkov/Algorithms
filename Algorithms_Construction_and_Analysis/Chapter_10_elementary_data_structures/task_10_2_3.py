"""
Реализовать стак с помощью односвязного списка.
"""

from typing import Optional, Any

from Algorithms_Construction_and_Analysis.Chapter_10_elementary_data_structures.errors import (
    StackOverflowError,
    StackUnderflowError
)


class ListNode:

    def __init__(self, value: Any) -> None:
        self.value: Any = value
        self.next: Optional[ListNode] = None


class LinkedListStack:

    def __init__(self) -> None:
        self.head: Optional[ListNode] = None
        self._length: int = 0
        self._max_size: int = 5

    def is_empty(self) -> bool:
        return self._length == 0

    def is_full(self) -> bool:
        return self._length == self._max_size

    def push(self, value: Any) -> None:
        if self.is_full():
            raise StackOverflowError

        node: ListNode = ListNode(value)
        node.next = self.head
        self.head = node

        self._length += 1

    def pop(self) -> ListNode:
        if self.is_empty():
            raise StackUnderflowError

        node: ListNode = self.head
        self.head = self.head.next
        self._length -= 1
        return node

    def __len__(self) -> int:
        return self._length


if __name__ == '__main__':
    stack = LinkedListStack()
    print(stack.is_empty())
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)
    print(stack.is_full())
    print(stack.pop().value)
    print(stack.pop().value)
    print(stack.pop().value)
    print(stack.pop().value)
    print(stack.pop().value)
    print(stack.is_full())
    print(stack.is_empty())
