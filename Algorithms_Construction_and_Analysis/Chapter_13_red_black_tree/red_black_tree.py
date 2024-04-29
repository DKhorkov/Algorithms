"""
Красно-черные деревья похожи на бинарные деревья поиска, одна их узлы имеют еще и цвета, а также у них есть
пять свойств, за счет которых гарантируется выполнение операций за асимптоматические O(log(n)) в наихудшем случае.

Свойства красно-черного дерева:
1) Каждый узел окрашен либо в красный, либо в черный цвет (в структуре данных узла появляется
дополнительное поле – бит цвета);
2) Корень окрашен в черный цвет;
3) Листья(так называемые NULL-узлы) окрашены в черный цвет;
4) Каждый красный узел должен иметь два черных дочерних узла. Нужно отметить, что у черного узла могут быть
черные дочерние узлы. Красные узлы в качестве дочерних могут иметь только черные;
5) Пути от узла к его листьям должны содержать одинаковое количество черных узлов(это черная высота).
"""

from typing import Any, Optional
from dataclasses import dataclass


@dataclass(frozen=True)
class Colors:
    BLACK: str = 'black'
    RED: str = 'red'


class Node:

    def __init__(self, color: Colors = Colors.BLACK, key: int = 0, value: Any = None, nil_node: bool = False) -> None:
        self.parent: Optional[Node] = None
        self.left: Optional[Node] = None
        self.color: Colors = color
        self.key: int = key
        self.value: Any = value
        self.right: Optional[Node] = None
        self._nil_node: bool = nil_node

    def is_nil_node(self) -> bool:
        return self._nil_node


class RedBlackTree:

    def __init__(self) -> None:
        self.root: Node = Node()

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
