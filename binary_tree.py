class Branch:

    """
        Данный класс представляет собой узел (микро-дерево), который имеет левую и правую ветки. Данные ветки также
        могут быть экземплярами данного класса.
    """

    def __init__(self, key: int) -> None:
        self.key = key
        self.left_branch = self.right_branch = None


class BinaryTree:

    """
        Основной класс-представление бинарного дерева.
    """

    def __init__(self) -> None:
        self.root = None  # Изначально корень дерева не задан

    def append_branch(self, new_branch: Branch) -> None:

        """
            Метод добавляет ветку к текущему дереву в соответствии с концепцией бинарного дерева в случае, если ветки
            с таким ключом еще не существует в текущем дереве.

            :param new_branch: Ветка, которая будет присоединена к текущему дереву.
            :return: None
        """

        if not self.root:  # Same as "if self.root is None"
            self.root = new_branch
            return

        branch_to_append_to, parent_branch, branch_found = self.__find_branch_by_key(
            branch=self.root,
            parent_branch=None,
            key=new_branch.key
        )

        if branch_to_append_to and not branch_found:
            if new_branch.key < branch_to_append_to.key:
                branch_to_append_to.left_branch = new_branch
            else:
                branch_to_append_to.right_branch = new_branch

    def __find_branch_by_key(
            self,
            branch: Branch,
            parent_branch: Branch | None,
            key: int
    ) -> tuple[Branch | None, Branch, bool]:

        """
            Данный метод пытается найти, существует ли ветка по заданному ключу.

            :param branch: Текущая ветка.
            :param parent_branch: Родительская ветка для той, от которой ищем ветку по ключу.
            :param key: Ключ, на основе которого определяется, куда будет добавлена новая ветка.
            :return: Ветку, к которой будет присоединена новая ветка, если в текущем дереве не была найдена ветка с
            указанным ключом, корень данной ветки и флаг, указывающий на то, была ли найдена ветка по ключу.
        """

        branch_found = False

        if not branch:
            return branch, parent_branch, branch_found

        elif key == branch.key:
            branch_found = True
            return branch, parent_branch, branch_found

        elif key < branch.key:
            if branch.left_branch:
                return self.__find_branch_by_key(branch=branch.left_branch, parent_branch=branch, key=key)

        elif key > branch.key:
            if branch.right_branch:
                return self.__find_branch_by_key(branch=branch.right_branch, parent_branch=branch, key=key)

        return branch, parent_branch, branch_found

    def remove_branch_by_key(self, key: int) -> None:

        """
            Данный метод удаляет ветку по заданному ключу, если ветка с таким ключом существует в текущем дереве.
            В зависимости от того, имеет ли ветка для удаления свои ветки, будет выполнен один из трех методов:
                1) Удалить лист (ветка без под-веток)
                2) Заменить удаляемую ветку на ее под-ветку
                3)

            :param key: Ключ, по которому будет произведен поиск ветки для дальнейшего удаления.
            :return: None
        """

        branch_to_delete, parent_branch, branch_found = self.__find_branch_by_key(
            branch=self.root,
            parent_branch=None,
            key=key
        )

        if not branch_found:
            return

        elif not branch_to_delete.left_branch and not branch_to_delete.right_branch:
            self.__delete_leaf(branch_to_delete=branch_to_delete, parent_branch=parent_branch)

        elif not branch_to_delete.left_branch or not branch_to_delete.right_branch:
            self.__replace_branch_to_delete_by_its_subbranch(
                branch_to_delete=branch_to_delete,
                parent_branch=parent_branch
            )

        else:
            self.__delete_branch_with_two_subbranches(branch_to_delete=branch_to_delete)

    @staticmethod
    def __delete_leaf(branch_to_delete: Branch, parent_branch: Branch) -> None:

        """
            Данный метод удаляет у родительской ветки текущую (ветку для удаления). Ветка (выбранная для удаления) не
            имеет под-веток, поэтому и называется листом дерева.

            :param branch_to_delete: Ветка для удаления.
            :param parent_branch: Родительская ветка.
            :return: None
        """

        if parent_branch.left_branch == branch_to_delete:
            parent_branch.left_branch = None

        elif parent_branch.right_branch == branch_to_delete:
            parent_branch.right_branch = None

    def __replace_branch_to_delete_by_its_subbranch(self, branch_to_delete: Branch, parent_branch: Branch) -> None:

        """
            Данный метод получает ветку для удаления, у которой есть только правая или левая под-ветка.
            Данная под-ветка заменит ветку для удаления.

            :param branch_to_delete: Ветка для удаления.
            :param parent_branch: Родительская ветка.
            :return: None
        """

        if branch_to_delete == parent_branch.right_branch:
            if branch_to_delete.right_branch:
                parent_branch.right_branch = branch_to_delete.right_branch

            elif branch_to_delete.left_branch:
                parent_branch.right_branch = branch_to_delete.left_branch

            else:
                self.__delete_leaf(branch_to_delete=branch_to_delete, parent_branch=parent_branch)

        elif branch_to_delete == parent_branch.left_branch:
            if branch_to_delete.right_branch:
                parent_branch.left_branch = branch_to_delete.right_branch

            elif branch_to_delete.left_branch:
                parent_branch.left_branch = branch_to_delete.left_branch

            else:
                self.__delete_leaf(branch_to_delete=branch_to_delete, parent_branch=parent_branch)

    def __delete_branch_with_two_subbranches(self, branch_to_delete: Branch) -> None:

        """
            Данный метод находит в правой под-ветке ветки для удаления ее минимальную под-ветку,
            чтобы заменить ключ ветки для удаления на ключ минимальной под-ветки.
            Далее метод удаляет эту под-ветку с минимальным значением из правой под-ветки удаляемой ветки, поскольку
            данное значение уже будет существовать ранее.

            :param branch_to_delete: Ветка для удаления.
            :return: None
        """

        min_key_branch, min_key_branch_parent = self.__find_min_key_branch(
            branch=branch_to_delete.right_branch,
            parent_branch=branch_to_delete
        )

        branch_to_delete.key = min_key_branch.key

        self.__replace_branch_to_delete_by_its_subbranch(
            branch_to_delete=min_key_branch,
            parent_branch=min_key_branch_parent
        )

    def __find_min_key_branch(self, branch: Branch, parent_branch: Branch) -> tuple[Branch, Branch]:

        """

            :param branch: Ветка, в которой ищем минимальное значение.
            :param parent_branch: Родительская ветка.
            :return: Возвращает минимальную ветку и ее родителя
        """

        if branch.left_branch:
            return self.__find_min_key_branch(branch=branch.left_branch, parent_branch=branch)

        return branch, parent_branch

    def draw_binary_tree(self, branch: Branch = None) -> None:

        """
            Данный метод выводит бинарное дерево в STDOUT.
            Если не была передана ветка, с которой отрисовать бинарное дерево, то будет отрисовано дерево с корня.

            :param branch: Ветка, с которой начинаем отрисовывать дерево.
            :return: None
        """

        print(end="\n\n")  # Отделяем дерево от следующих данный в STDOUT

        if not branch:
            parent_branches_list = [self.root]
        else:
            parent_branches_list = [branch]

        while parent_branches_list:
            subbranches_parent_branches_list = []
            for parent_branch in parent_branches_list:
                print(parent_branch.key, end=" ")

                if parent_branch.left_branch:
                    subbranches_parent_branches_list.append(parent_branch.left_branch)

                if parent_branch.right_branch:
                    subbranches_parent_branches_list.append(parent_branch.right_branch)

            print()  # Создаем пустую строку после отрисовки уровня под-веток

            # Обновляем список для отрисовки следующего уровня под-веток:
            parent_branches_list = subbranches_parent_branches_list

        print(end="\n\n")  # Отделяем дерево от следующих данный в STDOUT


if __name__ == '__main__':
    binary_tree = BinaryTree()
    values_list = [50, 42, 12, 3, 1, 18, 105, 92, 67, 30]

    for value in values_list:
        new_branch = Branch(key=value)
        binary_tree.append_branch(new_branch=new_branch)

    binary_tree.draw_binary_tree()

    binary_tree.remove_branch_by_key(key=42)
    binary_tree.draw_binary_tree()

    binary_tree.remove_branch_by_key(key=12)
    binary_tree.draw_binary_tree()