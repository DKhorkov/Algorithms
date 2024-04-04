"""
The code for MAX-HEAPIFYMAX-HEAPIFY is quite efficient in terms of constant factors, except possibly for the
recursive call in line 10, which might cause some compilers to produce inefficient code. Write an efficient
MAX-HEAPIFYMAX-HEAPIFY that uses an iterative control construct (a loop) instead of recursion.
"""

from typing import List

from Algorithms_Construction_and_Analysis.Chapter_6_heapsort.heapsort import HeapSort


class IterativeHeapSort(HeapSort):

    def _heapify(self, index: int) -> None:
        while True:
            largest: int = index

            if index == 0:
                left = 1  # left = 2 * i, но по псевдокоду минимальный индекс = 1
            else:
                left: int = 2 * index

            right: int = left + 1

            if left < self._heap_size and self._arr[largest] < self._arr[left]:
                largest = left

            if right < self._heap_size and self._arr[largest] < self._arr[right]:
                largest = right

            if largest != index:
                self._swap(first_index=index, second_index=largest)
                index = largest
                continue

            break


if __name__ == '__main__':
    array: List[int] = [16, 14, 10, 8, 7, 9, 3, 2, 4, 1]
    sorted_array: List[int] = IterativeHeapSort(arr=array).sort()
    print(sorted_array)