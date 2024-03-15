class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author

class LibraryMember:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        """
        Add a Book object to the borrowed_books list.
        """
        self.borrowed_books.append(book)

    def return_book(self, book):
        """
        Remove a Book object from the borrowed_books list.
        """
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
        else:
            print("Error: Book not borrowed by this member.")

    def display_info(self):
        """
        Display member ID, name, and borrowed books.
        """
        print("Member ID:", self.member_id)
        print("Name:", self.name)
        print("Borrowed Books:")
        for book in self.borrowed_books:
            print("- Title:", book.title)
            print("  Author:", book.author)
            print()



book1 = Book(1, "Python Programming", "John Smith")
book2 = Book(2, "Data Science Essentials", "Emma Johnson")

member1 = LibraryMember(101, "Alice")
member1.borrow_book(book1)
member1.borrow_book(book2)

member1.display_info()
