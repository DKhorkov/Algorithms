"""
Данный алгоритм полезен для одновременного поиска минимального и максимального элемента во множестве.
Также делается предположение, что множество состоит из уникальных неповторяющихся элементов.

Асимптоматическая скорость алгоритма O(n/2) - поскольку мы сравниваем пары = O(n).
Количество сравнений равно "пол" от 3n/2, вместо 2n - 2, если бы мы сравнивали каждый элемент с минимумом и максимумом.
"""

from typing import List, Tuple, Union


class MinAndMaxSimultaneousSearch:

    def __init__(self, arr: List[int]) -> None:
        self._arr: List[int] = arr
        self._min_value: Union[int, float] = float('-inf')
        self._max_value: Union[int, float] = float('inf')
        self._index: int = 0

        self._prepare()

    def _prepare(self) -> None:
        if len(self._arr) % 2 == 1:
            self._index = 1
            self._min_value = self._arr[0]
            self._max_value = self._arr[0]

    def search(self) -> Tuple[int, int]:
        while self._index < len(self._arr):
            first_number = self._arr[self._index]
            second_number = self._arr[self._index + 1]

            # Первое сравнение элементов между собой для определения, какой из них меньше
            if first_number < second_number:
                current_min = first_number
                current_max = second_number
            else:
                current_min = second_number
                current_max = first_number

            # Второе сравнение текущего меньшего с наименьшим
            if current_min < self._min_value:
                self._min_value = current_min

            # Третье сравнение текущего большего с наибольшим
            if current_max > self._max_value:
                self._max_value = current_max

            # Переход к следующей паре для сравнения
            self._index += 2

        return self._min_value, self._max_value


if __name__ == '__main__':
    array: List[int] = [1, 15, 4, 425, 3, 1324, 2, 7, 90]
    minimum, maximum = MinAndMaxSimultaneousSearch(arr=array).search()
    print(minimum, maximum)
