class Singleton(object):
    _instances = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = object.__new__(cls, *args, **kwargs)
        return cls._instances[cls]


class Foo(Singleton):
    pass


if __name__ == '__main__':
    foo1 = Foo()
    foo2 = Foo()

    print(foo1 is foo2)
