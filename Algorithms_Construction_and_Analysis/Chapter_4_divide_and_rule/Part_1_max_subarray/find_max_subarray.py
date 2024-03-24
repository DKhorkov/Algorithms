"""
Find a subarray whose sum will be maximum within the input array.
The growth rate of the algorithm should be O(n * log(n)), where n is the length of the input array.
"""

from typing import List, Optional, Tuple, Union
from math import inf


def find_max_subarray(
        array: List[Union[int, float]],
        low_index: int = 0,
        high_index: Optional[int] = None
) -> Tuple[int, int, Union[int, float]]:

    # First level of recursive algorithm case:
    if high_index is None:
        high_index = len(array) - 1

    # Base recursion case:
    if low_index == high_index:
        return low_index, high_index, array[low_index]

    middle_index = (low_index + high_index) // 2
    left_low_index, left_high_index, left_sum = find_max_subarray(
        array=array,
        low_index=low_index,
        high_index=middle_index
    )

    right_low_index, right_high_index, right_sum = find_max_subarray(
        array=array,
        low_index=middle_index + 1,
        high_index=high_index
    )

    cross_left_index, cross_right_index, cross_sum = find_max_crossing_subarray(
        array=array,
        low_index=low_index,
        middle_index=middle_index,
        high_index=high_index
    )

    if left_sum >= right_sum and left_sum >= cross_sum:
        return left_low_index, left_high_index, left_sum
    elif right_sum >= left_sum and right_sum >= cross_sum:
        return right_low_index, right_high_index, right_sum

    return cross_left_index, cross_right_index, cross_sum


def find_max_crossing_subarray(
        array: List[Union[int, float]],
        low_index: int,
        middle_index: int,
        high_index: int
) -> Tuple[int, int, Union[int, float]]:

    """
    The growth rate is O(n), where n is the length of the input array.
    """

    """
    Подсчет максимальной суммы в левой части массива. Начиная со среднего индекса в сторону наименьшего индекса.
    Используем "low_index - 1" для того, чтобы правильно сработало включение, так как уже используются индексы!. 
    Последний атрибут (-1) функции range используется для описанной ранее реверсии.
    """

    left_sum: float = -inf
    left_iteration_sum: int = 0
    left_min_index: int = middle_index
    for i in range(middle_index, low_index - 1, -1):  # down to equivalent
        left_iteration_sum += array[i]
        if left_iteration_sum > left_sum:
            left_sum = left_iteration_sum
            left_min_index = i

    """
    Подсчет максимальной суммы в правой части массива. Начиная со среднего индекса + 1, поскольку сам 
    средний индекс уже испоьзовался в левой части массива, в сторону наибольшего индекса.
    Используем "high_index + 1" для того, чтобы правильно сработало включение, так как уже используются индексы!
    """

    right_sum: float = -inf
    right_iteration_sum: int = 0
    right_max_index: int = middle_index + 1
    for j in range(middle_index + 1, high_index + 1):
        right_iteration_sum += array[j]
        if right_iteration_sum > right_sum:
            right_sum = right_iteration_sum
            right_max_index = j

    return left_min_index, right_max_index, left_sum + right_sum


if __name__ == '__main__':
    array: List[int] = [13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]
    left_index, right_index, max_sum = find_max_subarray(array=array)
    max_subarray: List[int] = array[left_index: right_index + 1]
    print(array, max_subarray, max_sum, sep='\t-\t')
