
class Book:
    def __init__(self, title, author, isbn, copies):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.copies = copies

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"ISBN: {self.isbn}")
        print(f"Copies: {self.copies}")


class Member:
    def __init__(self, name, member_id, premium=False):
        self.name = name
        self.member_id = member_id
        self.premium = premium

    def borrow_book(self, book, number_of_copies):
        max_limit = 10 if self.premium else 5

        if number_of_copies > max_limit:
            print(f"{self.name} cannot borrow more than {max_limit} books at once.")
            return

        if book.copies >= number_of_copies:
            book.copies -= number_of_copies
            print(f"{self.name} borrowed {number_of_copies} copy/copies of '{book.title}'.")
        else:
            print(f"Not enough copies of '{book.title}' available.")

    def return_book(self, book, number_of_copies):
        book.copies += number_of_copies
        print(f"{self.name} returned {number_of_copies} copy/copies of '{book.title}'")


p1 = Book("RandomBook", "RandomPerson", "999-999-999", 7)


m1 = Member("Matthew", 14, premium=False)
m1.borrow_book(p1, 4)
p1.display_info()


m2 = Member("Alice", 15, premium=True)
m2.borrow_book(p1, 3)
p1.display_info()
