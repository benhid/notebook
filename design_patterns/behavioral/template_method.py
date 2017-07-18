from abc import ABCMeta, abstractmethod


class Template(metaclass=ABCMeta):
    def run(self):
        print(self._primitive_operation_1(), self._primitive_operation_2())

    def _primitive_operation_1(self) -> str:
        return 'template'

    @abstractmethod
    def _primitive_operation_2(self) -> str:
        pass


class ConcreteClassOne(Template):
    def _primitive_operation_2(self) -> str:
        return 'one'


class ConcreteClassTwo(Template):
    def _primitive_operation_2(self) -> str:
        return 'two'


if __name__ == "__main__":
    concrete_class = ConcreteClassOne()
    concrete_class.run()

    concrete_class = ConcreteClassTwo()
    concrete_class.run()