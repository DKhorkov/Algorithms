"""Задача найти самый быстрый путь от старта до финиша"""


class Dijkstras:

    def __init__(self):

        # Создаем граф с расценкой каждого ребра. Ребра не могут быть отрицательными, а граф без циклов и направленный:
        self.graph = {'start': {'a': 6, 'b': 2, 'c': 7},
                      'a': {'finish': 5,  'c': 1},
                      'b': {'finish': 10, 'c': 4},
                      'c': {'finish': 3},
                      'finish': {}}
        self.costs = {'a': 6, 'b': 2, 'c': 7, 'finish': float('inf')}  # Создаем таблицу стоимости
        self.parents = {'a': 'start', 'b': 'start', 'c': 'start', 'finish': None}  # Создаем таблицу родителей пути
        self.proceed = []  # Создаем список обработанных узлов

    def find_lowest_cost(self):
        """Находим самый дешевый узел и добавляем возвращаем ключ с самым дешевым значением ребра"""
        lowest_cost = float('inf')  # Определяем изначально самое дешевое ребро, так сказать
        lowest_cost_node = None  # Определяем ключ самого дешевого ребра
        for elem in self.costs:  # Перебираем все ребра
            # Если дешевле отсмотренных и не проверены ранее, то изменяем данные:
            if self.costs[elem] < lowest_cost and elem not in self.proceed:
                lowest_cost = self.costs[elem]
                lowest_cost_node = elem
        return lowest_cost_node

    def main(self):
        """Основная функция алгоритма"""
        current_node = self.find_lowest_cost()  # Получаем текущее самое дешевое ребро
        while current_node is not None:  # Если оно существует (не все ребра обработаны):
            cost = self.costs[current_node]  # Берем стоимость до текущего ребра
            neighbors = self.graph[current_node]  # И всех его соседей
            for neighbor in neighbors:  # Для каждого соседа
                new_cost = cost + neighbors[neighbor]  # Рассчитываем новую стоимость до него
                if self.costs[neighbor] > new_cost:  # Если стоимость до соседа была дороже новой
                    self.costs[neighbor] = new_cost  # Меняем стоимость этого соседа
                    self.parents[neighbor] = current_node  # Добавляем в родители соседу текущее ребро
            self.proceed.append(current_node)  # Говорим, что проверили полностью текущее ребро
            current_node = self.find_lowest_cost()  # И ищем новое самое дешевое ребро
        print(f"Самый дешевый путь: {self.get_way()} со стоимостью {self.costs['finish']}")

    def get_way(self):
        """Воссоздаем путь от начала до конца"""
        last_way_point = 'finish'
        way = 'finish'
        while True:
            try:
                last_way_point = self.parents[last_way_point]
            except KeyError:
                break
            else:
                way = last_way_point + "-" + way
        return way


if __name__ == '__main__':
    alr = Dijkstras()
    alr.main()
