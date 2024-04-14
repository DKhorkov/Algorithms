"""
Скользящее окно — концепция, при которой мы работаем с фиксированным набором элементов последовательности данных.
Это «окно» перемещается по последовательности, обрабатывая только те элементы, которые входят в его текущий диапазон.
Таким образом, мы можем анализировать данные по частям, что часто бывает более эффективным и экономичным с точки
зрения ресурсов.

Например, данный подход может быть использован для задачи нахождения максимальной длины последовательности единиц
в массиве, при условии, что можно заменить только определенное количество нулей, чтобы увеличить длину
последовательности единиц.
"""

from typing import List


class WindowingMethod:

    def __init__(self, arr: List[int], nums_to_change: int) -> None:
        self._arr: List[int] = arr
        self._nums_to_change: int = nums_to_change

    def calculate(self) -> int:
        """
        В данном случае асимптоматическая скорость алгоритма O(n + k), где n - длина входного массива,
        а k - размер текущего "окна".

        Затраты по памяти равны O(1).
        """

        if not self._arr:
            return 0

        left_index = 0
        right_index = 0
        changed_nums_count = 0
        max_sequence_length = 0

        """
        Расширяем окно до тех пор, пока количество измененных элементов не превышает максимальное значение 
        элементов для изменения. В этмо случае начинаем сдвигать окно слева направо.
        
        В ходе каждой итерации проверяем, не стала ли максимальная длина последовательности больше.
        """
        while right_index < len(self._arr):
            if self._arr[right_index] == 0:
                changed_nums_count += 1

            while changed_nums_count > self._nums_to_change:
                if self._arr[left_index] == 0:
                    changed_nums_count -= 1

                left_index += 1

            max_sequence_length = max(max_sequence_length, right_index - left_index + 1)
            right_index += 1

        return max_sequence_length


if __name__ == '__main__':
    array: List[int] = [0, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1]
    max_sequence_length: int = WindowingMethod(array, 1).calculate()
    print(max_sequence_length)
