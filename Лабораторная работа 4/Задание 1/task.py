# TODO: описать базовый класс
class Animal:
    """
    Базовый класс для животных.
    """

    def __init__(self, name: str, age: int) -> None:
        """
        Конструктор класса Animal.
        :param name: Имя животного.
        :param age: Возраст животного.
        """
        self._name = name  # Инкапсуляция: имя доступно только внутри класса
        self._age = age    # Инкапсуляция: возраст доступен только внутри класса


    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта Animal.
        """
        return f"Имя животного - {self._name}, возраст животного - {self._age}"

    def __repr__(self) -> str:
        """
        Возвращает строковое представление объекта Animal для разработчиков.
        """
        return f"Animal(name='{self._name}', age={self._age})"

    def make_sound(self) -> str:
        """
        Возвращает звук, издаваемый животным.
        """
        return "Animal sound"


# TODO: описать дочерний класс
class Dog(Animal):
    """
    Дочерний класс для собак.
    """

    def __init__(self, name: str, age: int, breed: str) -> None:
        """
        Конструктор класса Dog.
        :param name: Имя собаки.
        :param age: Возраст собаки.
        :param breed: Порода собаки.
        """
        super().__init__(name, age)  # Вызов конструктора родительского класса
        self.breed = breed

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта Dog.
        """
        return f"Имя собаки - {self._name}, возраст - {self._age}, порода - {self.breed}"

    def __repr__(self) -> str:
        """
        Возвращает строковое представление объекта Dog для разработчиков.
        """
        return f"Dog(name='{self._name}', age={self._age}, breed='{self.breed}')"

    def make_sound(self) -> str:
        """
        Возвращает звук, издаваемый собакой. Перегрузка метода make_sound из базового класса.

        Перегрузка необходима, так как собаки издают звук, отличный от общего звука животных.
        """
        return "Woof!"

    def fetch(self, item: str) -> str:
        """
        Собака приносит предмет.
        :param item: Предмет, который нужно принести.
        Возвращает сообщение о том, что собака принесла предмет.
        """
        return f"Dog {self._name} fetched the {item}."


animal = Animal("Abrakadabra", 5)
print(animal)  # Вывод: Имя животного - Abrakadabra, возраст животного - 5
print(repr(animal)) # Вывод: Animal(name='Generic Animal', age=5)
print(animal.make_sound()) # Вывод: Animal sound

dog = Dog("Sharik", 3, "Golden Retriever")
print(dog)  # Вывод: Имя собаки - Sharik, возраст - 3, порода - Golden Retriever
print(repr(dog)) # Вывод: Dog(name='Buddy', age=3, breed='Golden Retriever')
print(dog.make_sound())  # Вывод: Woof!
print(dog.fetch("ball"))  # Вывод: Dog Sharik fetched the ball.