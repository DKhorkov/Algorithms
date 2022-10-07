def quick_sort(list_of_num):
    if len(list_of_num) <= 1:
        return list_of_num
    separator = list_of_num[len(list_of_num) // 2]  # Тут нам нужно именно значение из входящего списка
    left_part = list(filter(lambda x: x < separator, list_of_num))
    middle = [x for x in list_of_num if x == separator]
    right_part = list(filter(lambda x: x > separator, list_of_num))
    return quick_sort(left_part) + middle + quick_sort(right_part)


list_of_numbers = [5, 1, 4, 0, 2, 2, 8, 6]
print(list_of_numbers)
print(quick_sort(list_of_numbers))