from typing import List, Optional


def binary_search(array: List[int], target: int, low_index: int = 0, high_index: Optional[int] = None) -> Optional[int]:
    """
    :param array: Sorted array with values.
    :param target: Target to find in sorted array.
    :param low_index: Lowest index to search from in the array.
    :param high_index: Highest index to search from in the array.
    :return:
    """

    if high_index is None:  # if not high_index when high_index == 0 will pass condition
        high_index = len(array) - 1

    if low_index > high_index:
        return

    """ 
    If the target not in the middle of the array, and target is less than array element in the middle,
    recursively searching in the array, but divide high_index by 2, which is equal to middle index. 
    
    Else if the target not in the middle of the array, and target is greater than array element in the middle,
    recursively searching in the array, but multiply low_index by 2, which is equal to middle index. 
    
    Due to the fact, that array[mid_index] was already checked, there is no need to check it again in recursions.
    """

    middle_index = (high_index + low_index) // 2
    if array[middle_index] == target:
        return middle_index
    elif array[middle_index] > target:
        return binary_search(array=array, target=target, low_index=low_index, high_index=middle_index - 1)
    elif array[middle_index] < target:
        return binary_search(array=array, target=target, low_index=middle_index + 1, high_index=high_index)


if __name__ == '__main__':
    array: List[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(binary_search(array=array, target=10))
    print(binary_search(array=array, target=3))
    print(binary_search(array=array, target=8))
