"""
Write pseudocode for the brute-force method of solving the maximum-subarray problem.
Procedure should run in Θ(n^2) time.
"""

from typing import List, Tuple, Union
from math import inf


def max_subarray_brute_force(array: List[int]) -> Tuple[int, int, Union[int, float]]:
    max_sum: float = -inf
    low_index: int = 0
    high_index: int = 0
    for i in range(len(array)):
        sum: int = 0
        for j in range(i, len(array)):
            sum += array[j]
            if sum > max_sum:
                max_sum = sum
                low_index = i
                high_index = j

    return low_index, high_index, max_sum


if __name__ == '__main__':
    array: List[int] = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    left_index, right_index, max_sum = max_subarray_brute_force(array=array)
    max_subarray: List[int] = array[left_index: right_index + 1]
    print(array, max_subarray, max_sum, sep='\t-\t')
