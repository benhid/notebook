from abc import ABCMeta, abstractmethod
import time


class Observable(object):
    def register(self, observer):
        pass

    def deregister(self, observer):
        pass

    def notify_all(self, *args, **kwargs):
        pass


class DefaultObservable(Observable):
    def __init__(self):
        self.observers = []

    def register(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)

    def deregister(self, observer):
        if observer in self.observers:
            self.observers.remove(observer)

    def notify_all(self, *args, **kwargs):
        for observer in self.observers:
            observer.update(*args, **kwargs)


class Observer(metaclass=ABCMeta):
    """ We want to ensure those Observer based classes will contain the update method. """
    @abstractmethod
    def update(self, *args, **kwargs):
        pass


class TimeObserver(Observer):
    def update(self, *args, **kwargs):
        current_time = kwargs['current_time']
        print("Compute time: ", current_time)


class Algorithm:
    def __init__(self, observable: Observable = DefaultObservable()):
        self.observable = observable
        self.current_time = None

    def update_progress(self):
        observable_data = {'current_time': self.current_time}
        self.observable.notify_all(**observable_data)

    def run(self):
        for i in range(0, 5):
            self.current_time = time.time()
            self.update_progress()


if __name__ == "__main__":
    example = Algorithm()
    time_observer = TimeObserver()

    example.observable.register(time_observer)
    example.run()
