def largest_num(array):
    if len(array) == 0:
        return 0
    elif len(array) == 1:
        return array[0]
    elif len(array) == 2:
        return array[0] if array[0] > array[1] else array[1]
    recursion = largest_num(array[1:])
    return array[0] if array[0] > recursion else recursion


print(largest_num([5, 2, 10, 1, 22, 4]))
