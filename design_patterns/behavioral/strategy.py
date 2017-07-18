from abc import ABCMeta, abstractmethod


class Strategy(metaclass=ABCMeta):
    @abstractmethod
    def compute(self, number_one, number_two):
        pass


class AlgorithmAdd(Strategy):
    def compute(self, number_one, number_two):
        print(number_one+number_two)


class AlgorithmMultiply(Strategy):
    def compute(self, number_one, number_two):
        print(number_one*number_two)


class Context:
    def __init__(self, strategy):
        self._strategy = strategy

    def compute(self, number_one, number_two):
        self._strategy.compute(number_one, number_two)


if __name__ == "__main__":
    context = Context(strategy=AlgorithmAdd())
    context.compute(5,5)

    context = Context(strategy=AlgorithmMultiply())
    context.compute(5,5)