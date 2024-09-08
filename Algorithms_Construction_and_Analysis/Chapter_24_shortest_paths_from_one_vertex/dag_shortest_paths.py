"""
Алгоритм поиска кратчайших путей из вершины в ациклическом ориентированном взвешенном графе.

Ослабляя ребра взвешенного ориентированного ациклического графа G = (V, E) в порядке, определенном
топологической сортировкой его вершин, кратчайшие пути из одной вершины можно найти за время O(V + E).
В ориентированном ациклическом графе кратчайшие пути всегда вполне определены, поскольку, даже если вес
некоторых ребер отрицателен, циклов с отрицательными весами не существует.

Работа алгоритма начинается с топологической сортировки ориентированного ациклического графа,
которая должна установить линейное упорядочение вершин. Если путь из первой вершины ко второй вершине и существует,
то в топологической сортировке первая вершина предшествует второй вершине.
По вершинам, расположенным в топологическом порядке, проход выполняется только один раз.
При обработке каждой вершины производится ослабление всех ребер, исходящих из этой вершины с целью найти
кратчайший путь до каждой вершины из исходной.

Граф для теста будет следующим (ацикличный ориентированный взвешенный),
где символ "*" является частью ребра от вершины к вершине, "←" - направление графа,
а цифры - стоимость перемещения по ребру между узлами:


                   * * * * 6 * * * * *          * * * * 1 * * * * *
                 *                     *      *                      *
               *                         ↘  ↗                          ↘
R * * 5 * * → S * * 2 * * → T * * 7 * * → X * * -1 * * → Y * * -2 * * → Z
 *                        ↗ ↓  ↘                        ↗              ↗
   *                    *   *     * * * * * 4 * * * * *              *
     * * * * 3 * * * *       *                                     *
                                * * * * * * * * 2 * * * * * * * *

Асимптоматическая скорость алгоритма составляет O(V + E) за счет топологической сортировки,
где V - количество вершин графа, а E - количество ребер.
"""


from typing import List, Any, Optional

from Algorithms_Construction_and_Analysis.Chapter_22_elementary_algorithms_with_graphs.colors import GraphNodeColors
from Algorithms_Construction_and_Analysis.Chapter_22_elementary_algorithms_with_graphs.topological_sort import (
    TopologicalGraphNode,
    TopologicalSort
)
from Algorithms_Construction_and_Analysis.Chapter_24_shortest_paths_from_one_vertex.base_algorithm import (
    ShortestPathsFromOneVertexBaseAlgorithm
)
from Algorithms_Construction_and_Analysis.Chapter_24_shortest_paths_from_one_vertex.node import GraphNode, GraphEdge


class DAGShortestPathsNode(GraphNode, TopologicalGraphNode):

    def __init__(self, value: Any) -> None:
        super().__init__(value=value)

        # Topological node attrs:
        self.neighbors: List[DAGShortestPathsNode] = []
        self.distance_from_root: int = 0
        self.parent: Optional[DAGShortestPathsNode] = None
        self.color: GraphNodeColors = GraphNodeColors.WHITE
        self.opening_time: int = 0
        self.explored_time: int = 0


class DAGShortestPaths(ShortestPathsFromOneVertexBaseAlgorithm):

    def process_graph(self, roots: List[DAGShortestPathsNode], source_node: DAGShortestPathsNode) -> None:
        topological_sorter = TopologicalSort()
        topological_sorter.sort(roots=roots)
        self._roots = topological_sorter.sorted_nodes
        self._source_node = source_node

        self._init_single_source()
        self._get_all_edges()

        for edge in self._edges:
            self._relax(edge=edge)


if __name__ == '__main__':
    # Create nodes:
    r: DAGShortestPathsNode = DAGShortestPathsNode('r')
    s: DAGShortestPathsNode = DAGShortestPathsNode('s')
    t: DAGShortestPathsNode = DAGShortestPathsNode('t')
    x: DAGShortestPathsNode = DAGShortestPathsNode('x')
    y: DAGShortestPathsNode = DAGShortestPathsNode('y')
    z: DAGShortestPathsNode = DAGShortestPathsNode('z')

    # Adding neighbours for topological sort:
    r.neighbors = [s, t]
    s.neighbors = [t, x]
    t.neighbors = [z, x, y]
    x.neighbors = [y, z]
    y.neighbors = [z]

    # Create edges:
    r.edges = [
        GraphEdge(node_from=r, node_to=t, cost=3),
        GraphEdge(node_from=r, node_to=s, cost=5),
    ]

    s.edges = [
        GraphEdge(node_from=s, node_to=t, cost=2),
        GraphEdge(node_from=s, node_to=x, cost=6),
    ]

    t.edges = [
        GraphEdge(node_from=t, node_to=z, cost=2),
        GraphEdge(node_from=t, node_to=x, cost=7),
        GraphEdge(node_from=t, node_to=y, cost=4),
    ]

    x.edges = [
        GraphEdge(node_from=x, node_to=y, cost=-1),
        GraphEdge(node_from=x, node_to=z, cost=1),
    ]

    y.edges = [
        GraphEdge(node_from=y, node_to=z, cost=-2),
    ]

    dag_shortest_paths_algorithm: DAGShortestPaths = DAGShortestPaths()
    dag_shortest_paths_algorithm.process_graph(
        source_node=s,
        # roots=[r, s, t, x, y, z],
        # roots=[s, z, r, y, t, x],
        roots=[z, y, x, t, s, r]
    )

    dag_shortest_paths_algorithm.print_shortest_path(node_to=r)
    dag_shortest_paths_algorithm.print_shortest_path(node_to=y)
    dag_shortest_paths_algorithm.print_shortest_path(node_to=z)
