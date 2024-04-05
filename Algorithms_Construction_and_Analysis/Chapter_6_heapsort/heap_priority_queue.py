from typing import List, AnyStr, Optional, Self
from dataclasses import dataclass


@dataclass
class QueueTask:
    priority: int
    task: AnyStr

    def __str__(self) -> AnyStr:
        return f'Task with priority={self.priority} and value={self.task}'


class HeapPriorityQueue:
    """
    Очередь с приоритетами, основанная на невозрастающей пирамиде.
    """

    def __init__(self):
        self._heap_size: int = 0
        self._tasks: List[QueueTask] = []

    def _heapify(self, index: int) -> None:
        """
        Согласно второму закону основного метода решения рекуррентных уравнений, скорость алгоритма будет равна O(log(n)).

        Работа алгоритма аналогична пиромидальнйо сортировке, но сделан учет того, что таска - объект,
        а не целочисленное значение.
        """

        largest: int = index

        if index == 0:
            left = 1  # left = 2 * i, но по псевдокоду минимальный индекс = 1
        else:
            left: int = 2 * index

        right: int = left + 1

        if left < self._heap_size and self._tasks[largest].priority < self._tasks[left].priority:
            largest = left

        if right < self._heap_size and self._tasks[largest].priority < self._tasks[right].priority:
            largest = right

        if largest != index:
            self._swap(first_index=index, second_index=largest)
            self._heapify(largest)

    def _swap(self, first_index, second_index) -> None:
        self._tasks[first_index], self._tasks[second_index] = self._tasks[second_index], self._tasks[first_index]

    def get(self) -> Optional[QueueTask]:
        if self._heap_size == 0:
            return  # An Error could be raised

        """
        1) Достаем первую таску (с самым большим приоритетом согласно пирамиде)
        2) Уменьшаем размер очереди на 1, таким образом теперь она соответствует индексу последней таски в очереди. 
        3) Меняем первую таску на последнюю.
        4) Удаляем последнюю, поскольку она теперь дублируется.
        5) Сортируетм пирамиду так, чтобы она отвечала требованиям невозрастающей пирамиды.
        """
        task: QueueTask = self._tasks[0]
        self._heap_size -= 1
        self._tasks[0] = self._tasks[self._heap_size]
        self._tasks.pop(-1)
        self._heapify(0)
        return task

    def add(self, task: QueueTask) -> None:
        self._tasks.append(task)
        self._heap_size += 1
        self.change_priority(index=self._heap_size - 1, priority=task.priority)

    def change_priority(self, index: int, priority: int) -> None:
        self._check_index(index=index)
        self._check_priority(priority=priority)

        if priority >= self._tasks[index].priority:
            self._increase_priority(index=index, priority=priority)

        elif priority < self._tasks[index].priority:
            self._decrease_priority(index=index, priority=priority)

    def _increase_priority(self, index: int, priority: int) -> None:
        self._tasks[index].priority = priority

        while index > 0 and self._tasks[self._get_parent(index)].priority < self._tasks[index].priority:
            self._swap(first_index=self._get_parent(index), second_index=index)
            index = self._get_parent(index)

    def _decrease_priority(self, index: int, priority: int) -> None:
        """
        Является реализацией задачи 6.5.3.

        Write pseudocode for the procedures HEAP-MINIMUM, HEAP-EXTRACT-MIN,
        HEAP-DECREASE-KEY, and MIN-HEAP-INSERT that implement a min-priority queue with a min-heap.
        """

        self._tasks[index].priority = priority

        while (index < self._heap_size and
               self._get_left_child(index) < self._heap_size and   # Avoiding IndexError
               self._tasks[index].priority < self._tasks[self._get_left_child(index)].priority
        ):

            self._swap(first_index=self._get_left_child(index), second_index=index)
            index = self._get_left_child(index)

    def delete(self, index: int) -> None:
        """
        Является реализацией задачи 6.5.8.

        The operation HEAP-DELETE(A,i) deletes the item in node i from heap A.
        Give an implementation of HEAP-DELETE that runs in O(log(n)) time for an n-element max-heap.
        """

        self._check_index(index=index)
        self._tasks.pop(index)
        self._heap_size -= 1
        self._heapify(0)

    def _check_index(self, index: int) -> None:
        if index < 0 or index >= self._heap_size:
            raise IndexError(f'There is no task with index={index} in queue.')

    @staticmethod
    def _check_priority(priority: int) -> None:
        if priority < 0:
            raise ValueError(f'Priority can not be less than zero.')

    @staticmethod
    def _get_parent(index: int) -> int:
        # Согласно принципу получения родителя для пирамиды  parent = int(index / 2)
        return int(index / 2)

    @staticmethod
    def _get_left_child(index: int) -> int:
        """
        Согласно принципу получения родителя для пирамиды индекс левого под-дерева = 2 * index
        """
        if index == 0:
            return 1

        return index * 2 + 1

    @property
    def tasks(self) -> List[QueueTask]:
        return self._tasks

    def __iter__(self) -> Self:
        return self

    def __next__(self) -> QueueTask:
        if self._heap_size == 0:
            raise StopIteration

        return self.get()


if __name__ == '__main__':
    heap_priority_queue = HeapPriorityQueue()
    task1 = QueueTask(priority=10, task='fourth')
    task2 = QueueTask(priority=40, task='first')
    task3 = QueueTask(priority=20, task='third')
    task4 = QueueTask(priority=30, task='second')
    task5 = QueueTask(priority=1, task='sixth')
    task6 = QueueTask(priority=5, task='fifth')

    heap_priority_queue.add(task1)
    heap_priority_queue.add(task2)
    heap_priority_queue.add(task3)
    heap_priority_queue.add(task4)
    heap_priority_queue.add(task5)
    heap_priority_queue.add(task6)
    for task in heap_priority_queue:
        print(task)

    print('\n')

    heap_priority_queue.add(task1)
    heap_priority_queue.add(task2)
    heap_priority_queue.add(task3)
    heap_priority_queue.add(task4)
    heap_priority_queue.add(task5)
    heap_priority_queue.add(task6)
    heap_priority_queue.change_priority(index=2, priority=7)
    heap_priority_queue.change_priority(index=1, priority=50)
    heap_priority_queue.change_priority(index=4, priority=100)
    heap_priority_queue.change_priority(index=0, priority=1)
    for task in heap_priority_queue:
        print(task)

    print('\n')

    heap_priority_queue.add(task1)
    heap_priority_queue.add(task2)
    heap_priority_queue.add(task3)
    heap_priority_queue.add(task4)
    heap_priority_queue.add(task5)
    heap_priority_queue.add(task6)
    heap_priority_queue.delete(1)
    heap_priority_queue.delete(3)
    for task in heap_priority_queue:
        print(task)

    print('\n')