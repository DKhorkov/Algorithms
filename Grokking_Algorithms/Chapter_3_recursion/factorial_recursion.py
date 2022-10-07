def factorial(number):
    """Вычисляет факториал заданного числа"""
    if number == 1:
        return number  # Выход из рекурсии
    else:
        return number * factorial(number - 1)


num = 100  # При 1000 будет превышение глубины рекурсии и трассировка об этом.
result = factorial(num)
print(f'{num}! = {result:,d}')
