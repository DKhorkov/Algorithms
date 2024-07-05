"""
B-tree - это сбалансированное дерево поиска, которое имеет множество детей у каждого узла, а также ключей у каждого
узла. Количество узлов зависит от степени (t-degree) дерева.

Данное дерево особенно хорошо подходят для систем хранения с медленным и объемным доступом к данным,
таких как жесткие диски, флэш-память и компакт-диски.

Основные свойства B-tree:
1) Каждый узел, кроме корневого, должен содержать как минимум t - 1 ключей;
2) Каждый узел должен содержать не более 2t - 1 ключей;
3) Каждый внутренний узел (не лист), не являющийся корневым, имеет как минимум t дочерних узлов;
4) Внутренний узел имеет не более 2t дочерних узлов;
5) Узел заполнен, если содержит ровно 2t - 1 ключей;
6) Ключи каждого узла находятся в отсортированном порядке;
7) Все листья B-tree находятся всегда на одном уровне;
8) Глубина B-tree всегда увеличивается или уменьшается сверху, а не снизу как у других деревьев.

Асимптоматическая скорость всех операций с B-tree составляет O(log n), где n - высота дерева.

https://www.geeksforgeeks.org/b-tree-in-python/amp/ - доп. источник.
"""

from typing import List, Optional, Any


class BTreeNode:

    def __init__(self, is_leaf: bool = False) -> None:
        """
        В данной реализации ключи являются целыми числами, но могут быть заменены любым объектом, который имеет методы
        __hash__, __gt__, __lt__, __eq__.

        Главное условие - сравнение для целей сортировки ключей.
        """

        self.is_leaf: bool = is_leaf
        self.keys: List[int] = []
        self.values: List[Any] = []  # Upgrade of tree to store data by key index
        self.children: List[BTreeNode] = []

    def display(self, high: int = 0) -> None:
        """
        Отрисовывает в консоли текущее B-tree с учетом высоты узла.
        """

        print(f"Tree node high: {high}: {self.keys}")
        if not self.is_leaf:
            for child in self.children:
                child.display(high=high + 1)


