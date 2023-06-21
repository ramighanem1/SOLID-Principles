class Books():
    def __init__(self):
        self.books = {}
        self.number = 0

    def add_book(self,book):
        self.number += 1
        self.books[self.number] = book

    def __str__(self):
        return str(self.books)
    

    
    
class StoreBooks():
    @staticmethod
    def save_books(filename,books):
        with open(filename,"w") as f:
            f.write(str(books))



b = Books()
b.add_book("Book A")
b.add_book("Book B")
print(f'Available Books : {b}')

store = StoreBooks()
store.save_books("Books.txt",b)