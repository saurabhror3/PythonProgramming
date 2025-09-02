# 1. Define the Book class
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self):
        return f"'{self.title}' by {self.author} (ISBN: {self.isbn})"


# 2. Define the Member class
class Member:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    # 3a. Method to borrow a book
    def borrow_book(self, book):
        self.borrowed_books.append(book)
        print(f"{self.name} has borrowed {book.title}.")

    # 3b. Method to return a book
    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            print(f"{self.name} has returned {book.title}.")
        else:
            print(f"{self.name} has not borrowed {book.title}.")

    # 4. String representation
    def __str__(self):
        borrowed_titles = ', '.join([book.title for book in self.borrowed_books]) or "No books borrowed"
        return f"Member: {self.name} (ID: {self.member_id}) | Borrowed Books: {borrowed_titles}"


# 5. Demonstrate usage
# Create books
book1 = Book("1984", "George Orwell", "9780451524935")
book2 = Book("To Kill a Mockingbird", "Harper Lee", "9780060935467")

# Create a member
member1 = Member("Alice Johnson", "M001")

# Borrow books
member1.borrow_book(book1)
member1.borrow_book(book2)

# Show member info
print(member1)

# Return a book
member1.return_book(book1)

# Show member info again
print(member1)
