"""
Базовая hash-таблица, в которой для разрешения конфликтов используется метод цепочек на основе связного списка.
В качестве метода hash-функции выбран метод делением.

Асимптоматическая скорость вставки O(1), поиска и удаления - O(n) из-за того, что поиск идет по связному списку.
"""

from typing import List, Optional, Any


class ListNode:

    def __init__(self, key: int, value: Any = None) -> None:
        self.prev: Optional[ListNode] = None
        self.key: int = key
        self.value: Any = value
        self.next: Optional[ListNode] = None


class LinkedList:

    def __init__(self) -> None:
        self._head: Optional[ListNode] = None
        self._length: int = 0

    def search(self, key: int) -> Optional[ListNode]:
        node: Optional[ListNode] = self._head
        while node and node.key != key:
            node = node.next

        return node

    def insert(self, key: int, value: Any) -> None:
        node: ListNode = ListNode(key=key, value=value)
        node.next = self._head
        if self._head:
            self._head.prev = node

        self._head = node
        self._length += 1

    def delete(self, key: int) -> None:
        node: Optional[ListNode] = self.search(key)
        if node is None:
            raise KeyError

        if node.prev:
            node.prev.next = node.next
        else:
            self._head = node.next

        if node.next:
            node.next.prev = node.prev

        self._length -= 1

    def __len__(self) -> int:
        return self._length


class HashTable:

    def __init__(self, size: int = 200) -> None:
        self._size: int = size
        self._table: List[Optional[LinkedList]] = [None] * self._size

    def _hash(self, key: int) -> int:
        return key % self._size

    def __setitem__(self, key: int, value: Any):
        hashed_key: int = self._hash(key)
        if self._table[hashed_key] is None:
            self._table[hashed_key] = LinkedList()

        self._table[hashed_key].insert(key=key, value=value)

    def __getitem__(self, key: int) -> Any:
        hashed_key: int = self._hash(key)
        linked_list: Optional[LinkedList] = self._table[hashed_key]
        if linked_list is None:
            raise KeyError

        return linked_list.search(key=key).value

    def remove(self, key: int) -> None:
        hashed_key: int = self._hash(key)
        linked_list: Optional[LinkedList] = self._table[hashed_key]
        if linked_list is None:
            raise KeyError

        """
        Обновляем до начального состояния и освобождаем память от хранения пустого списка в случае, если длина списка
        равняется нулю.
        """
        linked_list.delete(key=key)
        if len(linked_list) == 0:
            self._table[hashed_key] = None

    def get(self, key: int, default: Any = None) -> Any:
        try:
            return self.__getitem__(key)
        except KeyError:
            return default


if __name__ == '__main__':
    hash_table: HashTable = HashTable()
    hash_table[1] = 'a'
    hash_table[201] = 'n'
    hash_table[20] = 'a'
    try:
        print(hash_table[22])
    except KeyError:
        print('Key 22 not found')

    print(hash_table.get(22, 'default_value'))
    hash_table.remove(20)
    print(hash_table.get(20, 'deleted value'))

    print(hash_table.get(201, 'deleted value'))
    try:
        hash_table.remove(20)
    except KeyError:
        print('Key 20 not in hash_table')
