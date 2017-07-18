from abc import ABCMeta, abstractmethod


class Model(metaclass=ABCMeta):
    @abstractmethod
    def get_product(self, item):
        pass


class View(metaclass=ABCMeta):
    @abstractmethod
    def show_item_list(self, item_list):
        pass

    @abstractmethod
    def show_item_information(self, item_name, item_info):
        pass


class Product(Model):
    products = {
        'milk':   {'price': 1.50, 'quantity': 10},
        'eggs':   {'price': 0.20, 'quantity': 100},
        'cheese': {'price': 2.00, 'quantity': 10}
    }

    def get_product(self, product):
        return self.products[product]


class Console(View):
    def show_item_list(self, item_list):
        print('Items list: ')
        for item in item_list:
            print('-', item)

    def show_item_information(self, item_name, item_info):
        print('Item: {0}, price = {1}, quantity = {2}'
              .format(item_name, item_info['price'], item_info['quantity']))


class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def show_items(self):
        items = self.model.products
        self.view.show_item_list(items)

    def show_item_information(self, item_name):
        try:
            item_info = self.model.get_product(item_name)
            self.view.show_item_information(item_name, item_info)
        except KeyError:
            print('Item *{0}* not found!'.format(item_name))


if __name__ == '__main__':
    model = Product()
    view = Console()
    controller = Controller(model, view)

    controller.show_items()
    controller.show_item_information('cheese')
    controller.show_item_information('eggs')
    controller.show_item_information('milk')
    controller.show_item_information('arepas')