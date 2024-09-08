"""
Топологическая сортировка - это пример использования поиска в глубину для упорядочивания вершин графа.
Граф ДОЛЖЕН быть ориентированным и ациклическим для корректной работы сортировки.
На основе сортировки вершины добавляются в список в порядке убывания временной метки ИССЛЕДОВАНИЯ вершины.

Граф для теста будет следующим (ацикличный ориентированный),
где символ "*" является частью ребра от вершины к вершине, а "←" - направление графа.:

 → ↓ ↗ ↓ ← ↙

underpants              socks
    *                     *
    ↓                     ↓         watch
trousers * * * * * * * → shoes
   *
   *         shirt
   *      *    *
   ↓  ↙        *
 belt          ↓
      *       tie
         *     *
           ↘   ↓
            blazer

Асимптоматическая скорость алгоритма составляет O(V + E), где V - количество вершин графа, а E - количество ребер,
поскольку именно такая сложность у поиска в глубину, а вставка узла в начало массива имеет асимптоматическую скорость
O(1).
"""


from typing import List, Any

from Algorithms_Construction_and_Analysis.Chapter_22_elementary_algorithms_with_graphs.colors import GraphNodeColors
from Algorithms_Construction_and_Analysis.Chapter_22_elementary_algorithms_with_graphs.depth_first_search import (
    GraphNode
)


class TopologicalGraphNode(GraphNode):

    def __init__(self, value: Any) -> None:
        super().__init__(value=value)
        self.neighbors: List[TopologicalGraphNode] = []

    def __str__(self) -> str:
        return f'{self.value} opened at {self.opening_time} and explored at {self.explored_time}'


class TopologicalSort:

    def __init__(self) -> None:
        self._sorted_nodes: List[TopologicalGraphNode] = []
        self._roots: List[TopologicalGraphNode] = []
        self._time: int = 0

    def sort(self, roots: List[TopologicalGraphNode]) -> None:
        self._time = 0  # Сбрасываем временные метки для каждого нового поиска
        self._roots = roots  # Не клонируем узлы, иначе один узел будет обработан несколько раз

        self._depth_first_search()

    def _depth_first_search(self) -> None:
        # Строим деревья поиска в глубину для всех вершин графа:
        for root in self._roots:
            if root.color == GraphNodeColors.WHITE:
                self._build_dfs_tree(node=root)

    def _build_dfs_tree(self, node: TopologicalGraphNode) -> None:
        # Отмечаем узел как открытый:
        self._time += 1
        node.opening_time = self._time
        node.color = GraphNodeColors.GREY

        # Рекурсивно углубляемся по ветку дерева для каждого ребра с соседним узлом для текущего,
        # если он еще не был открыт:
        for neighbor in node.neighbors:
            if neighbor.color == GraphNodeColors.WHITE:
                neighbor.distance_from_root = node.distance_from_root + 1
                neighbor.parent = node
                self._build_dfs_tree(node=neighbor)

        # Помечаем узел как изученный:
        self._time += 1
        node.explored_time = self._time
        node.color = GraphNodeColors.BLACK
        self._sorted_nodes.insert(0, node)

    def print_path(self) -> None:
        """
        Метод рекурсивно отрисовывает в консоль путь до искомого узла, если такой путь существует.

        :param node_to: Узел, к которому мы хотим найти путь.
        """

        for node in self._sorted_nodes:
            print(node)

    @property
    def sorted_nodes(self) -> List[TopologicalGraphNode]:
        return self._sorted_nodes


if __name__ == '__main__':
    # Creating graph nodes:
    underpants: TopologicalGraphNode = TopologicalGraphNode('underpants')  # трусы
    socks: TopologicalGraphNode = TopologicalGraphNode('socks')  # носки
    watch: TopologicalGraphNode = TopologicalGraphNode('watch')  # часы
    shoes: TopologicalGraphNode = TopologicalGraphNode('shoes')  # туфли
    trousers: TopologicalGraphNode = TopologicalGraphNode('trousers')  # брюки
    belt: TopologicalGraphNode = TopologicalGraphNode('belt')  # ремень
    shirt: TopologicalGraphNode = TopologicalGraphNode('shirt')  # рубашка
    tie: TopologicalGraphNode = TopologicalGraphNode('tie')  # галстук
    blazer: TopologicalGraphNode = TopologicalGraphNode('blazer')  # пиджак

    # Building our graph:
    underpants.neighbors = [trousers, shoes]
    socks.neighbors = [shoes]
    trousers.neighbors = [belt, shoes]
    shirt.neighbors = [tie, belt]
    tie.neighbors = [blazer]
    belt.neighbors = [blazer]

    topological_sort: TopologicalSort = TopologicalSort()
    # topological_sort.sort(roots=[shirt, watch, underpants, socks])
    topological_sort.sort(roots=[watch, socks, underpants, shirt])
    topological_sort.print_path()
