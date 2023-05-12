class Book:
    def __init__(self, title, quantity, author, price):
        self.title = title
        self.quantity = quantity
        self.author = author
        self.price = price

    # def __str__(self):
    #     return f"Book: {self.title}, Quantity: {self.quantity}, Author: {self.author}, Price: {self.price}"
    def __repr__(self):
        return f"Book: {self.title}, Quantity: {self.quantity}, Author: {self.author}, Price: {self.price}"

book1 = Book('River and the source', 2, 'Margaret Ogola', 750)
book2 = Book('Betrayal in the City', 1, 'Francis D. Imbuga', 650)
book3 = Book('The 4 - Hour Workweek', 1, 'Timothy Ferriss', 500)
print(book1)
print(book2)
print(book3)
