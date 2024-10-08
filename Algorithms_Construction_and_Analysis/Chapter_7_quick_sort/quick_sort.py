"""
Быстра сортировка работает в худшем случае за асимптоматические θ(n ^ 2), но в среднем случае работает за
O(n * log(n)), а также имеет маленький постоянный коэффициент. Таким образом, в большинстве случаев быстрая сортировка
будет более предпочтительной пирамидальной сортировке.
"""

from typing import List, Optional


class QuickSort:

    def __init__(self, arr: List[int]) -> None:
        self._arr: List[int] = arr

    def sort(self, low_index: int = 0, high_index: Optional[int] = None) -> List[int]:
        # Инициализация при НЕ рекурсивном (изначальном) вызове метода:
        if high_index is None:
            high_index = len(self._arr) - 1

        # Базовый случай рекурсии:
        if low_index < high_index:
            pivot_index: int = self._get_pivot_index(low_index=low_index, high_index=high_index)

            # pivot_index - 1, поскольку данный элемент массива являлся опорным и уже считается отсортированным:
            self.sort(low_index=low_index, high_index=pivot_index - 1)
            self.sort(low_index=pivot_index + 1, high_index=high_index)

        return self._arr

    def _get_pivot_index(self, low_index: int, high_index: int) -> int:
        """
        Использует последний элемент массива в качестве опорного и сортирует массив на месте без выделения
        дополнительной памяти.

        ВАЖНО: именно выбор опорного элемента является основным критерием, в зависимости от которого быстрая
        сортировка будет работать за асимптоматические θ(n ^ 2) в случае выбора несбалансированного опорного элемента
        (например, наибольшего или наименьшего значения в массиве). В таком случае одна из частей массива при рекурсии
        будет всегда пустой. Или за O(n * log(n)) в случае выбора сбалансированного опорного элемента
        (например, среднего по значению элемента в массиве).

        Возвращает индекс опорного элемента для рекурсивного вызова сортировки.
        """

        pivot_elem: int = self._arr[high_index]
        pivot_index = low_index - 1

        """
        Также итерацию начинаем с нижнего индекс, чтобы не затрагивать рекурсивно уже отсортированные элементы массива.
        
        Поскольку уже работаем с индексом, то последний элемент не будет использоваться в цикле, 
        ибо он уже используется в рамках опорного
        """
        for j in range(low_index, high_index):
            if self._arr[j] <= pivot_elem:
                pivot_index += 1
                self._swap(first_index=pivot_index, second_index=j)

        """
        Увеличиваем опорный индекс еще на единицу, чтобы поменять опорный элемент с первым элементом, 
        который больше опорного. Таким образом, получим слева от опорного индекса элементы, значение которых меньше или
        равно опорному, а справа от опорного индекс будут элементы со значением больше опорного.
        """
        pivot_index += 1
        self._swap(first_index=pivot_index, second_index=high_index)
        return pivot_index

    def _swap(self, first_index: int, second_index: int) -> None:
        self._arr[first_index], self._arr[second_index] = self._arr[second_index], self._arr[first_index]


if __name__ == '__main__':
    array: List[int] = [2, 8, 7, 1, 3, 5, 6, 4]
    quick_sort: QuickSort = QuickSort(arr=array)
    sorted_arr: List[int] = quick_sort.sort()
    print(sorted_arr)
