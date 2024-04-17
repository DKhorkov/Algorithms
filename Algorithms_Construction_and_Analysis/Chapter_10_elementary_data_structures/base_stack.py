"""
Базовая реализация стака.
Асимптоматическая скорость всех операций O(1).
"""

from typing import List, Any

from Algorithms_Construction_and_Analysis.Chapter_10_elementary_data_structures.errors import (
    StackOverflowError,
    StackUnderflowError
)


class Stack:

    def __init__(self):
        self._max_size: int = 5
        self._items: List[Any] = [0 for _ in range(self._max_size)]
        self._current_elem_index: int = -1

    def is_empty(self) -> bool:
        return self._current_elem_index == -1

    def is_full(self) -> bool:
        return self._current_elem_index == self._max_size - 1  # -1 due to index

    def push(self, element: Any) -> None:
        if self.is_full():
            raise StackOverflowError

        self._current_elem_index += 1
        self._items[self._current_elem_index] = element

    def pop(self) -> Any:
        if self.is_empty():
            raise StackUnderflowError

        value: Any = self._items[self._current_elem_index]
        self._current_elem_index -= 1
        return value

    def __len__(self) -> int:
        return self._current_elem_index + 1


if __name__ == '__main__':
    stack: Stack = Stack()
    print(stack.is_empty())
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.is_empty())
    print(stack.pop())
    stack.push(4)
    stack.push(5)
    stack.push(6)
    print(len(stack))
    print(stack.pop())
