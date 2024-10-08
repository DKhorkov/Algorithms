"""
Префиксная сумма — подход, при котором предварительно вычисляются суммы элементов массива для быстрого получения
суммы любого подмассива. Суть в том, чтобы сэкономить время на вычислениях, не пересчитывая сумму каждый раз заново.

Префиксная сумма особенно полезна при работе с задачами, требующими частого вычисления суммы подмассивов.
Это ускоряет выполнение кода и делает его более оптимизированным.

Таким образом, мы имеем асимптоматическую скорость O(n) при подсчете префиксных сумм, и O(1) при их дальнейшем
получении каждый раз.
Расход памяти будет O(n), поскольку необходимо хранить дополнительный массив с префиксными суммами.
"""

from typing import List


class PrefixSum:

    def __init__(self, arr: List[int]) -> None:
        self._arr = arr
        self._prefix_sum_arr: List[int] = self._calculate_prefix_sum()

    def _calculate_prefix_sum(self) -> List[int]:
        """
        Создаем промежуточный массив с длиной, идентичной длине входного массива, чтобы обращатсья по индексам.
        Суммируем текущий элемент с суммой предыдущих, тем самым получая накопительный эффект
        """

        prefix_sum_arr: List[int] = [0 for _ in range(len(self._arr))]
        prefix_sum_arr[0] = self._arr[0]
        for i in range(1, len(self._arr)):
            prefix_sum_arr[i] = prefix_sum_arr[i - 1] + self._arr[i]

        return prefix_sum_arr

    def get_prefix_sum(self, first_index: int, second_index: int) -> int:
        """
        Определяем старший и младший индекс для обращения к массиву префиксных сумм, а затем возвращаем разницу
        между данными суммами (за вычетом единицы из младшего индекса, поскольку нам необходимо учитывать значение,
        которое находится во входном массиве под нижним индексом), которая и будет ответом.

        Если нижний индекс равен нулю, то возвращаем префиксную сумму, записанную под верхним индексом, поскольку
        необходимо просто взять сумму всех элементов массива до верхнего включительно.
        """

        if first_index < second_index:
            first_index, second_index = second_index, first_index

        if second_index == 0:
            return self._prefix_sum_arr[first_index]

        return self._prefix_sum_arr[first_index] - self._prefix_sum_arr[second_index - 1]


if __name__ == '__main__':
    array: List[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    prefix_sum: int = PrefixSum(array).get_prefix_sum(6, 3)
    print(prefix_sum)
