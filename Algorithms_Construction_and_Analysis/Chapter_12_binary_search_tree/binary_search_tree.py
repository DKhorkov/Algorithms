"""
Бинарное дерево поиска - это структура, где ключи всех левых ветвей меньше или равны родительскому, а ключи всех
правых ветвей больше или равны родительскому.

Все основные операции (вставка, поиск, удаление, максимум, минимум, родитель и наследник)
выполняются за асимптоматические O(h), где h - высота дерева = O(log(n)),
а обход всего дерева за O(n), где n - количество узлов в дереве.
"""

from typing import Optional, List, Any


class Node:

    def __init__(self, key: int, value: Any = None) -> None:
        self.parent: Optional[Node] = None
        self.left: Optional[Node] = None
        self.key: int = key
        self.value: Any = value
        self.right: Optional[Node] = None

    def __repr__(self) -> str:
        return f"Node(key={self.key}, value={self.value})"


class BinarySearchTree:

    def __init__(self, root: Optional[Node] = None) -> None:
        self.root: Optional[Node] = root

    def traverse(self, node: Node = 'root') -> List[Node]:
        """
        Обходим дерево так, чтобы список узлов вернулся в отсортированном по ключам порядке,
        что происходит за счет концепции бинарного дерева поиска.
        """

        if node == 'root':
            node: Optional[Node] = self.root

        if node:
            return self.traverse(node=node.left) + [node] + self.traverse(node=node.right)

        return []

    def search(self, key: int, node: Node = 'root') -> Optional[Node]:
        """
        Если дерево пустое или узла с искомым ключом в дереве нет, то получим NoneType.
        Если искомый ключ меньше ключа родительского узла, то по определению бинарного дерева он может
        находиться только в левом узле наследнике. Если же он больше родительского, то в правом.
        Если искомый ключ равен ключу узла, значит это и есть искомый узел.
        """

        if node == 'root':
            node: Optional[Node] = self.root

        if not node or node.key == key:
            return node

        if node.key < key:
            return self.search(key=key, node=node.right)
        else:
            return self.search(key=key, node=node.left)

    def find_max(self, node: Optional[Node] = 'root') -> Optional[Node]:
        """
        Является выполнением задачи 12.2.2.

        Если у нас нет узла или его правого наследника, то возвращаем пустой узел.
        В ином случае максимум находится в самом правом узле наследнике на последнем уровне бинарного дерева.
        """

        if node == 'root':
            node: Optional[Node] = self.root

        if not node or not node.right:
            return node

        return self.find_max(node=node.right)

    def find_min(self, node: Optional[Node] = 'root') -> Optional[Node]:
        """
        Является выполнением задачи 12.2.2.

        Если у нас нет узла или его левого наследника, то возвращаем пустой узел.
        В ином случае минимум находится в самом левом узле наследнике на последнем уровне бинарного дерева.
        """

        if node == 'root':
            node: Optional[Node] = self.root

        if not node or not node.left:
            return node

        return self.find_min(node=node.left)

    def successor(self, node: Optional[Node] = 'root') -> Optional[Node]:
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

        if node == 'root':
            node: Optional[Node] = self.root

        if node.right:
            return self.find_min(node=node.right)

        successor_node: Optional[Node] = node.parent
        while successor_node and node == successor_node.right:
            node = successor_node
            successor_node = node.parent

        return successor_node

    def predecessor(self, node: Optional[Node] = 'root') -> Optional[Node]:
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

        if node == 'root':
            node: Optional[Node] = self.root

        if node.left:
            return self.find_max(node=node.left)

        predecessor_node: Optional[Node] = node.parent
        while predecessor_node and node == predecessor_node.left:
            node = predecessor_node
            predecessor_node = node.parent

        return predecessor_node

    def insert(self, key: int, value: Any = None) -> None:
        """
        Создаем новый узел и продвигаемся по дереву вниз до тех пор, пока не найдем пустой дочерний узел,
        куда должен будет быть вставлен новый узел.

        Временный узел служит как указатель в поисках пустого узла, куда будет помещен новый узел.
        Далее связываем новый узел и найденного родителя по ключу.
        Если же родителя нет, то новый узел должен стать корневым в дереве.
        """

        new_node: Node = Node(key=key, value=value)
        parent: Optional[Node] = None
        temp: Optional[Node] = self.root
        while temp:
            parent = temp
            if new_node.key < temp.key:
                temp = temp.left
            else:
                temp = temp.right

        new_node.parent = parent

        if not parent:
            self.root = new_node
        elif new_node.key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node

    def delete(self, key: int) -> None:
        """
        Процедура удаления узла из дерева является самой сложной, поскольку здесь имеются 4 вариант развития событий:
        1) У удаляемого узла нет дочерних узлов, тогда мы просто удаляем его, делая дерево пустым,
        а его корень NoneType;
        2) У удаляемого узла есть только правый дочерний узел, тогда мы заменяем удаляемый узел его
        правым дочерним узлом и связываем правый дочерний узел с родителем удаляемого узла;
        3) У удаляемого узла есть только левый дочерний узел, тогда мы заменяем удаляемый узел его
        левым дочерним узлом и связываем левым дочерний узел с родителем удаляемого узла;
        4) У удаляемого узла есть и левый, и правый дочерние узлы. В таком случае мы ищем в правой ветке удаляемого узла
        такой узел, у которого не будет левого дочернего узла (поскольку левый дочерний узел меньше удаляемого,
        а любой узел в правой ветке больше удаляемого, то мы сможем заменить удаляемый узел искомым).

        4.1. Если искомый узел является правым дочерним узлом удаляемого, то мы просто заменяем удаляемый узел его
        правым дочерним узлом и делаем левый дочерний узел удаляемого узла левым дочерним узлом правого дочернего узла,
        который теперь заменил удаляемый узел.

        4.2. В ином случае, мы ищем в правой ветке удаляемого узла нужный нам узел. Затем заменяем найденный узел его
        правым дочерним узлом для сохранения иерархии дерева. После чего заменяем удаляемый узел найденным узлом, и
        также делаем левый дочерний узел удаляемого узла левым дочерним узлом найденного узла,
        который теперь заменил удаляемый узел.
        """

        node_to_delete: Optional[Node] = self.search(key=key)
        if not node_to_delete:
            raise KeyError

        # Обработка первого и второго случая. Если node_to_delete.right == None - это первый случай:
        if not node_to_delete.left:
            self._transplant(to_delete=node_to_delete, to_transplant=node_to_delete.right)

        # Обработка третьего случая:
        elif not node_to_delete.right:
            self._transplant(to_delete=node_to_delete, to_transplant=node_to_delete.left)

        # Обработка 4 случая
        else:
            """
            Поскольку минимум находится в самом левом узле наследнике на последнем уровне бинарного дерева,
            то мы найдем минимальный узел в правой ветке удаляемого узла. Если у него нет левого дочернего узла, 
            значит он минимальный в текущей ветке
            """
            node_to_transplant: Node = self.find_min(node=node_to_delete.right)

            # Случай 4.2.
            if node_to_transplant.parent != node_to_delete:
                # Заменяем найденный узел его правым дочерним узлом для сохранения иерархии дерева
                self._transplant(to_delete=node_to_transplant, to_transplant=node_to_transplant.right)

                # Делаем правую ветвь удаляемого узла правой ветвью найденного узла.
                node_to_transplant.right = node_to_delete.right
                node_to_transplant.right.parent = node_to_transplant

            """
            Общая часть для пунктов 4.1 и 4.2 - замена удаляемого узла найденным и 
            привязка левого дочернего узла удаляемого узла к найденному узлу.
            """
            self._transplant(to_delete=node_to_delete, to_transplant=node_to_transplant)
            node_to_transplant.left = node_to_delete.left
            node_to_delete.left.parent = node_to_transplant

    def _transplant(self, to_delete: Node, to_transplant: Optional[Node]) -> None:
        """
        Данный метод заменяет один узел другим и нужен для процедуры удаления узла из дерева.

        Если у узла, который должен быть удален, нет родителя, то новый узел становится корневым,
        поскольку удаляемый узел был корневым.

        В ином случае, идет проверка, является ли удаляемый узел левым или правым дочерним узлом своего родителя,
        чтобы новый узел занял его место.

        Если новый узел не является NoneType, то необходимо привязать его к родителю, коим будет являться родитель
        удаляемого узла.
        """

        if not to_delete.parent:
            self.root = to_transplant
        elif to_delete.parent.left == to_delete:
            to_delete.parent.left = to_transplant
        else:
            to_delete.parent.right = to_transplant

        if to_transplant:
            to_transplant.parent = to_delete.parent


if __name__ == '__main__':
    values: List[int] = [2, 8, 4, 3, 12, 10, 5, 7, 1, 9]
    tree: BinarySearchTree = BinarySearchTree()

    for value in values:
        tree.insert(key=value)

    print(*tree.traverse())

    print(tree.find_min())
    print(tree.find_max())

    searched: Node = tree.search(key=3)
    print(searched)
    successor: Node = tree.successor(node=searched)
    print(successor)
    predecessor: Node = tree.predecessor(node=searched)
    print(predecessor)

    tree.delete(key=1)  # 1 случай
    print(*tree.traverse())
    tree.delete(key=2)  # 4 случай
    print(*tree.traverse())
