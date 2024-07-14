class Book():
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False    

    def check_out(self):
        if self._is_checked_out:
            raise ValueError("Book is already checked")
        self._is_checked_out = True
        
    def return_book(self):
        if not self._is_checked_out:
            raise ValueError("Booked is not checked")
        self._is_checked_out = False
    
    def is_available(self):
        return not self._is_checked_out
        
        

class Library():
    def __init__(self):
        self._books = []

    def add_book(self, book):
        if isinstance(book, Book):
            self._books.append(book)
        else:
            raise ValueError("Only instances of Books can be added")
    
    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                book.check_out()
                return book
            else:
                raise ValueError(f"Book '{title}' is already checked out")
        raise ValueError(f"No available book found with title: {title}")

    def list_available_books(self):
        return [book for book in self._books if book.is_available]

    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                if not book.is_available():
                    book.return_book()
                    return book
                else:
                    raise ValueError(f"Book '{title}' is not checked out")
        raise ValueError(f"No checked-out book found with title: {title}")
            


        