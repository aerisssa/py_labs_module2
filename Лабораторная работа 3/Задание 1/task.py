class Book:
    """Базовый класс книги."""

    def __init__(self, name: str, author: str):
        self._name = name  # Используем _name для обозначения "защищенного" атрибута
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self._pages = pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, pages: int):
        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть целым числом.")
        if pages <= 0:
            raise ValueError("Количество страниц должно быть больше 0.")
        self._pages = pages

    def __str__(self):
        return (f"Бумажная книга {self.name}. Автор {self.author}. "
                f"Количество страниц: {self.pages}")


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self._duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, duration: float):
        if not isinstance(duration, (int, float)):
            raise TypeError("Продолжительность должна быть числом.")
        if duration <= 0:
            raise ValueError("Продолжительность должна быть больше 0.")
        self._duration = duration

    def __str__(self):
        return (f"Аудиокнига {self.name}. Автор {self.author}. "
                f"Продолжительность: {self.duration} часов")


# Пример использования
book1 = Book("Название книги", "Автор")
print(book1)  # Вывод: Книга Название книги. Автор Автор
print(repr(book1))  # Вывод: Book(name='Название книги', author='Автор')

paper_book = PaperBook("Название бумажной книги", "Автор", 200)
print(paper_book)  # Вывод: Бумажная книга Название бумажной книги. Автор Автор. Количество страниц: 200
print(repr(paper_book))  # Вывод: PaperBook(name='Название бумажной книги', author='Автор')

audio_book = AudioBook("Название аудиокниги", "Автор", 5.5)
print(audio_book)  # Вывод: Аудиокнига Название аудиокниги. Автор Автор. Продолжительность: 5.5 часов
print(repr(audio_book))  # Вывод: AudioBook(name='Название аудиокниги', author='Автор')
