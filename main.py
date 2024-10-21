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