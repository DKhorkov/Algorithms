from typing import Dict, Optional

from Algorithms_Construction_and_Analysis.Chapter_15_dynamic_programming.longest_common_subsequence.constants import (
    LCSDirections
)


"""
Подпоследовательность можно получить из некоторой конечной последовательности, если удалить из последней некоторое 
множество её элементов (возможно пустое). 
Например, BCDB является подпоследовательностью последовательности ABCDBAB. 
Будем говорить, что последовательность Z является общей подпоследовательностью последовательностей X и Y, 
если Z является подпоследовательностью как X, так и Y. 
Требуется для двух последовательностей X и Y найти общую подпоследовательность наибольшей длины. 
Заметим, что НОП может быть несколько.

Обратите внимание! Подпоследовательность отличается от подстроки. 
Например, если есть исходная последовательность "ABCDEF", то "ACE" будет подпоследовательностью, но не подстрокой, 
а "ABC" будет как подпоследовательностью, так и подстрокой. 

Решение задачи нахождения наидлиннейшей общая подпоследовательность в лоб будет иметь асимптоматическую скорость
O(n ^ m), где m - длина наибольшей из двух последовательностей. Такая скорость обусловлена тем, что у каждой строки 
имеется 2 ^ n (где n - длина строки) возможный подпоследовательностей, которые будут сравниваться в лоб с 
подпоследовательностями второй строки.

Однако за счет наличия оптимальной подструктуры (в данном случае табличного сохранения результатов), а также 
перекрывающихся подзадач, данная задача может быть решена с помощью динамического программирования и иметь 
линейную асимптоматическую скорость O(n * m), где n - длина первой строки, а m - длина второй строки.
"""


class LongestCommonSubsequenceEstimator:

    def __init__(self, first_sequence: str, second_sequence: str) -> None:
        self._first_sequence: str = first_sequence
        self._second_sequence: str = second_sequence

        # Таблица со значениями длин совпадающих подпоследовательностей
        self._length_table: Dict[str, int] = {}

        # Таблица с направлениями для нахождения наибольшей общей подпоследовательности
        self._direction_table: Dict[str, str] = {}

        self._fill_length_table()

    def _fill_length_table(self) -> None:
        """
        Создаем заготовку таблицы, чтобы потом обращаться по индексам.
        """

        for i in range(len(self._first_sequence) + 1):
            self._length_table[f'{i}0'] = 0

        for j in range(len(self._second_sequence) + 1):
            self._length_table[f'0{j}'] = 0

    def estimate_lcs(self) -> str:
        self._calculate_lcs_length()
        return self._build_lcs()

    def _calculate_lcs_length(self) -> None:
        """
        Проходимся по каждой из последовательностей и:

        Если текущий элемент первой последовательности равен текущему
        элементу второй последовательности, значит наидлиннейшая общая подпоследовательность равна количеству совпавших
        ранее элементов + 1 (текущий);

        В противном случае для ячейки в таблице длин общих подпоследовательностей для индекса i (элемента первой
        подпоследовательности) и индекса j (элемента второй подпоследовательности) выбирается наибольшая длина общей
        подпоследовательности, вычисленная на предыдущих итерациях.
        """
        for i in range(1, len(self._first_sequence) + 1):
            for j in range(1, len(self._second_sequence) + 1):
                if self._first_sequence[i - 1] == self._second_sequence[j - 1]:
                    self._length_table[f'{i}{j}'] = self._length_table[f'{i - 1}{j - 1}'] + 1
                    self._direction_table[f'{i}{j}'] = LCSDirections.TOP_LEFT
                elif self._length_table[f'{i - 1}{j}'] >= self._length_table[f'{i}{j - 1}']:
                    self._length_table[f'{i}{j}'] = self._length_table[f'{i - 1}{j}']
                    self._direction_table[f'{i}{j}'] = LCSDirections.TOP
                else:
                    self._length_table[f'{i}{j}'] = self._length_table[f'{i}{j - 1}']
                    self._direction_table[f'{i}{j}'] = LCSDirections.LEFT

    def _build_lcs(self, i: Optional[int] = None, j: Optional[int] = None) -> str:
        """
        Проходимся по таблице с направлениями в восходящем направлении. Поскольку мы сохраняли в методе
        self._calculate_lcs_length() совпадающие элементы обеих последовательностей под направлением
        LCSDirections.TOP_LEFT, то при его определении в таблице направлений мы будем возвращать данный совпадающий
        элемент.
        """

        if i is None:
            i = len(self._first_sequence)

        if j is None:
            j = len(self._second_sequence)

        lcs = ''
        if i == 0 or j == 0:
            return lcs

        if self._direction_table[f'{i}{j}'] == LCSDirections.TOP_LEFT:
            # Найденный элемент возвращается после вызова рекурсии для корректного отображения LCS
            return self._build_lcs(i=i - 1, j=j - 1) + self._first_sequence[i - 1]
        elif self._direction_table[f'{i}{j}'] == LCSDirections.TOP:
            return self._build_lcs(i=i - 1, j=j)
        else:
            return self._build_lcs(i=i, j=j - 1)


if __name__ == '__main__':
    first_sequence = 'sbgtfrt'
    second_sequence = 'qsotlr'
    lcs_estimator: LongestCommonSubsequenceEstimator = LongestCommonSubsequenceEstimator(first_sequence, second_sequence)
    lcs: str = lcs_estimator.estimate_lcs()
    print(lcs)
