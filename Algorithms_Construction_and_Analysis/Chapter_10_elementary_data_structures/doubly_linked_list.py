"""
Реализация двухсвязного списка.
Скорость поиска O(n), скорость вставки O(1), скорость удаления O(n)
"""

from typing import Any, Optional, Self


class ListNode:

    def __init__(self, value: Any = None) -> None:
        self.prev: Optional[ListNode] = None
        self.value: Any = value
        self.next: Optional[ListNode] = None


class DoublyLinkedList:

    def __init__(self) -> None:
        self._head: Optional[ListNode] = None
        self._length: int = 0

        self._create_iterable()

    def _create_iterable(self) -> None:
        """
        Метод для создания итерируемого объекта, который будет использоваться итератором, а также будет обновлять
        итерируемый объект в случае наступления StopIteration ошибки, чтобы можно было использовать итератор
        бесконечное количество раз.
        """

        self._iterable = ListNode()
        self._iterable.next = self._head

    def search(self, value: Any) -> Optional[ListNode]:
        """
        Создаем временную переменную и продолжаем искать узел, значение которого совпадает с искомым.
        Если искомого значения нет - нода будет NoneType объектом, который мы и вернем.
        """

        node: Optional[ListNode] = self._head
        while node and node.value != value:
            node = node.next

        return node

    def insert(self, value: Any) -> None:
        """
        Создаем новый узел с заданным значением. Его следующим узлом становится старый корневой узел.
        Если старый корневой узел = None (список пуст), то новый узел просто становится корневым.
        Если же старый корневой узел существовал, то связываем его с новым узлом, указывая новый узел
        как предыдущий для старого узла, а затем делаем новый узел корневым.

        Также изменяем длину нашего списка и обновляем итерируемый объект, поскольку лист был изменен.
        """

        node: ListNode = ListNode(value)
        node.next = self._head
        if self._head:
            self._head.prev = node

        self._head = node

        self._length += 1
        self._create_iterable()

    def delete(self, value: Any) -> None:
        """
        Находим узел с заданным для удаления значением.

        Далее, если у узла есть родительский узел, то пересвязываем родительский узел таким образом, чтобы его
        наследником был не текущий узел (для удаления), а наследник текущего узла. Если же узел для удаления был
        корневым, то теперь корневой узел - наследник текущего узла (если таковой имеется, иначе None)

        Далее пересвязываем наследника текущего узла, если он имеется, таким образом, чтобы он считал своим
        родителем не текущий узел, а родителя текущего узла.

        После этих действий на текущий узел не будет ссылаться ни его родитель, ни его наследник.

        Также изменяем длину нашего списка и обновляем итерируемый объект, поскольку лист был изменен.
        """

        node: ListNode = self.search(value)
        if node.prev:
            node.prev.next = node.next
        else:
            self._head = node.next

        if node.next:
            node.next.prev = node.prev

        self._length -= 1
        self._create_iterable()

    def __len__(self) -> int:
        return self._length

    def __iter__(self) -> Self:
        return self

    def __next__(self) -> ListNode:
        self._iterable = self._iterable.next
        if self._iterable is None:
            self._create_iterable()
            raise StopIteration

        return self._iterable


if __name__ == '__main__':
    doubly_linked_list: DoublyLinkedList = DoublyLinkedList()
    print(len(doubly_linked_list))
    doubly_linked_list.insert(1)
    doubly_linked_list.insert(3)
    doubly_linked_list.insert(2)
    print(len(doubly_linked_list))
    searched_node: ListNode = doubly_linked_list.search(1)
    print(searched_node.value)
    for node in iter(doubly_linked_list):
        print(node.value)

    print('\nnow will delete value = 3\n')
    doubly_linked_list.delete(3)
    for node in iter(doubly_linked_list):
        print(node.value)

