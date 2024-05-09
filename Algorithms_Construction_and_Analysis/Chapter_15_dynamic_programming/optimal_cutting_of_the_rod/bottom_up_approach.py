"""
Является решением поставленной задачи с помощью цикла и зачастую обладает лучшими константными множителями за счет
отсутствия более дорогостоящих вызовов рекурсивных функций.
"""

from typing import List


class BottomUpApproach:

    def __init__(self, prices: List[int], rod_length: int) -> None:
        self._prices: List[int] = prices
        self._rod_length: int = rod_length

        # self._rod_length + 1 поскольку будет обращение по индексу 0 для остатка от стрежня длиной 0:
        self._revenue: List[int] = [0] * (self._rod_length + 1)
        self._sections: List[int] = [0] * (self._rod_length + 1)

    def estimate(self) -> None:
        self._cut_the_rod()

        # Последний элемент всегда является ответом, какая прибыль максимальна
        print(f'Max revenue is {self._revenue[-1]}')

        temp = self._rod_length
        cut_counter: int = 1
        while temp:
            print(f'{cut_counter} cut - {self._sections[temp]}')
            temp -= self._sections[temp]
            cut_counter += 1

    def _cut_the_rod(self) -> None:
        # Проходимся по всем способам создания отрезка из первоначального стержня:
        for cut in range(1, self._rod_length + 1):  # self._rod_length + 1 для обработки всего массива
            """
            Создаем базовое отрицательное значение выручки -1 для отрезка,
            поскольку выручка не может быть отрицательной. Если она отрицательна, 
            значит подзадача по вычислению выручки для данного отрезка еще не была решена.
            """
            revenue = -1

            # Проходимся по всем способам выбрать отрезок от остатка стержня, после того как был выбран первый отрезок:
            for sub_cut in range(1, cut + 1):  # cut + 1 для обработки граничного случая
                """
                Проверяем, является ли разбиение остатка отрезка после выбора первого отрезка оптимальным с точки 
                зрения выручки. Таким образом мы найдем максимальную выручку для первого выбранного отрезка,
                а также запомним, каким будет оптимальный отрезок.
                
                self._prices[sub_cut - 1], поскольку выручка хранит в себе значения по размеру отрезка, то есть 
                нулевого отрезка в ней нет.
                """
                if revenue < (self._prices[sub_cut - 1] + self._revenue[cut - sub_cut]):
                    revenue = self._prices[sub_cut - 1] + self._revenue[cut - sub_cut]
                    self._sections[cut] = sub_cut

            # Сохраняем максимальную выручку для выбранного отрезка
            self._revenue[cut] = revenue


if __name__ == '__main__':
    bottom_up_approach: BottomUpApproach = BottomUpApproach([1, 5, 8, 9, 10, 17, 17, 20, 24, 30], 7)
    bottom_up_approach.estimate()
