"""
Задача 10.1.5.

Реализация двухсторонней очереди, в которой можно производить вставку и удаление элементов с обеих сторон.
Асимптоматическая скорость всех операций O(1).
"""

from typing import Any

from Algorithms_Construction_and_Analysis.Chapter_10_elementary_data_structures.base_queue import Queue
from Algorithms_Construction_and_Analysis.Chapter_10_elementary_data_structures.errors import (
    EmptyQueueError,
    QueueOverflowedError
)


class Deque(Queue):

    def head_get(self) -> Any:
        """
        Базовая операция получение елемента из стандартной очереди.
        """

        return super().get()

    def tail_put(self, element: Any) -> None:
        """
        Базовая операция вставки елемента из стандартной очереди.
        """

        return super().put(element=element)

    def tail_get(self) -> Any:
        if self.is_empty():
            raise EmptyQueueError

        """
        Поскольку мы достаем послений вставленный элемент по аналогии со стаком, то отталкиваемся от текущего 
        индекса для вставки элемента. Раз элемент достается с конца, то уменьшаем значение индекс для вставки и 
        достаем по нему элемент. Таким образом, в ходе нормальной вставки элемента на его место будет вставлен новый
        элемент, который в последствии будет получсен последним при условии нормальной работы очереди.
        """
        if self._put_index == 0:
            self._put_index = self._max_size - 1
        else:
            self._put_index -= 1

        return self._items[self._put_index]

    def head_put(self, element: Any) -> None:
        if self.is_full():
            raise QueueOverflowedError

        """
        Поскольку мы вставляем элемент в начало, а не конец, то отталкиваемся от текущего индекса для 
        получения элемента. Раз элемент вставляется в начало, то уменьшаем значение индекс для получение и 
        вставляем на его место элемент. Таким образом, в ходе нормального получения элемента он и будет получен первым.
        """
        if self._get_index == 0:
            self._get_index = self._max_size - 1
        else:
            self._get_index -= 1

        self._items[self._get_index] = element


if __name__ == '__main__':
    deque: Deque = Deque()
    print(deque.is_empty())
    deque.tail_put(1)
    deque.tail_put(2)
    deque.head_put(3)
    print(deque.head_get())
    print(deque.tail_get())
    print(deque.head_get())
