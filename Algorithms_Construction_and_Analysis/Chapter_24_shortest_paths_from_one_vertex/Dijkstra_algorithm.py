"""
Алгоритм Дейкстры решает задачу поиска кратчайших путей из одной вершины во взвешенном ориентированном
графе G = (V, E) в случае, когда веса ребер неотрицательны.
При хорошей реализации время работы алгоритма Дейкстры меньше времени работы алгоритма Беллмана-Форда.
В ходе обработки этой вершин проводится ослабление всех исходящих из вершины ребер.
В приведенной ниже реализации используется неубывающая очередь с приоритетами на основе бинарной пирамиды.
В очередь кладутся ребра графа, а приоритетом является стоимость перехода по ребру.

Граф для теста будет следующим (цикличный ориентированный взвешенный),
где символ "*" является частью ребра от вершины к вершине, "←" - направление графа,
а цифры - стоимость перемещения по ребру между узлами:

          T * * * * 1 * * * → X
       ↗ * ↖                ↗ * ↖
    10   *   *           *    *   *
  *      *   *        *       *     *
S        2   3      9         4     6
↑ *      *   *    *           *     *
*   5    *   *  *             *     *
*      ↘ ↘  * *               ↓   *
  *       Y * * * * 2 * * * → Z *
     *                      *
       * * * * * 7 * * * *

Время работы алгоритма Дейкстры зависит от реализации неубывающей очереди с приоритетами:
1) Неубывающая очередь с приоритетами поддерживается за счет того,
что все вершины пронумерованы от 1 до V. Атрибут @shortest_path_estimate просто помещается в элемент массива 
с индексом v. Каждая операция INSERT и DECREASE-KEY занимает время О(1), а каждая операция
EXTRACT-MIN - время O(V) (поскольку в ней выполняется поиск по всему мас-сиву); в результате полное время работы 
алгоритма равно О(V^2 + E) = 0(V^2).
2) Если граф достаточно разреженный, в частности, если количество вершин и ребер в нем связаны 
соотношением Е = o(V^2/log(V)), алгоритм можно сделать более эффективным путем реализации неубывающей очереди с 
приоритетами с помощью бинарной неубывающей пирамиды. Каждая операция EXTRACT-MIN занимает время О(log(V)). 
Как и ранее, всего таких операций - V. Время, необходимое для построения неубывающей пирамиды, равно O(V). 
Каждая операция DECREASE-KEY выполняется за время О(log(V)), а всего таких операций выполняется не более Е. 
Поэтому полное время работы алгоритма составляет О((V + E) log(V)), что равно О(E * log(V)), 
если все вершины достижимы из истока. Это время работы оказывается лучшим по сравнению со временем работы 
прямой реализации О(V^2), если Е = o(V^2/log(V)).
3) Фактически можно достичь времени работы алгоритма O(V * log(V) + Е), если неубывающая очередь с приоритетами
реализуется с помощью пирамиды Фибоначчи. Амортизированная стоимость каждой из V операций
EXTRACT-MIN равна O(log(V)), а каждый вызов процедуры DECREASE-KEY (всего их не более E) требует лишь О(1)
амортизированного времени. Исторически сложилось так, что развитие пирамид Фибоначчи было стимулировано наблюдением:
в алгоритме Дейкстры процедура DECREASE-KEY обычно вызывается намного чаще, чем процедура EXTRACT-MIN.
Любой метод, уменьшающий амортизированное время каждой операции DECREASE-KEY до величины o(log(V)),
не увеличивая при этом амортизированного времени операции EXTRACT-MIN, позволяет получить реализацию,
которая в асимптотическом пределе работает быстрее, чем реализация с помощью бинарных пирамид.
"""


from typing import List, Union

from Algorithms_Construction_and_Analysis.Chapter_24_shortest_paths_from_one_vertex.base_algorithm import (
    ShortestPathsFromOneVertexBaseAlgorithm
)
from Algorithms_Construction_and_Analysis.Chapter_24_shortest_paths_from_one_vertex.node import GraphNode, GraphEdge
from Algorithms_Construction_and_Analysis.Chapter_6_heapsort.heap_priority_queue import HeapPriorityQueue, QueueTask


class DijkstraAlgorithm(ShortestPathsFromOneVertexBaseAlgorithm):

    def process_graph(self, roots: List[GraphNode], source_node: GraphNode) -> None:
        """
        Подготавливает вершины и ребра для дальнейшей обработки через очередь с приоритетами.
        """

        self._roots = roots
        self._source_node = source_node
        self._init_single_source()
        self._get_all_edges()

        priority_queue: HeapPriorityQueue = HeapPriorityQueue()
        for edge in self._edges:
            priority_queue.add(
                task=QueueTask(
                    priority=edge.cost,
                    task=edge
                )
            )

        self._process_roots_via_priority_queue(priority_queue=priority_queue)

    def _process_roots_via_priority_queue(self, priority_queue: HeapPriorityQueue) -> None:
        """
        Обрабатывает каждое ребро в очереди, пытаясь провести ослабление. Если ослабление произведено, то вершина,
        в которую входит ребро, должна изменить приоритет в очереди на актуальный.
        """

        while not priority_queue.is_empty():
            edge: GraphEdge = priority_queue.get().task
            old_shortest_path_estimate: Union[int, float] = edge.node_to.shortest_path_estimate
            self._relax(edge=edge)

            if old_shortest_path_estimate > edge.node_to.shortest_path_estimate:
                self._update_edge_priority(
                    priority_queue=priority_queue,
                    edge=edge
                )

    @staticmethod
    def _update_edge_priority(priority_queue: HeapPriorityQueue, edge: GraphEdge) -> None:
        """
        Обновляет приоритет ребра в очереди.
        """

        for index, task in enumerate(priority_queue.tasks):
            if task.task == edge.node_to:
                priority_queue.change_priority(index=index, priority=task.task.priority)


if __name__ == '__main__':
    # Create nodes:
    s: GraphNode = GraphNode('s')
    t: GraphNode = GraphNode('t')
    y: GraphNode = GraphNode('y')
    x: GraphNode = GraphNode('x')
    z: GraphNode = GraphNode('z')

    # Create edges:
    s.edges = [
        GraphEdge(node_from=s, node_to=t, cost=10),
        GraphEdge(node_from=s, node_to=y, cost=5),
    ]

    t.edges = [
        GraphEdge(node_from=t, node_to=y, cost=2),
        GraphEdge(node_from=t, node_to=x, cost=1),
    ]

    y.edges = [
        GraphEdge(node_from=y, node_to=t, cost=3),
        GraphEdge(node_from=y, node_to=z, cost=2),
        GraphEdge(node_from=y, node_to=x, cost=9),
    ]

    x.edges = [
        GraphEdge(node_from=x, node_to=z, cost=4),
    ]

    z.edges = [
        GraphEdge(node_from=z, node_to=x, cost=6),
        GraphEdge(node_from=z, node_to=s, cost=7),
    ]

    dijkstra_algorithm: DijkstraAlgorithm = DijkstraAlgorithm()
    dijkstra_algorithm.process_graph(
        source_node=s,
        # roots=[s, t, y, x, z],
        roots=[s, z, y, t, x],
        # roots=[z, x, y, t, s]
    )

    dijkstra_algorithm.print_shortest_path(node_to=x)
    dijkstra_algorithm.print_shortest_path(node_to=t)
    dijkstra_algorithm.print_shortest_path(node_to=z)
