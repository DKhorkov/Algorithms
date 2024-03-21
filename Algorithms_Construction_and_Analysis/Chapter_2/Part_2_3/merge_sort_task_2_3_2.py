from typing import List


def merge_sort(array: List[int]) -> List[int]:
    if len(array) <= 1:
        return array

    mid = len(array) // 2
    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])
    sorted_array = merge(left, right)
    return sorted_array


def merge(left: List[int], right: List[int]) -> List[int]:
    merged_array = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged_array.append(left[i])
            i += 1
        else:
            merged_array.append(right[j])
            j += 1

    if i < len(left):
        merged_array.extend(left[i:])
    elif j < len(right):
        merged_array.extend(right[j:])

    return merged_array


if __name__ == '__main__':
    array: List[int] = [3, 41, 52, 26, 38, 57, 9, 49]  # array from task Part_2_3.1
    print(merge_sort(array))
