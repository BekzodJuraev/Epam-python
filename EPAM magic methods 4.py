class Book:

    def __init__(self, author, name, price):
        self._name = name
        self._author = author
        self.price = price  # This will trigger the price setter

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, x):
        if 0 <= x <= 100:
            self._price = x  # Set the value to the internal attribute
        else:
            raise ValueError("Price must be between 0 and 100.")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,s):
        raise ValueError("Name can not be changed.")

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, s):
        raise ValueError("Author can not be changed.")








b = Book("William Faulkner", "The Sound and the Fury", 12)
b.price=5
print(b.name)
print(b.author)




