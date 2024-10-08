def selection_search(lst):
    """Алгоритм сортировки выборкой, скорость работы алгоритма О(n^2)"""
    for i in range(len(lst)):
        lowest = i
        for j in range(i + 1, len(lst)):
            if lst[lowest] > lst[j]:
                lowest = j
        lst[lowest], lst[i] = lst[i], lst[lowest]


a = [5, 3, 6, 2, 7, 1, 0, 15, 22, 4, 11]
print(a)
selection_search(a)
print(a)
