from abc import ABCMeta, abstractmethod


class Subject(metaclass=ABCMeta):
    @abstractmethod
    def run(self):
        pass


class Proxy(Subject):
    def __init__(self, real_algorithm):
        self._algorithm = real_algorithm

    def run(self):
        print('do something (before)')
        self._algorithm.run()
        print('do something (after)')


class Algorithm(Subject):
    def run(self):
        print('hello')


if __name__ == "__main__":
    real_subject = Algorithm()
    proxy = Proxy(real_subject)
    proxy.run()