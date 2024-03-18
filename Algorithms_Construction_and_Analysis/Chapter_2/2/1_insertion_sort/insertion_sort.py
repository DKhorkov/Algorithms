from typing import List


def insertion_sort(array: List[int]) -> List[int]:
    comparing_elem_index: int = 1
    array_length: int = len(array)

    while comparing_elem_index < array_length:
        # Saving element to insert it later:
        comparing_elem: int = array[comparing_elem_index]
        elem_index: int = comparing_elem_index - 1
        while elem_index >= 0 and array[elem_index] > comparing_elem:
            # Shifting current element to the right:
            array[elem_index + 1] = array[elem_index]
            elem_index -= 1

        # Writing compared element
        array[elem_index + 1] = comparing_elem

        # Increasing index to iter through array:
        comparing_elem_index += 1

    return array


if __name__ == '__main__':
    array: List[int] = [31, 41, 59, 26, 41, 58]  # data from task 2.1
    print(insertion_sort(array))
