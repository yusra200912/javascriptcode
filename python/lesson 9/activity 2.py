class Library:
    def __init__(self, list_of_books, name):
        self.bookList = list_of_books
        self.name = name
        self.lendDict = {}

    def displayBooks(self):
        print(f"\nWe have the following books in our library: {self.name}")
        for book in self.bookList:
            print(" -", book)

    def lendBook(self, user, book):
        if book not in self.lendDict:
            self.lendDict[book] = user
            print("Lender-book database has been updated, you can take the book now.")
        else:
            print(f"Sorry, the book is already being used by {self.lendDict[book]}.")

    def addBook(self, book):
        self.bookList.append(book)
        print("Book has been added to the book list.")

    def returnBook(self, book):
        if book in self.lendDict:
            self.lendDict.pop(book)
            print("Thanks for returning the book.")
        else:
            print("This book was not lent out.")


if __name__ == '__main__':
    myLibrary = Library(
        ['Python', 'Rich Dad Poor Dad', 'Atomic Habits', 'I Am Not Jessica Chen',
         'The Silent Patient', 'If You Could See the Sun', "Let's Upskill"],
        "Z Library"
    )

    while True:
        print("\n===== Welcome to the Library =====")
        print("1. Display books")
        print("2. Lend a book")
        print("3. Add a book")
        print("4. Return a book")
        user_choice = input("Enter your choice (1-4): ")

        if user_choice not in ['1', '2', '3', '4']:
            print("Please enter a valid option.")
            continue
        else:
            user_choice = int(user_choice)

        if user_choice == 1:
            myLibrary.displayBooks()

        elif user_choice == 2:
            book = input("Enter the name of the book you want to lend: ")
            user = input("Enter your name: ")
            myLibrary.lendBook(user, book)

        elif user_choice == 3:
            book = input("Enter the name of the book you want to add: ")
            myLibrary.addBook(book)

        elif user_choice == 4:
            book = input("Enter the name of the book you want to return: ")
            myLibrary.returnBook(book)

        print("\nPress 'q' to quit or 'c' to continue")
        user_choice2 = ""
        while user_choice2.lower() not in ["c", "q"]:
            user_choice2 = input("Enter your choice: ")
            if user_choice2 == "q":
                exit()
            elif user_choice2 == "c":
                pass