class BTree:
    def __init__(self, degree: int) -> None:
        self._root: BTreeNode = BTreeNode(is_leaf=True)
        self._degree = degree

        self._max_keys_len: int = 2 * self._degree - 1

    def display(self):
        self._root.display()

    def insert(self, key: int, value: Any) -> None:
        """
        Вставляет новый узел в дерево.
        Если корень дерева заполнен, то он должен быть разбит и создан новый корень, а высота дерева
        увеличится на единицу.
        """

        root: BTreeNode = self._root
        if len(root.keys) == self._max_keys_len:
            temp: BTreeNode = BTreeNode()
            self._root = temp
            temp.children.append(root)
            self._split_child_node(temp, 0)  # Разбиваем единственный узел, который является бывшим заполненным корнем
            self._insert_non_full(node_to_insert_to=temp, key=key, value=value)
        else:
            self._insert_non_full(node_to_insert_to=root, key=key, value=value)

    def _insert_non_full(self, node_to_insert_to: BTreeNode, key: int, value: Any) -> None:
        """
        Вставка нового ключа в НЕ заполненный узел.
        Если узел является листом, то просто добавляем ключ к текущему узлу, смещая имеющиеся ключи таким образом,
        чтобы поддерживались свойства B-tree с точки зрения сортировки ключей узлов.

        Если же узел является поддеревом, то необходимо вставить ключ в подходящий узел в поддереве. Если узел заполнен,
        то вызывается процедура его разбивки, после чего производится определение дочернего узла (одного из двух
        созданных после разбиения), в который будет вставлен ключ.

        Таким образом, вставка нового ключа в дерево происходит за один проход от вершины дерева к нужному для
        вставки узлу, что гарантируется операциями _insert_non_full и _split_child_node.
        """

        index: int = len(node_to_insert_to.keys) - 1  # -1 так как массив начинается с 0 индекса

        if node_to_insert_to.is_leaf:
            # Создаем новый индекс в самом конце, чтобы сдвигать ключи и освободить место для нового узла:
            node_to_insert_to.keys.append(-1)
            node_to_insert_to.values.append(-1)

            """
            Поскольку мы идем с индекса, представляющего самый большой ключ узла, то сдвигаем все ключи, 
            которые меньше ключа для вставки
            """
            while index >= 0 and key < node_to_insert_to.keys[index]:
                node_to_insert_to.keys[index + 1] = node_to_insert_to.keys[index]
                node_to_insert_to.values[index + 1] = node_to_insert_to.values[index]
                index -= 1

            node_to_insert_to.keys[index + 1] = key
            node_to_insert_to.values[index + 1] = value
        else:
            # Ищем позицию, дочернего к текущему узла, в который будет вставлен ключ:
            while index >= 0 and key < node_to_insert_to.keys[index]:
                index -= 1

            index += 1

            # Разбиваем дочерний узел, если он заполнен:
            if len(node_to_insert_to.children[index].keys) == self._max_keys_len:
                self._split_child_node(node=node_to_insert_to, index=index)

                """
                Поскольку дочерний узел был разбит на два и его медиана была перемещена в родительский узел,
                то необходимо определить путем новой проверки, в какой из двух дочерних узлов (левый или правый) 
                должен быть вставлен новый ключ. Поскольку ключи были отсортированы в дочернем узле до разделения 
                (и такими и остаются в обоих новых дочерних узлах), то мы сравним самый большой ключ в первом новом
                дочернем узле с ключом для вставки, и, если ключ для вставки больше, то нам нужен второй ключ, а иначе
                первый. 
                """
                if key > node_to_insert_to.keys[index]:
                    index += 1

            self._insert_non_full(node_to_insert_to=node_to_insert_to.children[index], key=key, value=value)

    def _split_child_node(self, node: BTreeNode, index: int) -> None:
        """
        Получает узел, дочерний узел которого необходимо разделить.
        Дочерний узел разделяется на два новых (оба становятся дочерними узлами текущего полученного узла),
        а медианный ключ переносится в родительский узел так, чтобы были сохранены свойства B-tree.
        Высота дерева при этом увеличивается на единицу.

        Изначально дочерний разбиваемый узел имеет 2t узлов и 2t - 1 ключей, а после разбиения каждый из новых
        дочерних узлов будет иметь t узлов и t - 1 ключей.

        ВАЖНО: ключи, значения и дети должны сначала быть перенесены в новый дочерний узел,
        иначе они потрутся и пропадут.
        """

        split_node = node.children[index]
        new_brother_node = BTreeNode(is_leaf=split_node.is_leaf)

        # Вставляем медианный ключ и значение, принадлежащее ему, в родительский узел:
        node.keys.insert(index, split_node.keys[self._degree - 1])
        node.values.insert(index, split_node.values[self._degree - 1])

        # Разделяемый узел без медианы делится на два новых дочерних узла:
        new_brother_node.keys = split_node.keys[self._degree:]
        new_brother_node.values = split_node.values[self._degree:]
        split_node.keys = split_node.keys[: self._degree - 1]
        split_node.values = split_node.values[: self._degree - 1]

        # Если разделяемый узел не был листом, то его дети тоже должны быть разделены между новыми дочерними узлами
        if not split_node.is_leaf:
            new_brother_node.children = split_node.children[self._degree:]
            split_node.children = split_node.children[: self._degree - 1]

        """
        Поскольку второй дочерний узел является новым и имеет ключи, которые больше по значению, 
        чем у разделяемого узла, то он вставляется дальше по индексу детей родительского узла.
        """
        node.children.insert(index + 1, new_brother_node)

    def search(self, key: int, node: Optional[BTreeNode] = None) -> Optional[Any]:
        """
        Если не передан узел, то поиск начинается с корневого узла и продолжается рекурсивно, пока не найдет
        заданный ключ, либо пока не перейдет к листу (у листа нет дочерних узлов). Если ключ не найден в листе по
        заданному индексу, значит ключа нет в дереве. Если же узел не является листом, спускаемся по дереву рекурсивно
        и ищем ключ в поддереве.
        """

        if node is None:
            return self.search(key=key, node=self._root)

        """
        Проходимся по отсортированным ключам в поиске места, где ключ будет НЕ больше ключа, 
        представленного текущим значением индекса. В таком случае ключ либо равен искомому, либо больше него, и 
        надо искать заданный ключ в поддереве, если таковое имеется.
        """
        index: int = 0
        while index < len(node.keys) and key > node.keys[index]:
            index += 1

        if index < len(node.keys) and key == node.keys[index]:
            return node.values[index]
        elif node.is_leaf:
            return None
        else:
            return self.search(key=key, node=node.children[index])


if __name__ == '__main__':
    bt = BTree(degree=3)
    keys: List[int] = [10, 20, 5, 6, 12, 30, 7, 17]
    values: List[Any] = ['some', True, 102, 'data', {n for n in range(10)}, {'in': 'values'}, False, 15]
    assert len(keys) == len(values)

    for i in range(len(keys)):
        bt.insert(key=keys[i], value=values[i])

    bt.display()
    print('\n\n')

    for i in range(len(keys)):
        search_result: Optional[Any] = bt.search(key=keys[i])
        assert search_result == values[i]
        print(f'Value for key={keys[i]} = {search_result}')

