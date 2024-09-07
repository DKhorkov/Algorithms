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

    def check_negative_weight_cycle_existence(self, roots: List[GraphNode], source_node: GraphNode) -> bool:
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
        GraphEdge(node_to=t, node_from=s, cost=6),
        GraphEdge(node_to=y, node_from=s, cost=7),
    ]

    t.edges = [
        GraphEdge(node_to=z, node_from=t, cost=-4),
        GraphEdge(node_to=x, node_from=t, cost=5),
        GraphEdge(node_to=y, node_from=t, cost=8),
    ]

    y.edges = [
        GraphEdge(node_to=z, node_from=y, cost=9),
        GraphEdge(node_to=x, node_from=y, cost=-3),
    ]

    x.edges = [
        GraphEdge(node_to=t, node_from=x, cost=-2),
    ]

    z.edges = [
        GraphEdge(node_to=x, node_from=z, cost=7),
        GraphEdge(node_to=s, node_from=z, cost=2),
    ]

    bellman_ford_algorithm: BellmanFordAlgorithm = BellmanFordAlgorithm()
    circle: bool = bellman_ford_algorithm.check_negative_weight_cycle_existence(
        source_node=s,
        roots=[s, t, y, x, z]
    )

    if not circle:
        bellman_ford_algorithm.print_shortest_path(node_to=x)
        bellman_ford_algorithm.print_shortest_path(node_to=t)
    else:
        print(f'There is no shortest path from one source node to {x}')
