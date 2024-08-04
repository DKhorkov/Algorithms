from enum import Enum


class GraphNodeColors(str, Enum):
    """
    Цвета узлов графа не являются обязательными, однако используются для упрощения понимания.
    """

    WHITE = 'white'  # Узел графа не открыт
    GREY = 'grey'  # Узел графа открыт, но не исследован
    BLACK = 'black'  # Узел графа исследован
