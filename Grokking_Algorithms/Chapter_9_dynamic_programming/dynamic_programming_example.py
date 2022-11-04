"""Задача с помощью динамического программирования найти оптимальный набор вещей, которые могут поместитсья в рюкзак
заданного размера на примере задачи из книги."""
from configs import items


class DynamicProgramming:

    def __init__(self, size):
        self.package_size = size
        self.items = items
        self.max = {}

    def create_max_keys(self) -> None:
        """Function creates template of max amounts dict for every weight number in range of package size, which was
        given in init."""
        size = self.package_size
        for i in range(self.package_size):
            self.max[size] = 0
            size -= 1

    def get_alternative(self, item: dict, current_weight: int) -> dict:
        """Function takes 3 mandatory params and calculates the best alternative for given weight number.
        Returns alternative (dict)."""
        if current_weight > 0 and item['name'] not in self.max[current_weight]['name']:
            alternative = {'name': f"{self.max[current_weight]['name']} and " + item['name'],
                           'amount': self.max[current_weight]['amount'] + item['amount']}
        else:
            try:
                alternative = {'name': self.max[current_weight]['name'],
                               'amount': self.max[current_weight]['amount']}
            except KeyError:
                alternative = {'name': None, 'amount': 0}
        return alternative

    def main_comparison(self, item: dict, weight: int, current_weight: int) -> None:
        """Main logic function of dynamic algorithm. Takes 3 mandatory params and compares amount of item with the
        alternative amount to check, which is greater. Then the greatest amount will be putted in max dict."""
        try:
            current_weight -= item['weight']
            alternative = self.get_alternative(item, current_weight)
            if self.max[weight]['amount'] < item['amount']:
                self.max[weight] = {'name': item['name'], 'amount': item['amount']}
                if current_weight > 0 and self.max[current_weight]['name'] != item['name']:
                    self.max[weight]['amount'] += self.max[current_weight]['amount']
                    self.max[weight]['name'] += f" and {self.max[current_weight]['name']}"
            elif self.max[weight]['amount'] < alternative['amount']:
                self.max[weight] = {'name': alternative['name'], 'amount': alternative['amount']}
        except TypeError:
            try:
                if self.max[weight]['amount'] < item['amount']:
                    self.max[weight] = {'name': item['name'], 'amount': item['amount']}
            except TypeError:
                if self.max[weight] < item['amount']:
                    self.max[weight] = {'name': item['name'], 'amount': item['amount']}

    def main(self):
        """Main function of dynamic algorithm. Iterates through items and fill max dict. As the result, prints a string,
        in which informs user, what will be the best pack to fill a backpack with the predetermined weight and the
        amount of calculated pack."""
        self.create_max_keys()
        for item in self.items:
            for weight in sorted(self.max):
                current_weight = weight
                if weight >= item['weight']:
                    self.main_comparison(item, weight, current_weight)
        print(f"To fill a backpack with a volume of {self.package_size} kilos, it is best to put "
              f"{self.max[self.package_size]['name']} in it to achieve the maximum cost, which will be "
              f"{self.max[self.package_size]['amount']}$!")


if __name__ == '__main__':
    dp = DynamicProgramming(10)
    dp.main()
