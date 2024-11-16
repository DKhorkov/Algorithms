"""
Реализация циклического двухсвязного списка, который зациклен концом на начало
(последний элемент ссылается на первый, а первый на последний).

Нулевой узел является ограничителем - фиктивным объектом, упрощающим учет граничных условий.

Скорость поиска O(n), скорость вставки O(1), скорость удаления O(n)
"""

from typing import Any

from Algorithms_Construction_and_Analysis.Chapter_10_elementary_data_structures.doubly_linked_list import (
    ListNode,
    DoublyLinkedList
)


class CycledDoublyLinkedList(DoublyLinkedList):

    def __init__(self) -> None:
        # Создаем циклический узел
        self._nil_node: ListNode = ListNode()
        self._nil_node.next = self._nil_node
        self._nil_node.prev = self._nil_node

        """Используем супер не в начале self.__init__(), чтобы корректно работал метод self._create_iterable(), 
        ссылающийся на self._nil_node
        """
        super().__init__()

    def _create_iterable(self) -> None:
        self._iterable = self._nil_node

    def search(self, value: Any) -> ListNode:
        """
        Данный метод практически не отличается от реализации в обычном двухсвязном списке за исключением сравнения с
        нулевым узлом вместо NoneType.
        """

        node: ListNode = self._nil_node.next
        while node != self._nil_node and node.value != value:
            node = node.next

        return node

    def insert(self, value: Any) -> None:
        """
        1) Создаем новый узел с переданным значением.
        2) Далее присваиваем этому узлу бывший узел наследник.
        3) Обновляем бывший узел наследник так, чтобы теперь его предком был не нулевой узел, а созданный узел.
        4) После обновления всех узлов делаем так, чтобы нулевой узел считал своим наследником созданный узел
        (произошла вставка).
        5) Связываем созданный узел с нулевым, поскольку до этого его родителем был NoneType.
        """

        node: ListNode = ListNode(value)
        node.next = self._nil_node.next
        self._nil_node.next.prev = node
        self._nil_node.next = node
        node.prev = self._nil_node

        self._length += 1
        self._create_iterable()

    def delete(self, value: Any) -> None:
        """
        За счет ограничителя в лице нулевого узла мы можем просто связать родителя и наследника текущего узла.
        В крайнем случае мы опять получим ситуацию, когда нулевой узел указывает сам на себя с обеих сторон.
        """

        node: ListNode = self.search(value)
        node.prev.next = node.next
        node.next.prev = node.prev

        self._length -= 1
        self._create_iterable()

    def __next__(self) -> ListNode:
        self._iterable = self._iterable.next
        if self._iterable is self._nil_node:
            self._create_iterable()
            raise StopIteration

        return self._iterable


if __name__ == '__main__':
    cycled_doubly_linked_list = CycledDoublyLinkedList()
    print(len(cycled_doubly_linked_list))
    cycled_doubly_linked_list.insert(1)
    cycled_doubly_linked_list.insert(3)
    cycled_doubly_linked_list.insert(2)
    print(len(cycled_doubly_linked_list))
    searched_node: ListNode = cycled_doubly_linked_list.search(1)
    print(searched_node.value)
    for node in iter(cycled_doubly_linked_list):
        print(node.value)

    print('\nnow will delete value = 3\n')
    cycled_doubly_linked_list.delete(3)
    for node in iter(cycled_doubly_linked_list):
        print(node.value)
