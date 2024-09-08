"""
Алгоритм Беллмана-Форда решает задачу о кратчайшем пути из одной вершины в общем случае,
когда вес каждого из рёбер может быть отрицательным. Для заданного взвешенного ориентированного графа
с истоком в указанной вершине алгоритм возвращает логическое значение. Это логическое значение указывает,
содержится ли в графе цикл с отрицательным весом, достижимый из истока. Если такой цикл существует,
алгоритм указывает, что решение не существует. Если же таких циклов нет, алгоритм выдает кратчайшие пути и их веса.

Граф для теста будет следующим (цикличный ориентированный взвешенный),
где символ "*" является частью ребра от вершины к вершине, "←" - направление графа,
а цифры - стоимость перемещения по ребру между узлами:

          * * * * * * * *
        *                 *
        *  * * 5 * * ↘     *
         T             X    ↘
       ↗   ↖ * -2 * *   ↖    *
    6    *           ↗    *   *
  *      *         *      *  -4
S        8      -3        7   *
↑  *     *     *          *   ↓
*    7   *   *            *   *
 *    ↘  ↓ *             *   *
   *     Y * * 9 * * → Z ← *
     *               *
       * * * 2 * * *

Асимптоматическая скорость алгоритма составляет O(VE), где V - количество вершин графа, а E - количество ребер.
"""


from typing import List

from Algorithms_Construction_and_Analysis.Chapter_24_shortest_paths_from_one_vertex.base_algorithm import (
    ShortestPathsFromOneVertexBaseAlgorithm
)
from Algorithms_Construction_and_Analysis.Chapter_24_shortest_paths_from_one_vertex.node import GraphNode, GraphEdge


class BellmanFordAlgorithm(ShortestPathsFromOneVertexBaseAlgorithm):

    def process_graph(self, roots: List[GraphNode], source_node: GraphNode) -> bool:
        """
        Обрабатывает граф для поиска кратчайших путей ко всем узлам от исходного узла.
        Также проверяет существование цикла отрицательным весом. Если такой цикл существует,
        возвращает True, в противном случае возвращает False.
        """

        self._roots = roots
        self._source_node = source_node

        self._init_single_source()
        self._get_all_edges()

        for _ in range(len(self._roots)):
            for edge in self._edges:
                self._relax(edge=edge)

        for edge in self._edges:
            if edge.node_to.shortest_path_estimate > edge.node_from.shortest_path_estimate + edge.cost:
                return True

        return False


if __name__ == '__main__':
    # Create nodes:
    s: GraphNode = GraphNode('s')
    t: GraphNode = GraphNode('t')
    y: GraphNode = GraphNode('y')
    x: GraphNode = GraphNode('x')
    z: GraphNode = GraphNode('z')

    # Create edges:
    s.edges = [
        GraphEdge(node_from=s, node_to=t, cost=6),
        GraphEdge(node_from=s, node_to=y, cost=7),
    ]

    t.edges = [
        GraphEdge(node_from=t, node_to=z, cost=-4),
        GraphEdge(node_from=t, node_to=x, cost=5),
        GraphEdge(node_from=t, node_to=y, cost=8),
    ]

    y.edges = [
        GraphEdge(node_from=y, node_to=z, cost=9),
        GraphEdge(node_from=y, node_to=x, cost=-3),
    ]

    x.edges = [
        GraphEdge(node_from=x, node_to=t, cost=-2),
    ]

    z.edges = [
        GraphEdge(node_from=z, node_to=x, cost=7),
        GraphEdge(node_from=z, node_to=s, cost=2),
    ]

    bellman_ford_algorithm: BellmanFordAlgorithm = BellmanFordAlgorithm()
    circle: bool = bellman_ford_algorithm.process_graph(
        source_node=s,
        roots=[s, t, y, x, z]
    )

    if not circle:
        bellman_ford_algorithm.print_shortest_path(node_to=x)
        bellman_ford_algorithm.print_shortest_path(node_to=t)
        bellman_ford_algorithm.print_shortest_path(node_to=z)
    else:
        print(f'There is no shortest path source node to any other node due to negative weighted cycle')
