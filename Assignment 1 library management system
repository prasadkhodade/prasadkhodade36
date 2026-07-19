class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def display(self):
        print("Title :", self.title)
        print("Author :", self.author)
        if self.available:
            print("Status : Available")
        else:
            print("Status : Not Available")

class Patron:
    def __init__(self, name):
        self.name = name
        self.borrowed = []

    def display(self):
        print("Patron Name :", self.name)
        print("Borrowed Books :")
        if len(self.borrowed) == 0:
            print("None")
        else:
            for b in self.borrowed:
                print(b.title)

class Library:
    def __init__(self):
        self.books = []
        self.patrons = []

    def add_book(self, title, author):
        b = Book(title, author)
        self.books.append(b)
        print("Book Added")

    def register_patron(self, name):
        p = Patron(name)
        self.patrons.append(p)
        print("Patron Registered")

    def borrow_book(self, pname, btitle):
        foundPatron = None

        for p in self.patrons:
            if p.name == pname:
                foundPatron = p
                break

        if foundPatron == None:
            print("Patron not found")
            return

        for b in self.books:
            if b.title == btitle:
                if b.available:
                    b.available = False
                    foundPatron.borrowed.append(b)
                    print("Book Issued")
                else:
                    print("Book Not Available")
                return

        print("Book not found")

    def return_book(self, pname, btitle):
        for p in self.patrons:
            if p.name == pname:
                for b in p.borrowed:
                    if b.title == btitle:
                        b.available = True
                        p.borrowed.remove(b)
                        print("Book Returned")
                        return
                print("This book was not borrowed")
                return

        print("Patron not found")

    def show_books(self):
        if len(self.books) == 0:
            print("No Books")
        else:
            for b in self.books:
                b.display()
                print()

    def show_patrons(self):
        if len(self.patrons) == 0:
            print("No Patrons")
        else:
            for p in self.patrons:
                p.display()
                print()

lib = Library()

while True:
    print("\n------ Library Management ------")
    print("1. Add Book")
    print("2. Register Patron")
    print("3. Show Books")
    print("4. Show Patrons")
    print("5. Borrow Book")
    print("6. Return Book")
    print("7. Exit")

    ch = input("Enter Choice : ")

    if ch == "1":
        t = input("Enter Book Title : ")
        a = input("Enter Author : ")
        lib.add_book(t, a)

    elif ch == "2":
        n = input("Enter Patron Name : ")
        lib.register_patron(n)

    elif ch == "3":
        lib.show_books()

    elif ch == "4":
        lib.show_patrons()

    elif ch == "5":
        n = input("Enter Patron Name : ")
        t = input("Enter Book Title : ")
        lib.borrow_book(n, t)

    elif ch == "6":
        n = input("Enter Patron Name : ")
        t = input("Enter Book Title : ")
        lib.return_book(n, t)

    elif ch == "7":
        print("Program Ended")
        break

    else:
        print("Wrong Choice")
