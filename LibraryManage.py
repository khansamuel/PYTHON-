class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Publication Year: {self.publication_year}")

class FictionBook(Book):
    def __init__(self, title, author, publication_year, genre):
        super().__init__(title, author, publication_year)
        self.genre = genre

    def display_info(self):
        super().display_info()
        print(f"Genre: {self.genre}")

class NonFictionBook(Book):
    def __init__(self, title, author, publication_year, topic):
        super().__init__(title, author, publication_year)
        self.topic = topic

    def display_info(self):
        super().display_info()
        print(f"Topic: {self.topic}")

# Create objects
fiction_book = FictionBook("The River and the Source", "J.R.R. Tolkien", 2003, "Setbook")
non_fiction_book = NonFictionBook("A Short History of the African Tradition", "Bill Bryson", 2003, "Science")

# Display information
fiction_book.display_info()
print("\n")
non_fiction_book.display_info()
