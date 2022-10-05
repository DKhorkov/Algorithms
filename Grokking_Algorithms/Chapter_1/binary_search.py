def binary_search(sorted_list, element_for_search):
    """Бинарный алгоритм для нахождения элемента в отсортированном массиве"""
    lowest_elem = 0
    highest_elem = len(sorted_list) - 1  # Поскольку нам нужен индекс элемента

    # Если не будет условия - цикл никогда не закончится. Также нужно <=, иначе не будет находиться первый элемент.
    # = нужно, поскольку highest_elem ниже рассчитывается как середина МИНУС ЕДИНИЦА:
    while lowest_elem <= highest_elem:
        middle = (lowest_elem + highest_elem) // 2  # Если рассчитывать вне цикла - переменная не будет меняться
        if sorted_list[middle] == element_for_search:
            return middle  # Возвращаем индекс нужного нам элемента
        elif sorted_list[middle] > element_for_search:
            highest_elem = middle - 1
        elif sorted_list[middle] < element_for_search:
            lowest_elem = middle + 1
    return 'No such elem in list'


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = binary_search(a, 1)
print(b)
