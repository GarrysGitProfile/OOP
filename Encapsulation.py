"""Encapsulation is the process of preventing clients from accessing certain properties, which can only be accessed through specific methods."""

class Book:
    def __init__(self, title, quantity, author, price):
        self.title = title
        self.quantity = quantity
        self.author = author
        self.price = price
        # private attribute called __discount in the Book class.
        self.__discount = 0.10
        
    def __repr__(self):
        return f"Book: {self.title}, Quantity: {self.quantity}, Author: {self.author}, Price: {self.price}"
        
if __name__ == '__main__':
    book1 = Book('book 1', 12, 'Author 1', 120)
    
    print(book1.title)
    print(book1.quantity)
    print(book1.author)
    print(book1.price)
    print(book1.__discount)
