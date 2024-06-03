from typing import Dict, Optional

from Algorithms_Construction_and_Analysis.Chapter_15_dynamic_programming.longest_common_subsequence.longest_common_subsequence import \
    LongestCommonSubsequenceEstimator


class OptimizedLCSEstimator(LongestCommonSubsequenceEstimator):

    def __init__(self, first_sequence: str, second_sequence: str) -> None:
        self._first_sequence: str = first_sequence
        self._second_sequence: str = second_sequence

        # Таблица со значениями длин совпадающих подпоследовательностей
        self._length_table: Dict[str, int] = {}

        self._fill_length_table()

    def _calculate_lcs_length(self) -> None:
        """
        Избавляемся от таблицы направлений по сравнению с изначальной версией алгоритма.
        """

        for i in range(1, len(self._first_sequence) + 1):
            for j in range(1, len(self._second_sequence) + 1):
                if self._first_sequence[i - 1] == self._second_sequence[j - 1]:
                    self._length_table[f'{i}{j}'] = self._length_table[f'{i - 1}{j - 1}'] + 1
                elif self._length_table[f'{i - 1}{j}'] >= self._length_table[f'{i}{j - 1}']:
                    self._length_table[f'{i}{j}'] = self._length_table[f'{i - 1}{j}']
                else:
                    self._length_table[f'{i}{j}'] = self._length_table[f'{i}{j - 1}']

    def _build_lcs(self, i: Optional[int] = None, j: Optional[int] = None) -> str:
        """
        Реализация задания 15.4.2 - оптимизация алгоритма с точки зрения памяти за счет удаления таблицы с
        направлениями.
        """

        if i is None:
            i = len(self._first_sequence)

        if j is None:
            j = len(self._second_sequence)

        lcs = ''
        if self._length_table[f'{i}{j}'] == 0:
            return lcs

        if self._first_sequence[i - 1] == self._second_sequence[j - 1]:
            # Найденный элемент возвращается после вызова рекурсии для корректного отображения LCS
            return self._build_lcs(i=i - 1, j=j - 1) + self._first_sequence[i - 1]
        elif self._length_table[f'{i - 1}{j}'] > self._length_table[f'{i}{j - 1}']:
            return self._build_lcs(i=i - 1, j=j)
        else:
            return self._build_lcs(i=i, j=j - 1)


if __name__ == '__main__':
    first_sequence = 'sbgtfrt'
    second_sequence = 'qsotlr'
    lcs_estimator: OptimizedLCSEstimator = OptimizedLCSEstimator(first_sequence, second_sequence)
    lcs: str = lcs_estimator.estimate_lcs()
    print(lcs)
