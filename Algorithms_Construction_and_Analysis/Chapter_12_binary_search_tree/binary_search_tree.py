"""
Бинарное дерево поиска - это структура, где ключи всех левых ветвей меньше или равны родительскому, а ключи всех
правых ветвей больше или равны родительскому.

Все основные операции (вставка, поиск, удаление, максимум, минимум, родитель и наследник)
выполняются за асимптоматические O(log(n)), а обход всего дерева за O(n).
"""

from typing import Optional, List, Any


class Node:

    def __init__(self, key: int) -> None:
        self.parent: Optional[Node] = None
        self.left: Optional[Node] = None
        self.key: int = key
        self.value: Any
        self.right: Optional[Node] = None


class BinarySearchTree:

    def __init__(self, root: Optional[Node] = None) -> None:
        self.root: Optional[Node] = root

    def traverse(self, node: Node = None) -> List[Node]:
        """
        Обходим дерево так, чтобы список узлов вернулся в отсортированном по ключам порядке,
        что происходит за счет концепции бинарного дерева поиска.
        """

        if node is None:
            node: Optional[Node] = self.root

        if node:
            return self.traverse(node.left) + [node.key] + self.traverse(node.right)

        return []

    def search(self, key: int, node: Node = None) -> Optional[Node]:
        """
        Если дерево пустое или узла с искомым ключом в дереве нет, то получим NoneType.
        Если искомый ключ меньше ключа родительского узла, то по определению бинарного дерева он может
        находиться только в левом узле наследнике. Если же он больше родительского, то в правом.
        Если искомый ключ равен ключу узла, значит это и есть искомый узел.
        """

        if node is None:
            node: Optional[Node] = self.root

        if not node or node.key == key:
            return node

        if node.key < key:
            return self.search(key, node.left)
        else:
            return self.search(key, node.right)

    def find_max(self, node: Optional[Node] = None) -> Optional[Node]:
        """
        Является выполнением задачи 12.2.2.

        Если у нас нет узла или его правого наследника, то возвращаем пустой узел.
        В ином случае максимум находится в самом правом узле наследнике на последнем уровне бинарного дерева.
        """

        if node is None:
            node: Optional[Node] = self.root

        if not node or not node.right:
            return node

        return self.find_max(node.right)

    def find_min(self, node: Optional[Node] = None) -> Optional[Node]:
        """
        Является выполнением задачи 12.2.2.

        Если у нас нет узла или его левого наследника, то возвращаем пустой узел.
        В ином случае минимум находится в самом левом узле наследнике на последнем уровне бинарного дерева.
        """

        if node is None:
            node: Optional[Node] = self.root

        if not node or not node.left:
            return node

        return self.find_min(node.left)

    def successor(self, node: Optional[Node] = None) -> Optional[Node]:
        """
        Данный метод ищет ближайший больший узел к заданному
        (как в случае, когда все узлы были бы отсортированы методом self.traverse()).

        Если имеется правый наследник у заданного узла, то нам нужен наименьший узел правого наследника, поскольку
        все правые узлы больше или равны текущему по ключу. Таким образом наименьший узел находится в левой ветви
        правого наследника (движемся вниз по левой ветке правого наследника).

        Если же правого наследника нет, то ближайший больший узел находится сверху в дереве по отношению
        к заданному. Пока заданный узел является правым наследником своего родителя, мы двигаемся вверх по веткам
        дерева, поскольку справа находятся большие элементы от родителя, а значит текущий узел больше своего родителя,
        а нам нужен узел, который большего текущего.
        """

        if node is None:
            node: Optional[Node] = self.root

        if node.right:
            return self.find_min(node.right)

        successor_node: Optional[Node] = node.parent
        while successor_node and node == successor_node.right:
            node = successor_node
            successor_node = node.parent

        return successor_node

    def predecessor(self, node: Optional[Node] = None) -> Optional[Node]:
        """
        Является выполнением задачи 12.2.3.

        Данный метод ищет ближайший меньший узел к заданному
        (как в случае, когда все узлы были бы отсортированы методом self.traverse()).

        Если имеется левый наследник у заданного узла, то нам нужен наибольший узел левого наследника, поскольку
        все левые узлы меньше или равны текущему по ключу. Таким образом наибольший узел находится в правой ветви
        левого наследника (движемся вниз по правой ветке левого наследника).

        Если же левого наследника нет, то ближайший меньший узел находится сверху в дереве по отношению
        к заданному. Пока заданный узел является левый наследником своего родителя, мы двигаемся вверх по веткам
        дерева, поскольку слева находятся меньшие элементы от родителя, а значит текущий узел меньше своего родителя,
        а нам нужен узел, который меньше текущего.
        """

        if node is None:
            node: Optional[Node] = self.root

        if node.left:
            return self.find_max(node.left)

        predecessor_node: Optional[Node] = node.parent
        while predecessor_node and node == predecessor_node.left:
            node = predecessor_node
            predecessor_node = node.parent

        return predecessor_node
