def summing_array_elems(array):
    if len(array) == 0:  # Если не указать нулевую длину, то при пустом списке будет ошибка, если возвращать 1 элемент
        return 0
    return array[0] + summing_array_elems(array[1:])


print(summing_array_elems([10, 1, 2, 3, 4]))


def count_array_elems(array):
    if len(array) == 0:
        return 0
    return 1 + count_array_elems(array[1:])


print(count_array_elems([10, 1, 2, 3, 4]))
