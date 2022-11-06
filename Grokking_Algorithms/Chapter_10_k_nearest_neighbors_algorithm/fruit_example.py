"""There are some types of fruit, which are already in list. Now we added new fruit and would like to know, which
type of fruit is it"""


class KNearestFruitExample:

    def __init__(self):
        self.apple = {'name': 'apple', 'color': 3, 'size': 3}
        self.banana = {'name': 'banana', 'color': 1, 'size': 5}
        self.strawberry = {'name': 'strawberry', 'color': 4, 'size': 2}
        self.cherry = {'name': 'cherry', 'color': 5, 'size': 1}
        self.mango = {'name': 'mango', 'color': 2, 'size': 4}
        self.fruits = [self.apple, self.banana, self.strawberry, self.cherry, self.mango]

    @staticmethod
    def check_input(user_input):
        while not user_input.isdecimal() or len(user_input) != 2:
            user_input = input('\nError! Please input color (from 1 to 5. Yellow is 1, Red is 5, between is 2, 3, 4)\n'
                               'and size (from 1 to 5. Small is 1, Big is 5, between is 2, 3, 4) of fruit like in'
                               'this example (25): ')
        return [int(num) for num in user_input]

    def main(self):
        our_fruit = self.check_input(input('Please input color (from 1 to 5. Yellow is 1, Red is 5, between is 2, 3, '
                                           '4)\nand size (from 1 to 5. Small is 1, Big is 5, between is 2, 3, '
                                           '4) of fruit like in this example (25): '))
        nearest = {'name': None, 'color': float("inf"), 'size': float("inf"), 'similarities': float("inf")}
        for fruit in self.fruits:
            similarities = ((fruit['color'] - our_fruit[0]) ** 2 + (fruit['size'] - our_fruit[1]) ** 2) ** 0.5
            if nearest['similarities'] > similarities:
                nearest = fruit
                nearest['similarities'] = similarities
        print(f"\nSeems like the most similar fruit to yours is {nearest['name']}!")


if __name__ == '__main__':
    k_nearest_fruit_example = KNearestFruitExample()
    k_nearest_fruit_example.main()
