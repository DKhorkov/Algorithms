"""
Bucket Sort или же карманная сортировка хороша для относительно равномерно распределенных входных данных.
В случае карманной сортировки данные лежат в диапазоне [0, 1) и распределяются по "карманам" для дальнейшей сортировки
этих карманов и их конкатенации в итоговый массив.

Поскольку в основе данной сортировки лежит сортировка вставкой, то можно предположить, что асимптоматическая скорость
алгоритма будет O(n ^ 2), однако за счет подчинения входных данных закону равномерного распределения, среднее время
работы карманной сортировки будет o(n).

Асимптоматический расход памяти равен O(n + k), где n - длина входного массива, а k - количество созданных карманов.
"""

from typing import List


class BucketSort:

    def __init__(self, arr: List[float]) -> None:
        self._arr: List[float] = arr

    def sort(self) -> List[float]:
        # Создаем промежуточный массив с "карманами"
        temp_arr: List[List] = [[] for _ in range(len(self._arr))]

        """
        Распределяем каждый элемент входного массива в соответствии с алгоритмом распределения, 
        который может быть разным. Его основная задача - равномерное распределение элементов входного массива по
        карманам для оптимальной скорости работы алгоритма.
        """
        for num in self._arr:
            bucket_index: int = int(num * len(self._arr))
            temp_arr[bucket_index].append(num)

        # Сортируем каждый карман
        for i in range(len(temp_arr)):
            temp_arr[i] = self._insertion_sort(temp_arr[i])

        """
        Объединяем отсортированные карманы без выделения дополнительной памяти, как, например, 
        в случае подобной конкатенации: [num for bucket in temp_arr for num in bucket].
        
        Переписываем каждый элемент входного массива отсортированным элементом из временного массива с карманами в
        хронологическом порядке.
        """
        index: int = 0
        for bucket in temp_arr:
            for num in bucket:
                self._arr[index] = num
                index += 1

        return self._arr

    @staticmethod
    def _insertion_sort(arr: List[float]) -> List[float]:
        for i in range(len(arr) - 1):
            for j in range(i + 1, len(arr)):
                if arr[j] < arr[i]:
                    arr[j], arr[i] = arr[i], arr[j]

        return arr


if __name__ == "__main__":
    array: List[float] = [0.1, 0.312, 0.43543, 0.123, 0.5, 0.2345, 0.4952, 0.965]
    sorted_array: List[float] = BucketSort(arr=array).sort()
    print(sorted_array)
