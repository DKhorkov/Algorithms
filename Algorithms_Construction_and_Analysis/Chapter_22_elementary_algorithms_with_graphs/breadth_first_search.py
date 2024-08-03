"""
Поиск в ширину - это алгоритм для работы с ориентированными и неориентированными невзвешенными графами для нахождения
кратчайшего пути и смежных задач. Кратчайший путь находится путем обработки ближайших соседей один раз и
пометки каждого узла, если тот был обработан. Таким образом каждый узел обрабатывается единожды и путь до него от
вершины будет всегда вычислен корректно.

Граф для теста будет следующим, где символ "*" является частью ребра от вершины к вершине:

4 * * * 2 * * * 5 * * * 3
*    *    *
* *           *
1 * * * 7 * * * 6
"""


from __future__ import annotations
from copy import deepcopy
from typing import List, Protocol, Any, Optional
from enum import Enum
from queue import Queue


class GraphNodeColors(str, Enum):
    """
    Цвета узлов графа не являются обязательными, однако используются для упрощения понимания.
    """

    WHITE = 'white'  # Узел графа не открыт
    GREY = 'grey'  # Узел графа открыт, но не исследован
    BLACK = 'black'  # Узел графа исследован


class Prototype(Protocol):
    """
    Используем паттерн Прототип, чтобы не изменять полученные графы, а работать с их копиями.
    """

    def clone(self) -> Any:
        raise NotImplementedError


class GraphNode:

    def __init__(self, value: int) -> None:
        self.value: int = value
        self.distance_from_root: int = 0
        self.parent: Optional[GraphNode] = None
        self.neighbors: List[GraphNode] = []
        self.color: GraphNodeColors = GraphNodeColors.WHITE

    def clone(self) -> GraphNode:
        return deepcopy(self)

    def __eq__(self, other: GraphNode) -> bool:
        return self.value == other.value

    def __str__(self) -> str:
        return f'Node with value={self.value} and distance from root={self.distance_from_root}'


class BreadthFirstSearch:

    def __init__(self) -> None:
        self._root: Optional[GraphNode] = None
        self._node_to: Optional[GraphNode] = None
        self._queue: Queue = Queue()

    def breadth_first_search(self, graph: GraphNode, node_to: GraphNode) -> None:
        self._root: GraphNode = graph.clone()
        self._node_to: GraphNode = node_to.clone()
        self._build_bfs_tree()
        self._print_path()

    def _build_bfs_tree(self) -> None:
        # Обозначаем корень графа как открытый, но не исследованный узел:
        self._root.color = GraphNodeColors.GREY
        self._queue.put(self._root)

        # Пока очередь не пуста - есть узлы для изучения, а если найден искомый узел, значит известен и путь до него,
        # а дальнейшее построение дерева не имеет смысла:
        node_to_found: bool = False
        while not self._queue.empty() and not node_to_found:
            node: GraphNode = self._queue.get()
            for neighbor in node.neighbors:
                # Если узел еще не открыт, то открываем его и добавляем в очередь на исследование.
                # Под исследованием понимается открытие его соседей, если они еще не были открыты,
                # а также обновление дистанции от корня до узла
                if neighbor.color == GraphNodeColors.WHITE:
                    neighbor.color = GraphNodeColors.GREY
                    neighbor.distance_from_root = node.distance_from_root + 1
                    neighbor.parent = node

                    # Если найден искомый узел:
                    if neighbor == self._node_to:
                        self._node_to = neighbor
                        node_to_found = True
                        break  # Прерываем цикл for

                    self._queue.put(neighbor)

            node.color = GraphNodeColors.BLACK  # Помечаем узел как изученный

    def _print_path(self, node_to: Optional[GraphNode] = None) -> None:
        """
        Метод рекурсивно отрисовывает в консоль путь до искомого узла, если такой путь существует.

        :param node_to:
        """

        # По дефолту - начинаем с искомого узла:
        if not node_to:
            print(f'Way from node with value={self._root.value} to node with value={self._node_to.value}:\n')
            node_to = self._node_to

        if self._root == node_to:  # Искомый узел и есть корневой
            print(self._root)

        # Если у искомого узла нет родителя и он не корневой, значит он не был исследован в ходе метода
        # self._build_bfs_tree, а значит не имеет отношения к данному графу
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
    seven: GraphNode = GraphNode(7)

    # Building our graph:
    four.neighbors = [one, two]
    one.neighbors = [four, two, seven]
    two.neighbors = [four, one, five, six]
    five.neighbors = [two, three]
    three.neighbors = [five]
    seven.neighbors = [one, six]
    six.neighbors = [seven, two]

    bfs: BreadthFirstSearch = BreadthFirstSearch()
    bfs.breadth_first_search(graph=four, node_to=three)

    print('\n\n')
    bfs.breadth_first_search(graph=one, node_to=six)
