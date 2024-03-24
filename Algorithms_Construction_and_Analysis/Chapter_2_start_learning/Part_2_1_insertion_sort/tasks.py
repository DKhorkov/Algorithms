from typing import List, Optional


def reversed_insertion_sort(array: List[int]) -> List[int]:
    """
    Task Part_2_1 Reverse Insertion Sort
    """

    comparing_elem_index: int = 1
    array_length: int = len(array)

    while comparing_elem_index < array_length:
        # Saving element to insert it later:
        comparing_elem: int = array[comparing_elem_index]
        elem_index: int = comparing_elem_index - 1
        while elem_index >= 0 and comparing_elem > array[elem_index]:  # Reversing conditional statement
            # Shifting current element to the right:
            array[elem_index + 1] = array[elem_index]
            elem_index -= 1

        # Writing compared element
        array[elem_index + 1] = comparing_elem

        # Increasing index to iter through array:
        comparing_elem_index += 1

    return array


def linear_search(array: List[int], search_value: int) -> Optional[int]:
    """
    Task Part_2_1.3. Linear Search.

    :param array: Array of integers to search value in it.
    :param search_value: Value to search in array.
    :return:
    """

    for index in range(0, len(array)):
        if search_value == array[index]:
            return index

    return None


if __name__ == '__main__':
    array: List[int] = [31, 41, 59, 26, 41, 58]  # data from task Part_2_1.1
    print(reversed_insertion_sort(array))

    print(linear_search(array, 22), linear_search(array, 41), sep='\t')
