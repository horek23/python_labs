from task import Order

def main():
    order_Denis = Order({"Монитор":250, "Пепси" : 1.85, "Будильник" : 52})

    print(order_Denis.get_data())
    print(f"Добавим еще один товар к заказу и покажем как изменился заказ: {order_Denis.add_item("Машина",7000)}")
    print(f"Удалим Будильник из заказа и покажем как изменился заказ: {order_Denis.remove_item("Будильник")}")
    print(f"Общее количество заказов: {Order.orders_quantity}")
    order_Liza = Order({"Шампунь": 20, "Шоколад": 5})
    print(f"Общее количество заказов: {Order.orders_quantity}")

if __name__ == "__main__":
    main()