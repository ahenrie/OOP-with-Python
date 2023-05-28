class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.subtotal = 0

    def calculate_subtotal(self):
        self.subtotal = self.price * self.quantity

    def get_subtotal(self):
        return self.subtotal

    def __repr__(self):
        return f"Item({self.name}, {self.price}, {self.quantity}, {self.subtotal})"


class ShoppingCart:
    def __init__(self):
        self.items = []
        self.total = 0

    def add_item(self, item):
        self.items.append(item)
        item.calculate_subtotal()  # Update item subtotal
        self.calculate_total()

    def calculate_total(self):
        self.total = sum(item.get_subtotal() for item in self.items)

    def get_total(self):
        return self.total

    def get_num_items(self):
        return len(self.items)

    def get_items(self):
        return self.items

    def __str__(self):
        return f"The cart has {self.get_num_items()} items for a total of ${self.get_total():.2f}"


item1 = Item('milk', 1.5, 1)
item2 = Item('apple', 5, 0.75)
item3 = Item('bread', 2, 2.25)
cart = ShoppingCart()

cart.add_item(item1)
cart.add_item(item2)
cart.add_item(item3)

print(cart.get_total())
print(cart.get_num_items())
print(cart)
print(cart.get_items())
