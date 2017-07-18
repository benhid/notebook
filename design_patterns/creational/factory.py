from abc import ABCMeta, abstractmethod


class ShapeFactory:
    @staticmethod
    def generate(sides: int):
        if sides == 0: return Circle()
        if sides == 4: return Square()
        assert 0, "Bad shape: sides must be either 0 or 4" + str(sides)


class Shape(metaclass=ABCMeta):
    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def erase(self):
        pass


class Circle(Shape):
    def draw(self):
        print("Circle draw")

    def erase(self):
        print("Circle erase")


class Square(Shape):
    def draw(self):
        print("Square draw")

    def erase(self):
        print("Square erase")


if __name__ == '__main__':
    generic_shape = ShapeFactory.generate(sides=4)
    generic_shape.draw()