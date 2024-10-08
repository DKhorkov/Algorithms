from typing import List


class HeapSort:

    def __init__(self, arr: List[int]) -> None:
        self._arr: List[int] = arr
        self._length: int = len(self._arr)
        self._heap_size: int = self._length

    def sort(self) -> List[int]:
        """
        Скорость работы алгоритма равна:
        O(n) - для каждого индекса, кроме 0; * O(log(n)) - приведение пирамиды к невозрастающему виду = O(n * log(n)).
        """

        self._build_heap()

        """
        Сортируем пирамиду, меняя каждый элемент с конца с первым элементом массива (который и будет всегда наибольшим).
        Первый параметр = длина - 1, поскольку нам нужен максимальный индекс.
        Второй параметр = 0, поскольку с 0 индексом мы всегда и будем производить перестановку.
        Третий параметр = -1 для реализации процедуры down_to.
        """
        for i in range(self._length - 1, 0, -1):
            self._swap(first_index=0, second_index=i)

            # Поскольку теперь у нас есть один отсортированный элемент, то размер пирамиды уменьшается на 1.
            self._heap_size -= 1

            # Перестраиваем пирамиду после нашей перестановки, чтобы она продолжала оставаться невозрастающей.
            self._heapify(0)

        return self._arr

    def _build_heap(self) -> None:
        """
        Строит невозрастающую пирамиду для целей сортировки со скоростью O(n * log(n)).

        Поскольку последний родитель находится в середине массива (n//2), то с него можно начать построение пирамиды.
        Второй параметр = -1, чтобы ограничение генератором range() также вернуло нулевой индекс нашего массива.
        Третий параметр также = -1 для реализации процедуры down_to.
        """

        for index in range(self._length // 2, -1, -1):
            self._heapify(index=index)

    def _heapify(self, index: int) -> None:
        """
        Согласно второму закону основного метода решения рекуррентных уравнений,
        скорость алгоритма будет равна O(log(n)).
        """

        largest: int = index

        # Согласно правилу:
        if index == 0:
            left = 1  # left = 2 * i, но по псевдокоду минимальный индекс = 1
        else:
            left: int = 2 * index

        right: int = left + 1

        """
        Если индекс меньше размера пирамиды (то есть является листом или узлом), а также его значение больше 
        максимального - значит он и является максимальным
        """
        if left < self._heap_size and self._arr[largest] < self._arr[left]:
            largest = left

        # Аналогичная проверка, как и для левой ветви.
        if right < self._heap_size and self._arr[largest] < self._arr[right]:
            largest = right

        """
        Если текущий индекс и является максимальным, то дальнейшая сортировка не нужна.
        
        В противном случае производим построение пирамиды для ветви, предварительно поменяв местами 
        полученный в параметрах индекс с индексом, под которым находится максимальное значение в пирамиде.
        Таким образом, наша ветвь станет невозрастающей пирамидой.
        """
        if largest != index:
            self._swap(first_index=index, second_index=largest)
            self._heapify(largest)

    def _swap(self, first_index, second_index) -> None:
        self._arr[first_index], self._arr[second_index] = self._arr[second_index], self._arr[first_index]


if __name__ == '__main__':
    array: List[int] = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
    sorted_array: List[int] = HeapSort(arr=array).sort()
    print(sorted_array)
