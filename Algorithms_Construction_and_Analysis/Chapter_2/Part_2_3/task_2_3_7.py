"""
Describe a O(n * log n)-time algorithm that, given a set S of n integers and another integer x,
determines whether there exist two elements in S whose sum is exactly x.
"""

from typing import List

from Algorithms_Construction_and_Analysis.Chapter_2.Part_2_3.merge_sort_task_2_3_2 import merge_sort
from Algorithms_Construction_and_Analysis.Chapter_2.Part_2_3.binary_search_task_2_3_5 import binary_search


def sum_equal_target(array: List[int], target: int) -> bool:
    sorted_array = merge_sort(array)  # n * log n

    # n (iterating through all array) * log n (binary search for each element)
    for index, elem in enumerate(sorted_array):
        if elem > target:
            return False

        second_number = target - elem
        if binary_search(sorted_array, second_number, low_index=index + 1):
            return True

    return False


if __name__ == '__main__':
    array: List[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(sum_equal_target(array=array, target=15))
    print(sum_equal_target(array=array, target=20))

    array: List[int] = [10, 0, 5, 2, 0, 1, 15, 8, 9]
    print(sum_equal_target(array=array, target=0))

    array: List[int] = [10, 11, 12, 13]
    print(sum_equal_target(array=array, target=8))
