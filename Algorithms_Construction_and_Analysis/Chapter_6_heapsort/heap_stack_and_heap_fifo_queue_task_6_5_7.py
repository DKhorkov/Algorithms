"""
Является реализацией задачи 6.5.7.

Show how to implement a first-in, first-out queue with a priority queue.
Show how to implement a stack with a priority queue. (Queues and stacks are defined in section 10.1).
"""

from typing import AnyStr

from Algorithms_Construction_and_Analysis.Chapter_6_heapsort.heap_priority_queue import HeapPriorityQueue, QueueTask


class HeapStack(HeapPriorityQueue):

    def __init__(self) -> None:
        super().__init__()
        self._priority = 0

    def add(self, task: AnyStr) -> None:
        """
        За счет ПОВЫШЕНИЯ приоритета каждая новая добавленная таска будет иметь приоритет больше, чем у предыдущей,
        а следовательно, будет сортироваться для невозрастающей пирамиды и всегда перемещаться в самое начала массива.
        """

        self._tasks.append(
            QueueTask(
                task=task,
                priority=self._priority
            )
        )

        self._priority += 1
        self._heap_size += 1
        self.change_priority(index=self._heap_size - 1, priority=self._priority)


class HeapFirstInFirstOutQueue(HeapPriorityQueue):

    def __init__(self) -> None:
        super().__init__()
        self._priority = 1000  # Наша очередь будет не предполагать больше 1000 задач

    def add(self, task: AnyStr) -> None:
        """
        За счет ПОНИЖЕНИЯ приоритета каждая новая добавленная таска будет иметь приоритет меньше, чем у предыдущей,
        а следовательно, будет сортироваться для невозрастающей пирамиды и всегда перемещаться в самый низ левой или
        правой ветви. Далее, в ходе процесса извлечения, сортировка для невозрастающей пирамиды сделает за нас все
        остальное.
        """

        self._tasks.append(
            QueueTask(
                task=task,
                priority=self._priority
            )
        )

        self._priority -= 1
        self._heap_size += 1
        self.change_priority(index=self._heap_size - 1, priority=self._priority)


if __name__ == '__main__':
    heap_stack = HeapStack()
    task1 = 'first'
    task2 = 'second'
    task3 = 'third'
    task4 = 'fourth'
    task5 = 'fifth'
    task6 = 'sixth'

    heap_stack.add(task1)
    heap_stack.add(task2)
    heap_stack.add(task3)
    heap_stack.add(task4)
    heap_stack.add(task5)
    heap_stack.add(task6)
    for task in heap_stack:
        print(task)

    print('\n')

    heap_fifo_queue = HeapFirstInFirstOutQueue()
    heap_fifo_queue.add(task1)
    heap_fifo_queue.add(task2)
    heap_fifo_queue.add(task3)
    heap_fifo_queue.add(task4)
    heap_fifo_queue.add(task5)
    heap_fifo_queue.add(task6)
    for task in heap_fifo_queue:
        print(task)
