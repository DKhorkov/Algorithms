"""
Задача переместить все элементы массива, которые равны заданному числу в конец входного массива
Выполняется с помощью 2 указателей (индексов).

Скорость работы алгоритма O(n), а затраты памяти O(1).
"""

from typing import List


class TwoPointersSort:

    def __init__(self, arr: List[int], num: int) -> None:
        self._arr: List[int] = arr
        self._num: int = num

    def sort(self) -> List[int]:
        """
        Если элемент равен искомому, то увеличиваем индекс элемента, с которым он должен быть поменен и меняем их
        местами. А если не равен, увеличиваем индекс элемента, который потенциально равен искомому.
        """

        num_to_swap_index: int = 0
        other_num_index: int = 0
        for _ in range(len(self._arr) - 1):
            flag: bool = False
            if self._arr[num_to_swap_index] != self._num:
                num_to_swap_index += 1
                other_num_index += 1
                flag = True

            if self._arr[other_num_index] == self._num:
                if not flag:
                    other_num_index += 1

            self._swap(first_index=num_to_swap_index, second_index=other_num_index)

        return self._arr

    def _swap(self, first_index: int, second_index: int) -> None:
        self._arr[first_index], self._arr[second_index] = self._arr[second_index], self._arr[first_index]


if __name__ == '__main__':
    array: List[int] = [0,1,2,2,3,0,4,2]
    sorted_array: List[int] = TwoPointersSort(array, 2).sort()
    print(sorted_array)
