from __future__ import annotations

import math
from typing import Optional, List, Any, Union


class GraphEdge:

    def __init__(self, node_to: GraphNode, node_from: GraphNode, cost: int) -> None:
        self.node_to: GraphNode = node_to
        self.node_from: GraphNode = node_from
        self.cost: int = cost

    def __hash__(self) -> int:
        return hash(f'{self.node_to}_{self.node_from}_{self.cost}')

    def __str__(self) -> str:
        return f'"{self.node_from}" -> "{self.node_to}" with cost {self.cost}'


class GraphNode:

    def __init__(self, value: Any) -> None:
        self.parent: Optional[GraphNode] = None
        self.shortest_path_estimate: Union[int, float] = math.inf  # Нет пути к узлу из исходного узла
        self.value: Any = value
        self.edges: List[GraphEdge] = []
        self.path_from_source: List[GraphEdge] = []

    def __str__(self) -> str:
        return f'Node with value={self.value}'
