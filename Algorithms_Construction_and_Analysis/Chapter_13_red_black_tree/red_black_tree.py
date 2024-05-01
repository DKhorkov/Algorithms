"""
Красно-черные деревья похожи на бинарные деревья поиска, одна их узлы имеют еще и цвета, а также у них есть
пять свойств, за счет которых гарантируется выполнение операций за асимптоматические O(log(n)) в наихудшем случае.

Суть красно-черных деревьев в создании приблизительно сбалансированного дерева, чтобы его левая и правая ветви
имели приблизительно равную глубину (свойство №4).

Свойства красно-черного дерева:
1) Каждый узел окрашен либо в красный, либо в черный цвет (в структуре данных узла появляется
дополнительное поле – бит цвета);
2) Корень окрашен в черный цвет;
3) Листья(так называемые NULL-узлы) окрашены в черный цвет;
4) Каждый красный узел должен иметь два черных дочерних узла. Нужно отметить, что у черного узла могут быть
черные дочерние узлы. Красные узлы в качестве дочерних могут иметь только черные;
5) Пути от узла к его листьям должны содержать одинаковое количество черных узлов(это черная высота).
"""

from typing import Any, Optional, List
from dataclasses import dataclass

from Algorithms_Construction_and_Analysis.Chapter_12_binary_search_tree.binary_search_tree import BinarySearchTree


@dataclass(frozen=True)
class Colors:
    BLACK: str = 'black'
    RED: str = 'red'


class Node:

    def __init__(self, color: str = Colors.BLACK, key: int = 0, value: Any = None, nil_node: bool = False) -> None:
        self.parent: Optional[Node] = None
        self.left: Optional[Node] = None
        self.color: str = color
        self.key: int = key
        self.value: Any = value
        self.right: Optional[Node] = None
        self._nil_node: bool = nil_node

    def __repr__(self) -> str:
        return f"Node(key={self.key}, value={self.value})"

    def is_nil_node(self) -> bool:
        return self._nil_node


