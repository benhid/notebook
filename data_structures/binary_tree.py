from abc import ABCMeta, abstractmethod
from typing import TypeVar

S = TypeVar('S')


class BasicNode(metaclass=ABCMeta):
    @abstractmethod
    def get_element(self):
        raise NotImplementedError

    @abstractmethod
    def get_right(self):
        raise NotImplementedError

    @abstractmethod
    def get_left(self):
        raise NotImplementedError

    @abstractmethod
    def set_element(self, element: int):
        raise NotImplementedError

    @abstractmethod
    def set_right(self, element: int):
        raise NotImplementedError

    @abstractmethod
    def set_left(self, element: int):
        raise NotImplementedError

    def __str__(self):
        return str(self.get_element())


class Node(BasicNode):
    def __init__(self, element: int):
        self._element = element
        self._left_node: Node = None
        self._right_node: Node = None

    def get_element(self) -> int:
        return self._element

    def get_right(self):
        return self._right_node

    def get_left(self):
        return self._left_node

    def set_element(self, element: int) -> None:
        self._element = element

    def set_right(self, element: int):
        self._right_node = Node(element=element)

    def set_left(self, element: int):
        self._left_node = Node(element=element)


class BinaryTree:
    def __init__(self, root: Node = None):
        self.root = root

    def is_empty(self) -> bool:
        return not self.root

    def insert(self, element: int) -> None:
        if self.is_empty():
            self.root = Node(element=element)
        else:
            self._insert(self.root, element)

    def _insert(self, node: Node, element) -> None:
        if element <= node.get_element():
            # Insert on the left
            if node.get_left():
                # If node has left...
                self._insert(node.get_left(), element)
            else:
                # ...else, set the left
                node.set_left(element)
        else:
            # Insert on the right
            if node.get_right():
                # If node has right...
                self._insert(node.get_right(), element)
            else:
                # ...else, set the right
                node.set_right(element)

    def delete(self, element) -> None:
        pass

    def find(self, element: int) -> Node:
        if self.is_empty():
            raise Exception('Tree is empty!')
        else:
            print('Searching...')
            return self._find(self.root, element)

    def _find(self, node: Node, element: int) -> Node:
        if element == node.get_element():
            print('Found!')
            return node
        elif element < node.get_element() and node.get_left() is not None:
            self._find(node.get_left(), element)
        elif element > node.get_element() and node.get_right() is not None:
            self._find(node.get_right(), element)

    def print_tree(self):
        if self.root is not None:
            self._print_tree(self.root)

    def _print_tree(self, node: Node):
        if node is not None:
            self._print_tree(node.get_left())
            print(str(node.get_element()))
            self._print_tree(node.get_right())


if __name__ == '__main__':
    bt = BinaryTree()
    bt.insert(2)
    bt.insert(8)
    bt.insert(10)
    bt.insert(1)
    bt.insert(12)

    print('a', bt.find(8))

    bt.print_tree()