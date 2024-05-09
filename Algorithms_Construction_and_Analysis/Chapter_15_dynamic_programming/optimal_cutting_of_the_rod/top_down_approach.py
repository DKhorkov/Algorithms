"""
Является рекурсивным способом решения поставленной задачи.
"""

from typing import List


class TopDownApproach:

    def __init__(self, prices: List[int], rod_length: int) -> None:
        self._prices: List[int] = prices
        self._rod_length: int = rod_length

        """
        self._rod_length + 1 поскольку будет обращение по индексу 0 для остатка от стрежня длиной 0:
        
        Создаем базовое отрицательное значение выручки -1 для отрезка,
        поскольку выручка не может быть отрицательной. Если она отрицательна, 
        значит подзадача по вычислению выручки для данного отрезка еще не была решена.
        """
        self._revenue: List[int] = [-1] * (self._rod_length + 1)
        self._sections: List[int] = [0] * (self._rod_length + 1)

    def estimate(self) -> None:
        self._cut_the_rod(road_length=self._rod_length)
        print(f'Max revenue is {self._revenue[-1]}')
        temp = self._rod_length
        cut_counter: int = 1
        while temp:
            print(f'{cut_counter} cut - {self._sections[temp]}')
            temp -= self._sections[temp]
            cut_counter += 1

    def _cut_the_rod(self, road_length: int) -> int:
        # Последний элемент всегда является ответом, какая прибыль максимальна:
        if self._revenue[road_length] >= 0:
            return self._revenue[road_length]

        if road_length == 0:
            revenue: int = 0
        else:
            revenue: int = -1

            # Проходимся по всем способам создания отрезка из первоначального стержня:
            for cut in range(1, road_length + 1):  # self._rod_length + 1 для обработки всего массива

                """
                Рекурсивно проходимся по всем способам выбрать отрезок от остатка стержня, 
                после того как был выбран первый отрезок, чтобы получить его максимальную выручку.
                """
                sub_revenue = self._cut_the_rod(road_length=road_length - cut)

                """
                self._prices[cut - 1], поскольку выручка хранит в себе значения по размеру отрезка, то есть 
                нулевого отрезка в ней нет.
                """
                if revenue < (self._prices[cut - 1] + sub_revenue):
                    revenue = self._prices[cut - 1] + sub_revenue
                    self._sections[road_length] = cut

        # Сохраняем максимальную выручку для выбранного отрезка
        self._revenue[road_length] = revenue
        return revenue


if __name__ == '__main__':
    top_down_approach: TopDownApproach = TopDownApproach([1, 5, 8, 9, 10, 17, 17, 20, 24, 30], 5)
    top_down_approach.estimate()
