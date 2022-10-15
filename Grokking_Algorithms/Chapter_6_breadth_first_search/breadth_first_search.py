"""Задача найти ближайшего к нам продавца машин. Предположительно мы знаем, что его зовут Diggy.
Нужно выйти на него кратчайшим путем через свои связи или связи друзей"""

from collections import deque


class BreadthFirstSearch:

    def __init__(self):
        """Создаем взаимосвязи наши, наших друзей и друзей наших друзей для дальнейшего поиска продавца.
        Далее создаем очередь и добавляем в нее наших друзей. Также создаем список людей, которые уже проверены
        (изначально пустой), чтобы избежать бесконечного цикла и лишней работы, если у нас с друзьями есть
        общий друг."""
        self.connections = {'you': ['Bob', 'Sam', 'Joe'], 'Bob': ['Sam', 'Lucy', 'Maggy'],
                            'Sam': ['Andrew', 'Mikky', 'Marge'], 'Joe': ['Sergey', 'Konstantin', 'Diggy'],
                            'Jimmy': ['Tom'], 'Lucy': ['Andrew'], 'Maggy': ['Sew'], 'Andrew': ['Lue'], 'Mikky': ['Ben'],
                            'Marge': ['Ben'], 'Sergey': [], 'Konstantin': []}

        self.queue = deque()
        self.queue += self.connections['you']
        self.numeration = 0
        self.checked_persons = []

    def search(self):
        """Пока существует очередь, ищем в ней в порядке FIFO продавца машин. Если человек не продавец - то
        добавляем его друзей в очередь для дальнейшего поиска. Если человек продавец - возвращаем инфу,
        что нашли Diggy + количество людей, которых пришлось проверить до момента нахождения Diggy."""
        while self.queue:
            print(self.queue)
            self.numeration += 1
            person = self.queue.popleft()
            if person not in self.checked_persons:  # Если мы еще не проверили человека, то проверяем
                if person != 'Diggy':
                    self.queue += self.connections[person]
                    self.checked_persons.append(person)  # Добавляем в список проверенных, чтобы не повторять поиск
                    print(self.checked_persons)
                else:
                    return f"Found Diggy in {self.numeration} connections"
        else:
            return "No seller"


if __name__ == '__main__':
    search = BreadthFirstSearch()
    result = search.search()
    print(result)

