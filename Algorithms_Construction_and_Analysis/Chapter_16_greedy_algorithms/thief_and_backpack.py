"""
Жадные алгоритмы применяются для оптимизации и похожи на алгоритмы из динамического программирования тем, что
для их реализации необходима оптимальная подструктура. Задача демонстрирует оптимальную подструктуру, если в ее
оптимальном решении содержатся оптимальные решения подзадач.

Однако помимо оптимальной подструктуры, для реализации жадного алгоритма необходимо удовлетворение его свойства:
глобальное оптимальное решение можно получить делая локальный оптимальный (жадный) выбор.

Таким образом, динамическое программирование основано на нахождении оптимального решения, вычисляя все оптимальные
решения подзадач, а жадные алгоритмы выбирают оптимальный текущий выбор и переходят к следующей подзадаче.

Хорошим примером сравнения жадного алгоритма и динамического программирования является задача о воре и рюкзаке,
представленная в двух версиях. В обеих версиях у вора имеет рюкзак, который может вместить определенное количество
веса (целое число) украденных товаров. Также есть несколько товаров, каждый из которых имеет определенный вес
(целое число) и стоимость (целое число). Однако:
1) Дискретная задача - вор может положить вещь только целиком;
2) Континуальная задача - может разделять предметы.

Чтобы сделать оптимальный локальный выбор - товары будут отсортированы на основе соотношения цена/вес.

В данном примере первая задача может быть решена с помощью динамического программирования, но не жадного алгоритма,
поскольку останется место в рюкзаке и совокупность оптимальных локальных решений не будет оптимальным глобальным
решением. А вот вторая задача может быть решена с помощью жадного алгоритма, в чем мы и убедимся.
"""

from dataclasses import dataclass
from typing import Self, List


@dataclass(frozen=True)
class Item:
    weight: int
    worth: int

    def divide(self, available_weight: int) -> Self:
        return Item(
            weight=available_weight,
            worth=self.worth // self.weight * available_weight
        )


class BackpackIsFullError(Exception):
    def __init__(self, msg='Backpack is full', *args, **kwargs):
        super().__init__(msg, *args, **kwargs)


class DiscreteBackpack:

    def __init__(self, capacity: int) -> None:
        self._capacity: int = capacity
        self._weight: int = 0
        self._worth: int = 0

    def stole(self, item: Item) -> None:
        if not self.can_stole(item=item):
            raise BackpackIsFullError

        self._weight += item.weight
        self._worth += item.worth

    def is_full(self) -> bool:
        return self._weight == self._capacity

    def can_stole(self, item: Item) -> bool:
        return self._weight + item.weight < self._capacity

    @property
    def worth(self) -> int:
        return self._worth

    @property
    def weight(self) -> int:
        return self._weight


class ContinuumBackpack(DiscreteBackpack):

    def _calculate_free_weight(self) -> int:
        return self._capacity - self._weight

    def stole(self, item: Item) -> None:
        if self.is_full():
            raise BackpackIsFullError

        item_to_stole: Item = item
        free_weight: int = self._calculate_free_weight()
        if item.weight > free_weight:
            item_to_stole = item.divide(free_weight)

        self._weight += item_to_stole.weight
        self._worth += item_to_stole.worth


if __name__ == '__main__':
    gold_bar: Item = Item(worth=60, weight=10)
    silver_bar: Item = Item(worth=100, weight=20)
    bronze_bar: Item = Item(worth=120, weight=30)

    jewelry_shop_inventory: List[Item] = [gold_bar, silver_bar, bronze_bar]  # Already sorted
    discrete_backpack: DiscreteBackpack = DiscreteBackpack(capacity=50)
    continuum_backpack = ContinuumBackpack(capacity=50)

    for item in jewelry_shop_inventory:
        if discrete_backpack.can_stole(item=item):
            discrete_backpack.stole(item=item)

        if not continuum_backpack.is_full():
            continuum_backpack.stole(item=item)

    print(f'DiscreteBackpack stolen worth is {discrete_backpack.worth} with weight {discrete_backpack.weight}')
    print(f'ContinuumBackpack stolen worth is {continuum_backpack.worth} with weight {continuum_backpack.weight}')
