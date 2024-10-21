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