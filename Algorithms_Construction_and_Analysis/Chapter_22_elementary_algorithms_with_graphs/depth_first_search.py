"""
Поиск в ширину - это алгоритм для работы с ориентированными и неориентированными, цикличными и ацикличными
невзвешенными графами для нахождения. Как правило, данный алгоритм используется как подспорье или ядро в
других алгоритмах, связанных с графами. Алгоритм также может быть использован для нахождения пути до искомого узла.

ОДНАКО путь не всегда будет кратчайшим. Все зависит от порядка вершин, которые будут переданы в алгоритм для
обработки путей от этих вершин. Поскольку каждая вершина обрабатывается лишь единожды, то в случае, когда сначала
будет построено более глубокое поддерево поиска, то путь до вершины в этом дереве будет НЕ кратчайшим, если вершина
также доступна из другого поддерева, но уже не будет в нем, поскольку была обработана.

Граф для теста будет следующим (цикличный ориентированный),
где символ "*" является частью ребра от вершины к вершине, а "←" - направление графа.:

4 * * → 2       5
*    ↗  *     * *
↓ *     ↓  ↙    ↓
1 ← * * 3       6  ←  *
                *     *
                *  *  *

Асимптоматическая скорость алгоритма составляет O(V + E), где V - количество вершин графа, а E - количество ребер.
"""


from __future__ import annotations
from copy import deepcopy
from typing import List, Optional, Set

from Algorithms_Construction_and_Analysis.Chapter_22_elementary_algorithms_with_graphs.colors import GraphNodeColors


class GraphNode:

    def __init__(self, value: int) -> None:
        self.value: int = value
        self.distance_from_root: int = 0
        self.parent: Optional[GraphNode] = None
        self.neighbors: List[GraphNode] = []
        self.color: GraphNodeColors = GraphNodeColors.WHITE

        # Временные метки, которые могут быть полезны при использовании алгоритма поиска в глубину:
        self.opening_time: int = 0
        self.explored_time: int = 0

    def clone(self) -> GraphNode:
        return deepcopy(self)

    def __eq__(self, other: GraphNode) -> bool:
        return self.value == other.value

    def __hash__(self) -> int:
        return hash(self.value)

    def __str__(self) -> str:
        return (f'Node with value={self.value} and distance from root={self.distance_from_root}, '
                f'which was opened at {self.opening_time} time and explored at {self.explored_time} time')


class DepthFirstSearch:

    def __init__(self) -> None:
        self._roots: List[GraphNode] = []
        self._node_to: Optional[GraphNode] = None
        self._time: int = 0
        self._node_found: bool = False

    def depth_first_search(self, roots: List[GraphNode], node_to: GraphNode) -> None:
        self._time = 0  # Сбрасываем временные метки для каждого нового поиска
        self._roots = [root.clone() for root in roots]
        self._node_to = node_to.clone()

        # Строим деревья поиска в глубину для всех вершин графа:
        for root in self._roots:
            if root.color == GraphNodeColors.WHITE:
                self._build_dfs_tree(node=root)

            # Если найден искомый узел, то продолжать строить деревья поиска в глубину и
            # дальше открывать граф нет смысла, иначе некоторые узлы могут быть обработаны повторно:
            if self._node_found:
                break

        self._print_path()

    def _build_dfs_tree(self, node: GraphNode) -> None:
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

                # Если найден искомый узел, то продолжать строить деревья поиска в глубину и
                # дальше открывать граф нет смысла, иначе некоторые узлы могут быть обработаны повторно:
                if neighbor == self._node_to:
                    self._node_to = neighbor
                    self._node_found = True
                    break

        # Помечаем узел как изученный:
        self._time += 1
        node.explored_time = self._time
        node.color = GraphNodeColors.BLACK

    def _print_path(self, node_to: Optional[GraphNode] = None) -> None:
        """
        Метод рекурсивно отрисовывает в консоль путь до искомого узла, если такой путь существует.

        :param node_to: Узел, к которому мы хотим найти путь.
        """

        # По дефолту - начинаем с искомого узла:
        if not node_to:
            print(f'Way to node with value={self._node_to.value}:\n')
            node_to = self._node_to

        if node_to in self._roots:  # Искомый узел и есть корневой
            print(node_to)

        # Если у искомого узла нет родителя и он не корневой, значит он не был исследован в ходе метода
        # self._build_dfs_tree, а значит не имеет отношения к данному графу
        elif not node_to.parent:
            print(f'There is no way from root to provided node')
        else:
            # Рекурсивно ищем путь от родителя искомого узла (он ближе к коню) к корню, чтобы соблюсти порядок шагов
            # от корня к искомому узлу
            self._print_path(node_to=node_to.parent)
            print(node_to)


if __name__ == '__main__':
    # Creating graph nodes:
    one: GraphNode = GraphNode(1)
    two: GraphNode = GraphNode(2)
    three: GraphNode = GraphNode(3)
    four: GraphNode = GraphNode(4)
    five: GraphNode = GraphNode(5)
    six: GraphNode = GraphNode(6)

    # Building our graph:
    one.neighbors = [two]
    two.neighbors = [three]
    three.neighbors = [one]
    four.neighbors = [one, two]
    five.neighbors = [six, three]
    six.neighbors = [six]

    dfs: DepthFirstSearch = DepthFirstSearch()
    dfs.depth_first_search(roots=[four, five], node_to=three)

    print('\n\n')
    dfs.depth_first_search(roots=[five, four], node_to=three)
