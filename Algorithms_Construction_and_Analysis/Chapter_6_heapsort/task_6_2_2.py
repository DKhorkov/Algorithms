"""
Starting with the procedure MAX-HEAPIFYMAX-HEAPIFY, write pseudocode for the procedure MIN-HEAPIFY(A,i),
which performs the corresponding manipulation on a min-heap. How does the running time of MIN-HEAPIFYMIN-HEAPIFY
compare to that of MAX-HEAPIFYMAX-HEAPIFY?
"""

from typing import List

from Algorithms_Construction_and_Analysis.Chapter_6_heapsort.heapsort import HeapSort


class ReversedHeapSort(HeapSort):

    def _heapify(self, index: int) -> None:
        """
        Логика длял НЕУБЫВАЮЩЕЙ (ВОЗРАСТАЮЩЕЙ) пирамиды.

        По факту, создается реверсивная сортировка.

        Время выполнения полностью равно стандартной пирамидальной сортировке  = O(n * log(n)).
        """

        smallest: int = index

        if index == 0:
            left = 1  # left = 2 * i, но по псевдокоду минимальный индекс = 1
        else:
            left: int = 2 * index

        right: int = left + 1

        # Сравнение меняется местами: self._arr[left] < self._arr[smallest] VS self._arr[largest] < self._arr[left]
        if left < self._heap_size and self._arr[left] < self._arr[smallest]:
            smallest = left

        if right < self._heap_size and self._arr[right] < self._arr[smallest]:
            smallest = right

        if smallest != index:
            self._swap(first_index=index, second_index=smallest)
            self._heapify(smallest)


if __name__ == '__main__':
    array: List[int] = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
    sorted_array: List[int] = ReversedHeapSort(arr=array).sort()
    print(sorted_array)