class RedBlackTree(BinarySearchTree):

    def __init__(self) -> None:
        self._nil_node: Node = Node(nil_node=True)
        super().__init__(root=self._nil_node)

    def traverse(self, node: Node = 'root') -> List[Node]:
        """
        Обходим дерево так, чтобы список узлов вернулся в отсортированном по ключам порядке,
        что происходит за счет концепции бинарного дерева поиска.
        """

        if node == 'root':
            node: Optional[Node] = self.root

        if not node.is_nil_node():
            return self.traverse(node=node.left) + [node] + self.traverse(node=node.right)

        return []

    def _left_rotate(self, node: Node) -> None:
        """
        Метод поворота, необходимый для основных операций, который будет изменять структура красно-черного дерева с
        сохранением его свойств.

        При выполнении левого поворота предполагается, что полученный узел может быть любым, однако его правый дочерний
        узел НЕ может быть нулевым (NilNode).

        Левый поворот выполняется "вокруг" связи между полученным узлом (x) и его правым дочерним узлом (y):
        правый дочерний узел (y) занимает место полученного узла (x), полученный узел (x) становится левым
        дочерним узлом своего бывшего правого дочернего узла (y), а бывший левый дочерний узел (z)
        бывшего правого дочернего узла (y) от нашего полученного узла (x) становится правым дочерним узлом
        полученного узла (x).
        """

        # Установка y и превращение левого поддерева y в правое поддерево x:
        y = node.right
        node.right = y.left

        # У нулевого узла не может быть родителя:
        if not y.left.is_nil_node():
            y.left.parent = node

        # Передача родителя x узлу y:
        y.parent = node.parent
        if node.parent.is_nil_node():
            self.root = y
        elif node == node.parent.left:
            node.parent.left = y
        else:
            node.parent.right = y

        # Размещение x в качестве левого дочернего узла y:
        y.left = node
        node.parent = y

    def _right_rotate(self, node: Node) -> None:
        """
        Является решением задания 13.2.1.

        Метод поворота, необходимый для основных операций, который будет изменять структура красно-черного дерева с
        сохранением его свойств.

        Делает обратное изменение структуры красно-черного дерева от self._left_rotate().
        """

        # Установка x и превращение правого поддерева x в левое поддерево y:
        x = node.left
        node.left = x.right

        # У нулевого узла не может быть родителя:
        if not x.right.is_nil_node():
            x.right.parent = node

        # Передача родителя y узлу x:
        x.parent = node.parent
        if node.parent.is_nil_node():
            self.root = x
        elif node == node.parent.left:
            node.parent.left = x
        else:
            node.parent.right = x

        # Размещение y в качестве правого дочернего узла x:
        x.right = node
        node.parent = x

    def insert(self, key: int, value: Any = None) -> None:
        """
        Метод в большей части повторяем метод вставки из бинарного дерева поиска, но с учетом того, что теперь
        корень всегда существует,но может быть NilNode.

        Также в конце метода применяется self._insert_fixup() для нормализации структуры красно-черного дерева, в
        соответствии с которой должны сохраняться все свойства красно-черного дерева.

        Цвет нового узла всегда красный, поскольку черный цвет нарушает свойство №5 красно-черного
        дерева.
        """

        new_node: Node = Node(key=key, value=value, color=Colors.RED)
        parent: Node = self._nil_node
        temp: Node = self.root
        while not temp.is_nil_node():
            parent = temp
            if new_node.key < temp.key:
                temp = temp.left
            else:
                temp = temp.right

        new_node.parent = parent

        if parent.is_nil_node():
            self.root = new_node
        elif new_node.key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node

        # Сохранение свойства №3 красно-черного дерева:
        new_node.left = self._nil_node
        new_node.right = self._nil_node

        # Нормализации структуры красно-черного дерева:
        self._insert_fixup(node=new_node)

    def _insert_fixup(self, node: Node) -> None:
        """
        Данный метод занимается исключительно поддержанием свойств красно-черного дерева после добавление в дерево
        нового узла. После выполнения метода self.insert() могут быть нарушены только свойства №2 и №4.

        Всего существует три случая в ходе исправления нарушения свойства №4:
        1) Дядя (y) нового узла (z) является красным (как и z);
        2) Дядя (y) нового узла (z) является черным (а z красным), а также z является правым дочерним
        узлом своего отца (x);
        3) Дядя (y) нового узла (z) является черным (а z красным), а также z является левым дочерним
        узлом своего отца (x).
        """

        parent: Node = node.parent
        while parent.color == Colors.RED:  # Если цвет родителя черный, то свойство №4 не нарушается.
            grandfather: Node = parent.parent
            if parent == grandfather.left:
                uncle: Node = grandfather.right

                # Первый случай:
                if uncle.color == Colors.RED:
                    # Меняем цвета на противоположные для трех узлов:
                    parent.color = Colors.BLACK
                    uncle.color = Colors.BLACK
                    grandfather.color = Colors.RED

                    # Теперь не обходимо работать с дедом в следующей итерации с сохранением инварианта:
                    node = grandfather
                    parent = node.parent
                else:
                    # Второй случай, который приводится к третьему случаю:
                    if node == parent.right:
                        node = parent
                        self._left_rotate(node=node)

                    """
                    Третий случай. Меняем цвета на противоположные для всех, кроме дяди (уже черный), 
                    чтобы не нарушать свойство №4.
                    """
                    parent.color = Colors.BLACK
                    grandfather.color = Colors.RED
                    self._right_rotate(node=grandfather)
            else:
                uncle: Node = grandfather.left

                # Первый случай:
                if uncle.color == Colors.RED:
                    # Меняем цвета на противоположные для трех узлов:
                    parent.color = Colors.BLACK
                    uncle.color = Colors.BLACK
                    grandfather.color = Colors.RED

                    # Теперь не обходимо работать с дедом в следующей итерации с сохранением инварианта:
                    node = grandfather
                    parent = node.parent
                else:
                    # Второй случай, который приводится к третьему случаю:
                    if node == parent.left:
                        node = parent
                        self._right_rotate(node=node)

                    """
                    Третий случай. Меняем цвета на противоположные для всех, кроме дяди (уже черный), 
                    чтобы не нарушать свойство №4.
                    """
                    parent.color = Colors.BLACK
                    grandfather.color = Colors.RED
                    self._left_rotate(node=grandfather)

        # Восстановление свойства №2 красно-черного дерева:
        self.root.color = Colors.BLACK

    def delete(self, key: int) -> None:
        """
        Метод в большей части повторяем метод удаления из бинарного дерева поиска, но с учетом того, что теперь
        родитель всегда существует,но может быть NilNode, а также с учетом цвета удаляемого узла.

        Так, чтобы восстановить потенциально нарушенные свойства красно-черного дерева, в конце метода вызывается
        self._delete_fixup().
        """

        node_to_delete: Node = self.search(key=key)
        original_color: str = node_to_delete.color

        if node_to_delete.left.is_nil_node():
            temp_node: Node = node_to_delete.right
            self._transplant(to_delete=node_to_delete, to_transplant=node_to_delete.right)
        elif node_to_delete.right.is_nil_node():
            temp_node: Node = node_to_delete.left
            self._transplant(to_delete=node_to_delete, to_transplant=node_to_delete.left)
        else:
            node_to_transplant = self.find_min(node=node_to_delete.right)
            original_color = node_to_transplant.color
            temp_node: Node = node_to_transplant.right

            if node_to_delete == node_to_transplant.parent:
                temp_node.parent = node_to_transplant
            else:
                self._transplant(to_delete=node_to_transplant, to_transplant=node_to_transplant.right)
                node_to_transplant.right = node_to_delete.right
                node_to_transplant.right.parent = node_to_transplant

            self._transplant(to_delete=node_to_delete, to_transplant=node_to_transplant)
            node_to_transplant.left = node_to_delete.left
            node_to_transplant.left.parent = node_to_transplant
            node_to_transplant.color = node_to_delete.color

        # Только удаление узла черного цвета могло нарушить свойств красно-черного дерева:
        if original_color == Colors.BLACK:
            self._delete_fixup(node=temp_node)

    def _delete_fixup(self, node: Node) -> None:
        """
        Данный метод занимается исключительно поддержанием свойств красно-черного дерева после удаления из дерева
        узла.

        Всего существует четыре случая в ходе исправления нарушения свойств:
        1) Брат (w) удаляемого узла (z) является красным;
        2) Брат (w) удаляемого узла (z) является черным, а также оба его дочерних узла являются черными;
        3) Брат (w) удаляемого узла (z) является черным, его левый дочерний узел является красным, а правый черным;
        4) Брат (w) удаляемого узла (z) является черным, а его правый дочерний узел является красным.
        """

        # Если удаляется красный узел, то никакие свойства не нарушаются:
        while node != self.root and node.color == Colors.BLACK:
            if node == node.parent.left:
                brother: Node = node.parent.right

                # Первый случай, который преобразуется во второй, третий или четвертый случай и обрабатывается далее:
                if brother.color == Colors.RED:
                    brother.color = Colors.BLACK
                    node.parent.color = Colors.RED
                    self._left_rotate(node=node.parent)
                    brother = node.parent.right

                # Второй случай:
                if brother.left.color == Colors.BLACK and brother.right.color == Colors.BLACK:
                    brother.color = Colors.RED
                    node = node.parent
                else:
                    # Третий случай, который преобразуется в четвертый:
                    if brother.right.color == Colors.BLACK:
                        brother.left.color = Colors.BLACK
                        brother.color = Colors.RED
                        self._right_rotate(node=brother)
                        brother = node.parent.right

                    # Четвертый случай:
                    brother.color = node.parent.color
                    node.parent.color = Colors.BLACK
                    brother.right.color = Colors.BLACK
                    self._left_rotate(node=node.parent)
                    node = self.root
            else:
                brother: Node = node.parent.left

                # Первый случай, который преобразуется во второй, третий или четвертый случай и обрабатывается далее:
                if brother.color == Colors.RED:
                    brother.color = Colors.BLACK
                    node.parent.color = Colors.RED
                    self._right_rotate(node=node.parent)
                    brother = node.parent.left

                # Второй случай:
                if brother.right.color == Colors.BLACK and brother.left.color == Colors.BLACK:
                    brother.color = Colors.RED
                    node = node.parent
                else:
                    # Третий случай, который преобразуется в четвертый:
                    if brother.left.color == Colors.BLACK:
                        brother.right.color = Colors.BLACK
                        brother.color = Colors.RED
                        self._left_rotate(node=brother)
                        brother = node.parent.left

                    # Четвертый случай:
                    brother.color = node.parent.color
                    node.parent.color = Colors.BLACK
                    brother.left.color = Colors.BLACK
                    self._right_rotate(node=node.parent)
                    node = self.root

        node.color = Colors.BLACK

    def _transplant(self, to_delete: Node, to_transplant: Node) -> None:
        """
        Метод в большей части повторяем метод пересадки из бинарного дерева поиска, но с учетом того, что теперь
        родитель всегда существует,но может быть NilNode.

        Также в конце метода производится безусловное переопределение родителя узлу для пересадки,
        потому что он всегда существует, хоть и может быть NilNode.
        """

        if to_delete.parent.is_nil_node():
            self.root = to_transplant
        elif to_delete == to_delete.parent.left:
            to_delete.parent.left = to_transplant
        else:
            to_delete.parent.right = to_transplant

        to_transplant.parent = to_delete.parent


if __name__ == '__main__':
    tree: RedBlackTree = RedBlackTree()
    tree.insert(key=1)
    tree.insert(key=5)
    tree.insert(key=2)
    tree.insert(key=3)
    tree.insert(key=6)
    tree.insert(key=4)
    tree.insert(key=7)
    print(tree.traverse())
    print(tree.search(key=1))
    tree.delete(key=6)
    print(tree.traverse())


