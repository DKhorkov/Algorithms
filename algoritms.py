def buble(lst):
    swap = True
    while swap:
        swap = False
        for i in range(len(lst) - 1):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                swap = True


lst = [4, 3, 3, 44, 1, 5, 22, 2]
print(lst)
# buble(lst)
# print(lst)


def selection(lst):
    for i in range(len(lst)):
        lowest = i
        for j in range(i + 1, len(lst)):  # i+1, чтобы ускорить алгоритм и перебирать меньше значений списка.
            if lst[j] < lst[lowest]:
                lowest = j
        lst[i], lst[lowest] = lst[lowest], lst[i]


# selection(lst)
# print(lst)


def insertion(lst):
    for i in range(1, len(lst)):  # Первый считаем изначально отсортированным
        item_to_copy = lst[i]
        previous_item_index = i - 1
        while previous_item_index >= 0 and lst[previous_item_index] > item_to_copy:
            lst[previous_item_index + 1] = lst[previous_item_index]
            previous_item_index -= 1
        lst[previous_item_index + 1] = item_to_copy


# insertion(lst)
# print(lst)


def merge_sorting(lst):
    if len(lst) == 1:
        return lst
    middle = len(lst) // 2
    left_part = merge_sorting(lst[: middle])
    right_part = merge_sorting(lst[middle:])
    return unite_lists(left_part, right_part)


def unite_lists(left, right):
    new_list = []

    # Переключатели:
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            new_list.append(right[j])
            j += 1
        else:
            new_list.append(left[i])
            i += 1
    if i == len(left):
        new_list += right[j:]
    elif j == len(right):
        new_list += left[i:]
    return new_list


# print(merge_sorting(lst))


def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    middle = lst[len(lst) // 2]
    left_part = list(filter(lambda x: x < middle, lst))
    center = [i for i in lst if i == middle]
    right_part = list(filter(lambda x: x > middle, lst))
    return quick_sort(left_part) + center + quick_sort(right_part)


lst2 = [7, 2, 5, 2, 4, 9]
print(lst2)
print(quick_sort(lst2))