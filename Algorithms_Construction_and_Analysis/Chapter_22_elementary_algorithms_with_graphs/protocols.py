from typing import Protocol, Any


class Prototype(Protocol):
    """
    Используем паттерн Прототип, чтобы не изменять полученные графы, а работать с их копиями.
    """

    def clone(self) -> Any:
        raise NotImplementedError
