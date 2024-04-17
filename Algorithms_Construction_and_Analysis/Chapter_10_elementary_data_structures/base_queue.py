"""
Базовая реализация очереди.
Асимптоматическая скорость всех операций O(1).
"""

from typing import List, Any

from Algorithms_Construction_and_Analysis.Chapter_10_elementary_data_structures.errors import (
    EmptyQueueError,
    QueueOverflowedError
)


class Queue:

    def __init__(self) -> None:
        self._max_size: int = 5
        self._items: List[Any] = [0 for _ in range(self._max_size)]
        self._get_index: int = 0
        self._put_index: int = 0
        self._length: int = 0

    def is_empty(self) -> bool:
        return self._length == 0

    def is_full(self) -> bool:
        """
        Если очередь заполнена, то дальнейшая вставка начнет переписывать следующие заадчи,
        которые еще не были получены.
        """

        return self._get_index == self._put_index and self._length != 0

    def put(self, element: Any) -> None:
        # Реализация задачи 10.1.4
        if self.is_full():
            raise QueueOverflowedError

        self._items[self._put_index] = element
        self._length += 1
        if self._put_index == self._max_size - 1:
            self._put_index = 0
        else:
            self._put_index += 1

    def get(self) -> Any:
        # Реализация задачи 10.1.4
        if self.is_empty():
            raise EmptyQueueError

        value: Any = self._items[self._get_index]
        self._length -= 1
        if self._get_index == self._max_size - 1:
            self._get_index = 0
        else:
            self._get_index += 1

        return value

    def __len__(self) -> int:
        return self._length


if __name__ == '__main__':
    queue: Queue = Queue()
    print(queue.is_empty())
    queue.put(1)
    queue.put(2)
    queue.put(3)
    print(queue.is_empty())
    print(queue.get())
    # print(queue.get())
    # print(queue.get())
    # print(queue.get())
    queue.put(4)
    queue.put(5)
    queue.put(6)
    print(queue.get())
    queue.put(7)
    # queue.put(8)
