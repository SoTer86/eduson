class Inventory:
    def __init__(self):
        self.items = {}
    
    def add_item(self, id, name, quantity, price):
        if id in self.items:
            print(f"Товар с {id} уже существует.")
            return
        self.items[id] = {
            'name': name, 
            'quantity': quantity,
            'price': price
        }
        print(f"Товар {name} добавлен на склад.")
    
    def remove_item(self, id):
        if id in self.items:
            del self.items[id]
            print(f"Товар с id {id} удален со склада.")
        else:
            print(f"Товар с id {id} не найден.")
    
    def print_inventory(self):
        for id, info in self.items.items():
            print(f"id: {id}, Название: {info['name']}, Количество: {info['quantity']}, Цена: {info['price']}")


inventory = Inventory()
inventory.add_item('123', 'Мышка', 10, 500)
inventory.add_item('124', 'Клавиатура', 5, 1500)
inventory.print_inventory()
inventory.remove_item("124")
inventory.print_inventory