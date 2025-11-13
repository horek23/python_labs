class Order:

    orders_quantity = 0

    def __init__(self,items):
        Order.orders_quantity += 1
        self.items = dict(items)

    def get_data(self):
        return self.items

    def set_data(self,items):
        self.items = dict(items)

    def add_item(self,key, price):
        self.items[key] = price
        return self.items.items()

    def remove_item(self,key):
        confirmation = input("Вы уверены, что хотите удалить этот товар (ответьте да или  нет): ")
        if confirmation == "да":
            del self.items[key]
            return self.items.items()
        elif confirmation == "нет":
            print("Удаление не произведено")
        else:
            confirmation = input("Ответ не распознан (ответьте да или  нет): ")

    def get_total(self):
        return sum(self.items.values())