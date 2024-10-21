class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.read = False  # По умолчанию книга непрочитанная

    def mark_as_read(self):
        self.read = True

    def mark_as_unread(self):
        self.read = False

    def __str__(self):
        status = "Прочитана" if self.read else "Не прочитана"
        return f"{self.title} by {self.author} ({self.year}) - {status}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"Книга '{book.title}' добавлена в библиотеку.")

    def list_books(self):
        if not self.books:
            print("Библиотека пуста.")
        else:
            for book in self.books:
                print(book)

    def find_by_title(self, title):
        found_books = [book for book in self.books if book.title.lower() == title.lower()]
        if found_books:
            for book in found_books:
                print(book)
        else:
            print(f"Книга с названием '{title}' не найдена.")

    def find_by_author(self, author):
        found_books = [book for book in self.books if book.author.lower() == author.lower()]
        if found_books:
            for book in found_books:
                print(book)
        else:
            print(f"Книги автора '{author}' не найдены.")

    def mark_book_as_read(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                book.mark_as_read()
                print(f"Книга '{book.title}' отмечена как прочитанная.")
                return
        print(f"Книга с названием '{title}' не найдена.")

    def mark_book_as_unread(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                book.mark_as_unread()
                print(f"Книга '{book.title}' отмечена как непрочитанная.")
                return
        print(f"Книга с названием '{title}' не найдена.")

    def remove_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                print(f"Книга '{book.title}' удалена из библиотеки.")
                return
        print(f"Книга с названием '{title}' не найдена.")

    def filter_books(self, read_status):
        filtered_books = [book for book in self.books if book.read == read_status]
        if filtered_books:
            for book in filtered_books:
                print(book)
        else:
            status = "прочитанные" if read_status else "непрочитанные"
            print(f"В библиотеке нет {status} книг.")

    def sort_books_by_year(self):
        self.books.sort(key=lambda book: book.year)
        print("Книги отсортированы по году публикации.")


def main():
    library = Library()

    while True:
        print("\nМеню библиотеки:")
        print("1. Добавить книгу")
        print("2. Просмотреть все книги")
        print("3. Найти книгу по названию")
        print("4. Найти книги по автору")
        print("5. Отметить книгу как прочитанную")
        print("6. Отметить книгу как непрочитанную")
        print("7. Удалить книгу")
        print("8. Показать прочитанные книги")
        print("9. Показать непрочитанные книги")
        print("10. Сортировать книги по году публикации")
        print("0. Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            year = int(input("Введите год публикации: "))
            book = Book(title, author, year)
            library.add_book(book)

        elif choice == "2":
            print("\nСписок книг:")
            library.list_books()

        elif choice == "3":
            title = input("Введите название книги: ")
            library.find_by_title(title)

        elif choice == "4":
            author = input("Введите автора книги: ")
            library.find_by_author(author)

        elif choice == "5":
            title = input("Введите название книги: ")
            library.mark_book_as_read(title)

        elif choice == "6":
            title = input("Введите название книги: ")
            library.mark_book_as_unread(title)

        elif choice == "7":
            title = input("Введите название книги для удаления: ")
            library.remove_book(title)

        elif choice == "8":
            print("\nПрочитанные книги:")
            library.filter_books(read_status=True)

        elif choice == "9":
            print("\nНепрочитанные книги:")
            library.filter_books(read_status=False)

        elif choice == "10":
            library.sort_books_by_year()
            print("\nСписок книг после сортировки:")
            library.list_books()

        elif choice == "0":
            print("Выход из программы.")
            break

        else:
            print("Неверный ввод, попробуйте снова.")

if __name__ == "__main__":
    main()