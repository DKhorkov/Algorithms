def buble(lst):
    swap = True
    while swap:
        swap = False
        for i in range(len(lst) - 1):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                swap = True


lst = [4, 2, 5, 1]
print(lst)
# buble(lst)
# print(lst)


def selection(lst):
    for i in range(len(lst)):
        lowest = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[lowest]:
                lowest = j
        lst[i], lst[lowest] = lst[lowest], lst[i]


# selection(lst)
# print(lst)


def insertion(lst):
    for i in range(1, len(lst)):  # первый считаем отсортированным
        item_to_insert = lst[i]  # сохраняем анализируемый элемент списка
        previous_elem_index = i - 1  # смотрим элемент слева
        while previous_elem_index >= 0 and lst[previous_elem_index] > item_to_insert:  # проверка индекса на работоспособность
            # плюс если элемент слева больше проверяемого
            lst[previous_elem_index + 1] = lst[previous_elem_index]  # записываем на место проверяемое этот элемент
            previous_elem_index -= 1  # уменьшаем на один индекс, чтобы посмотреть следующий эдлемент слева
        lst[previous_elem_index + 1] = item_to_insert  # плюсуем к индексу один, ибо вычитали его в цикле
        # и заменяем на проверяемый элемент


# insertion(lst)
# print(lst)


def merge(left, right):
    lst = []
    a = b = 0
    while a < len(left) and b < len(right):
        if left[a] > right[b]:
            lst.append(right[b])
            b += 1
        else:
            lst.append(left[a])
            a += 1
    if a == len(left):
        lst += right[b:]
    elif b == len(right):
        lst += left[a:]
    return lst


def sliyanie(lst):
    if len(lst) <= 1:
        return lst
    middle = len(lst) // 2
    left = sliyanie(lst[:middle])
    right = sliyanie(lst[middle:])
    return merge(left, right)


# print(sliyanie(lst))


def quick(lst):
    if len(lst) <= 1:
        return lst
    elem = lst[len(lst) // 2]
    left = list(filter(lambda x: x < elem, lst))  # тут нужно именно функцию list использовать, а не []
    center = [i for i in lst if i == elem]
    right = list(filter(lambda x: x > elem, lst))  # тут нужно именно функцию list использовать, а не []
    return quick(left) + center + quick(right)


print(quick(lst))


def generator(lst):
    for i in lst:
        yield i


gen = generator(lst)
print(type(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))


class MyIterator:

    def __init__(self, num_iters):
        self.num_iters = num_iters
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.num_iters:
            self.count += 1
            print(f"Iteration for {self.count} time.")
        else:
            raise StopIteration


iterator = MyIterator(5)
print(type(iterator))
next(iterator)
next(iterator)
next(iterator)
next(iterator)
next(iterator)

user_is_logged_in = True


def decorator(func):

    def wrapper(*args, **kwargs):
        if user_is_logged_in:
            return func(*args, **kwargs)
        raise Exception("You haven't been logged in!")

    return wrapper


@decorator
def greet_user(username):
    print(f'Hello, {username}!')


greet_user('Dima')


g = dict(name=2)
g['male'] = 3
tpl = ('n', 'sn')
lst = [1, 2]
g[tpl] = 4
print(g)
tp = (1, g)
print(tp)
print(tpl[:1])

# компрехеншены в питоне + списковый, что само собой понятно!
dct = {key: value for key, value in zip(('name', 's'), (1, 2))}
print(dct)
set_compr = {x * 2 for x in list(range(5))}
print(set_compr)

# лямбда функция для фильтрации словаря:
dict_for_filtration = {key: value for key, value in zip('abcd', (1, 2, 3, 4))}
print(dict(filter(lambda x: x[1] > 2, dict_for_filtration.items())))

# функция map:
ref = list(map(lambda x: x * 2, [1, 2, 3, 4]))
print(ref)


# функция enumerate:
for count, value in enumerate([9, 8, 7, 6], start=1):
    print(f'{count}) {value}')

    