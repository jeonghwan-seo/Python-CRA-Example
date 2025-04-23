class Item:
    def __init__(self, name, weight, price):
        self.name = name
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price

a_book = Item('book', 10, 9.5)
print(a_book.subtotal())
a_book.weight = -10
print(a_book.subtotal())




