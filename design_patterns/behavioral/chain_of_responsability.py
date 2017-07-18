class Handler():
    def __init__(self, successor=None):
        self._successor = successor

    def can_handle(self, extension):
        pass

    def handle(self, extension):
        print(extension)

    def handle_request(self, extension):
        if self.can_handle(extension):
            self.handle(extension)
        elif self._successor is not None:
            self._successor.handle_request(extension)


class HandlerOne(Handler):
    def can_handle(self, extension):
        return extension == 'png'


class HandlerTwo(Handler):
    def can_handle(self, extension):
        return extension == 'pdf'


if __name__ == "__main__":
    concrete_handler_2 = HandlerTwo()
    concrete_handler_1 = HandlerOne(successor=concrete_handler_2)

    concrete_handler_1.handle_request('pdf')