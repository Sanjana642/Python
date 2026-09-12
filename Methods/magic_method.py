# magic methods = Dunder method (double underscore) __init__, __str__, __eq__ 
# they are automatically called by many of Python's built-in operations.
# They allow developers to define or customize the behaviour of objects 

class Book:

    # built-in operations -
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f"'{self.title}' by '{self.author}'"

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

    def __lt__(self, other):
        return self.num_pages < other.num_pages

    def __add__(self, other):
        return f"{self.num_pages + other.num_pages} pages"

    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author

    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "num_pages":
            return self.num_pages
        else:
            return f"Key '{key}' was not found"

        
book1 = Book("The Habit", "J.R.R Tolkien", 310)
book2 = Book("Harry Potter and The Philosopher's Stone", "J.K Rowling", 233)
book3 = Book("The Lion, the Witch and the Wardrobe", "C.S lewis", 172)

# print(book1) - it will print memory address if __str__ is not there
print(book1)    # now it give output - 'The Habit' by 'J.R.R Tolkien'

# print(book1 == book2)  # False - we have not put __eq__ method
print(book1 == book2)  # output - True

# print(book1 > book2) - it will give error due to __lt__ is not declared 
# ERROR- '>' not supported between instances of 'Book' and 'Book'
print(book1 < book2)    # output - False
print(book3 < book2)    # output - True

# print(book1 + book2) - it wiill error due to __add__ is not declared
# ERROR- unsupported operand type(s) for +: 'Book' and 'Book'
print(book1 + book2)    # output- 543 pages

# print('Lion' in book3) -argument of type 'Book' is not a container or iterable
print("Lion" in book3)  #output - True
print("Rowling" in book2)   #output- True

# print(book2['title']) -'Book' object is not subscriptable
print(book2['title'])   #output -  Harry Potter and The Philosopher's Stone

# print(book1['author']) - none
print(book1['author']) #output - J.R.R Tolkien

# print(book1['num_pages']) -none
print(book1['num_pages']) # output - 310

print(book1['audio'])   # output - Key 'audio' was not found