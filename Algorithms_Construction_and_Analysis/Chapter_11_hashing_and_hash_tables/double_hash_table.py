"""
Hash-таблица, в которой используется двойное хеширование.
В качестве основного метода hash-функции выбран метод делением, а вторичного - метод умножения.

Асимптоматическая скорость вставки, поиска и удаления - O(1) за счет того, что в случае, когда несколько разных ключей
попадают в один хэшированный индекс, то происходит вторичное хеширование и они распределяются по разным ячейкам
внутреннего массива.
"""

from typing import Any, List


class DoubleHashTable:

    def __init__(self, size: int = 200) -> None:
        self._size: int = size
        self._table: List[List[Any]] = [[None] * self._size] * self._size

    def _main_hash(self, key: int) -> int:
        return key % self._size

    def _secondary_hash(self, key: int) -> int:
        solt: float = 0.6180339887  # Knuth suggestion ≈ (√5 - 1) / √2
        return int(self._size * (key * solt % 1))

    def __setitem__(self, key: int, value: Any):
        main_hash: int = self._main_hash(key)
        secondary_hash: int = self._secondary_hash(key)
        self._table[main_hash][secondary_hash] = value

    def __getitem__(self, key: int) -> Any:
        main_hash: int = self._main_hash(key)
        if self._table[main_hash] is None:
            raise KeyError

        secondary_hash: int = self._secondary_hash(key)
        value: Any = self._table[main_hash][secondary_hash]
        if value is None:
            raise KeyError

        return value

    def remove(self, key: int) -> None:
        if self.__getitem__(key) is None:
            raise KeyError

        main_hash: int = self._main_hash(key)
        secondary_hash: int = self._secondary_hash(key)
        self._table[main_hash][secondary_hash] = None

    def get(self, key: int, default: Any = None) -> Any:
        try:
            return self.__getitem__(key)
        except KeyError:
            return default


if __name__ == '__main__':
    double_hash_table: DoubleHashTable = DoubleHashTable()
    double_hash_table[1] = 'a'
    double_hash_table[201] = 'n'
    double_hash_table[20] = 'a'
    try:
        print(double_hash_table[22])
    except KeyError:
        print('Key 22 not found')

    print(double_hash_table.get(22, 'default_value'))
    double_hash_table.remove(20)
    print(double_hash_table.get(20, 'deleted value'))

    print(double_hash_table.get(201, 'deleted value'))
    try:
        double_hash_table.remove(20)
    except KeyError:
        print('Key 20 not in double_hash_table')


