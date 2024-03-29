"""
Найти матрицу C равную произведению матриц A =
4	2
9	0
  и B =
3	1
-3	4 =
6	12
27	9

Элементы матрицы C вычисляются следующим образом:

c11 = a11·b11 + a12·b21 = 4·3 + 2·(-3) = 12 - 6 = 6

c12 = a11·b12 + a12·b22 = 4·1 + 2·4 = 4 + 8 = 12

c21 = a21·b11 + a22·b21 = 9·3 + 0·(-3) = 27 + 0 = 27

c22 = a21·b12 + a22·b22 = 9·1 + 0·4 = 9 + 0 = 9
"""

from typing import List


def square_matrix_multiplying(a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
    """
    Поскольку для умножения матриц количество столбцов первой матрицы должно равняться количеству строк второй,
    то можем вычислить n как длина первой матрицы.

    Скорость роста алгоритма O(n^3).
    """

    n: int = len(a)

    # Создаем пустую матрицу, чтобы корректно работать с индексами в ходе перемножения двух матриц:
    new_matrix: List[List[int]] = [
        [
            0 for _ in range(n)
        ] for _ in range(n)
    ]

    for i in range(n):  # Для каждого столбца первой матрицы
        for j in range(n):  # Для каждой строки второй матрицы
            for k in range(n):  # Вводим новую переменную k для корректного перемножения столбцов на строки
                new_matrix[i][j] += a[i][k] * b[k][j]

    return new_matrix


if __name__ == '__main__':
    a: List[List[int]] = [
        [4, 2],
        [9, 0]
    ]

    b: List[List[int]] = [
        [3, 1],
        [-3, 4]
    ]

    c: List[List[int]] = square_matrix_multiplying(a=a, b=b)
    print(c)
