"""
Randomized Selection - алгоритм основанный на быстрой сортировке, но использующийся для выбора k-th
(в данном случае наименьшего) элемента во входном массиве. Например, если k = 3, то мы ищем 3 наименьший
элемент во входном массиве. В отличие от алгоритма быстрой сортировки, рекурсивно будет вызываться поиск только для
одной из двух частей разделенного по опорному элементу входного массива.

В алгоритм НЕ ДОЛЖЕН передаваться пустой массив, а k должно принадлежать диапазону [1, len(arr)].

В наихудшем случае асимптоматическая скорость работы алгоритма составит O(n ^ 2), поскольку рандом не исключает
выбор несбалансированного (плохого) опорного элемента для каждого рекурсивного вызова. Однако ожидаемое время работы
алгоритма будет O(n), поскольку он рандомизирован и никакие входные данные не могут гарантированно привести к
наихудшему поведению алгоритма.
"""

from typing import List, Optional

from Algorithms_Construction_and_Analysis.Chapter_7_quick_sort.randomized_quick_sort import RandomizedQuickSort


class RandomizedSelection(RandomizedQuickSort):

    def __init__(self, arr: List[int], k: int) -> None:
        super().__init__(arr=arr)
        self._k: int = k

        if not self._arr:
            raise ValueError("arr cannot be empty")

        if self._k < 1 or self._k > len(self._arr):
            raise ValueError("k cannot be greater than len(arr) or less than 1")

    def search(self, low_index: int = 0, high_index: Optional[int] = None) -> int:
        if high_index is None:
            high_index = len(self._arr) - 1

        """
        Базовый выход из рекурсии, в случае, когда массив состоит из 1 элемента, который и будет возвращен.
        """
        if low_index == high_index:
            return self._arr[low_index]

        """
        В ходе выбора опорного элемента производится его сортировка так, что все эелементы во входном массиве до 
        опорного элемента будут меньше или равны ему, а все элементы после входного массива будут больше 
        опорного элемента.
        
        Далее вычисляется количество элементов в подмассиве меньшем подмассиве, то есть количество элементов, 
        попадающих в меньшую часть разбиения + опорный элемент. 
        Если количество элементов в выбранном подмассиве равняется k-th, то ответом является опорный элемент,
        поскольку подмассив уже будет отсортирован ранее.
        
        В ином случае, вызывается рекурсия.
        """
        pivot_index: int = self._get_randomized_pivot_index(low_index=low_index, high_index=high_index)
        elements_count: int = pivot_index - low_index + 1
        if elements_count == self._k:
            return self._arr[pivot_index]
        elif self._k < elements_count:
            return self.search(low_index=low_index, high_index=pivot_index - 1)
        else:
            self._k -= elements_count
            return self.search(low_index=pivot_index + 1, high_index=high_index)


if __name__ == '__main__':
    array: List[int] = [3, 1, 8, 4, 7, 9]
    for i in range(100):
        k_minimum: int = RandomizedSelection(arr=array, k=1).search()
        print(k_minimum, end='')
