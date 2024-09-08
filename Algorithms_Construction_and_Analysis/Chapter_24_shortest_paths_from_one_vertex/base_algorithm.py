import math
from typing import List, Optional, Set

from Algorithms_Construction_and_Analysis.Chapter_24_shortest_paths_from_one_vertex.node import GraphNode, GraphEdge


class ShortestPathsFromOneVertexBaseAlgorithm:

    def __init__(self) -> None:
        self._roots: List[GraphNode] = []
        self._source_node: Optional[GraphNode] = None
        self._edges: List[GraphEdge] = []

    def _init_single_source(self) -> None:
        """
        Инициализирует каждую из вершин для дальнейшей обработки и ослабления.
        Исходная вершина получает кратчайший путь, равный 0, так как из нее будет начинаться поиск.
        """

        for root in self._roots:
            root.parent = None
            root.shortest_path_estimate = math.inf
            root.path_from_source = []

        self._source_node.shortest_path_estimate = 0

    def _get_all_edges(self) -> None:
        self._edges.clear()
        for root in self._roots:
            self._edges += root.edges

    @staticmethod
    def _relax(edge: GraphEdge) -> None:
        """
        Процедура ослабления, которая проверяет, может ли значение кратчайшего пути до вершины уменьшено.
        Значение может быть уменьшено, если из потенциальной новой вершины родителя до текущей вершины путь
        с учетом цены ребра будет меньше, чем текущий.
        """

        if edge.node_to.shortest_path_estimate > edge.node_from.shortest_path_estimate + edge.cost:
            edge.node_to.shortest_path_estimate = edge.node_from.shortest_path_estimate + edge.cost
            edge.node_to.parent = edge.node_from
            edge.node_to.path_from_source = edge.node_from.path_from_source + [edge]

    def print_shortest_path(self, node_to: GraphNode) -> None:
        print(f'\nWay from {self._source_node} to {node_to}:')
        for edge in node_to.path_from_source:
            print(f'\t{edge}')

        if not node_to.shortest_path_estimate == math.inf:
            print(f'Shortest path from {self._source_node} to {node_to} costs {node_to.shortest_path_estimate}.')
        else:
            print(f'There is no path from {self._source_node} to {node_to}.')
