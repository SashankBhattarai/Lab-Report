class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}, Price: {self.price}")

    def update_price(self, new_price):
        self.price = new_price
        print(f"Price updated to {self.price}")


b1 = Book("Re:Zero", "Tappei Nagatsuki", 1699)
b1.display_info()
b1.update_price(1299)
b1.display_info()
