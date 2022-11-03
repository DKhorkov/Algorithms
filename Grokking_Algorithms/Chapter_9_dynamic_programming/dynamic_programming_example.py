"""Задача с помощью динамического программирования найти оптимальный набор вещей, которые могут поместитсья в рюкзак
заданного размера на примере задачи из книги."""


class DynamicProgramming:

    def __init__(self, size):
        self.package_size = size
        self.guitar = {'name': 'guitar', 'weight': 1, 'amount': 1500}
        self.laptop = {'name': 'laptop', 'weight': 3, 'amount': 2000}
        self.recorder = {'name': 'recorder', 'weight': 4, 'amount': 3000}
        self.iphone = {'name': 'iphone', 'weight': 1, 'amount': 1600}
        self.alternative = {}
        self.items = [self.iphone, self.guitar, self.recorder, self.laptop]
        self.max = {}

    def create_max_keys_and_alternative(self):
        size = self.package_size
        for i in range(self.package_size):
            self.max[size] = 0
            self.alternative[size] = {'name': None, 'amount': 0}
            size -= 1

    def main(self):
        self.create_max_keys_and_alternative()
        for item in self.items:
            for weight in sorted(self.max):
                current_weight = weight
                if weight >= item['weight']:
                    try:
                        current_weight -= item['weight']
                        if current_weight > 0 and item['name'] not in self.max[current_weight]['name']:
                            alternative = {'name': f"{self.max[current_weight]['name']} and " + item['name'],
                                       'amount': self.max[current_weight]['amount'] + item['amount']}
                        elif current_weight > 0 and item['name'] not in self.alternative[current_weight]['name']:
                            alternative = {'name': f"{self.alternative[current_weight]['name']} and " + item['name'],
                                           'amount': self.alternative[current_weight]['amount'] + item['amount']}
                        else:
                            alternative = {'name': None, 'amount': 0}
                        if self.max[weight]['amount'] < item['amount']:
                            self.alternative[weight] = {'name': self.max[weight]['name'],
                                                        'amount': self.max[weight]['amount']}
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


if __name__ == '__main__':
    dp = DynamicProgramming(5)
    dp.main()
    print(dp.max)


