from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'Lib'

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
        return self.books if self.books else []

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


library = Library()

@app.route('/')
def index():
    books = library.list_books()
    if books is None:  # Проверка на случай, если возвращается None
        books = []
    return render_template('index.html', books=books)

@app.route('/add', methods=['POST'])
def add_book():
    title = request.form.get('title')
    author = request.form.get('author')
    try:
        year = int(request.form.get('year'))
    except ValueError:
        flash('Год должен быть числом')
        return redirect(url_for('index'))

    book = Book(title, author, year)
    library.add_book(book)
    flash(f"Книга {title} добавлена в библиотеку")
    return redirect(url_for('index'))

@app.route('/remove/<title>')
def remove_book(title):
    if library.remove_book(title):
        flash(f"Книга {title} была удалена из библиотеки")
    else:
        flash(f"Книга с названием {title} не найдена")
    return redirect(url_for('index'))

@app.route('/mark_read/<title>')
def mark_read(title):
    if library.mark_book_as_read(title):
        flash(f"Книга {title} была отмечена как прочитанная")
    else:
        flash(f"Книга с названием {title} не найдена")
    return redirect(url_for('index'))

@app.route('/mark_unread/<title>')
def mark_unread(title):
    if library.mark_book_as_unread(title):
        flash(f"Книга {title} была отмечена как непрочитанная")
    else:
        flash(f"Книга с названием {title} не найдена")
    return redirect(url_for('index'))

@app.route('/sort')
def sort_books():
    library.sort_books_by_year()
    flash("Книги отсортированны по году публикации")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)