# TODO: Подробно описать три произвольных класса
import doctest
from typing import List, Tuple


# TODO: описать класс
class Refrigerator:
    def __init__(self, temperature: float, capacity: int):
        """
        Создание и подготовка к работе объекта "Холодильник"

        :param temperature: Температура внутри холодильника.
        :param capacity: Ёмкость холодильника.

        :raise ValueError: Если заданная температура не попадает
         в необходимый диапазон, то возвращается ошибка.
        :raise ValueError: Если ёмкость холодильника задана
         отрицательной, то возвращается ошибка.

        Примеры:
        >>> fridge = Refrigerator(temperature=4, capacity=200)    # инициализация холодильника
        """
        if not (-30 <= temperature <= 10):
            raise ValueError("Температура холодильника должна быть в диапазоне от -30 до 10 градусов.")
        if capacity <= 0:
            raise ValueError("Ёмкость должна быть положительным числом.")

        self.temperature: float = temperature
        self.capacity: int = capacity
        self.contents: List[Tuple[str, int]] = []

    def add_item(self, item: str, quantity: int) -> str:
        """
        Функция которая добавляет продукты в холодильник.

        :param item: Продукт, добавляемый в холодильник
        :param quantity: Количество продукта.

        :return: Сколько единиц продукта добавлено в холодильник.
        :raise ValueError: Если количество продуктов задано отрицательным, то возвращается ошибка.
        """
        if quantity <= 0:
            raise ValueError("Количество должно быть положительным.")
        self.contents.append((item, quantity))
        return f"Добавлено {quantity} единиц {item}."

    def adjust_temperature(self, new_temp: float) -> str:
        """
        Функция, которая изменяет температуру холодильника.
        :param new_temp: Новая заданная температура.

        :return: Какая температура установлена внутри холодильника.
        :raise ValueError: Если заданная температура не попадает в необходимый диапазон,
         то возвращается ошибка.
        """
        if not (-30 <= new_temp <= 10):
            raise ValueError("Новая температура должна быть в диапазоне от -30 до 10 градусов.")
        self.temperature = new_temp
        return f"Температура изменена на {new_temp}°C."


# TODO: описать ещё класс
class Phone:
    def __init__(self, brand: str, battery_capacity: int):
        """
        Создание и подготовка к работе объекта "Телефон"

        :param brand: Модель телефона.
        :param battery_capacity: Емкость батареи.

        :raise ValueError: Если заданная ёмкость батареи не попадает в необходимый диапазон,
         то возвращается ошибка.

        Примеры:
        >>> phone = Phone(brand="Samsung", battery_capacity=4000) # инициализация телефона
        """
        if battery_capacity <= 0 or battery_capacity > 5000:
            raise ValueError("Ёмкость батареи должна быть от 1 до 5000 мАч.")

        self.brand: str = brand
        self.battery_capacity: int = battery_capacity
        self.battery_level: int = 100

    def make_call(self, duration: int) -> str:
        """
        Функция которая совершает звонок, уменьшая емкость батареи.
        :param duration: Длительность звонка.

        :return: Длительность звонка и остаток заряда батареи
        :raise ValueError: Если длительность звонка задана отрицательной, то возвращается ошибка.
        :raise ValueError: Если количество заряда недостаточно для звонка, то возвращается ошибка.
        """
        if duration <= 0:
            raise ValueError("Длительность звонка должна быть положительным числом.")
        battery_usage = duration * 2
        if battery_usage > self.battery_level:
            raise ValueError("Недостаточно заряда для звонка.")
        self.battery_level -= battery_usage
        return f"Звонок длительностью {duration} минут завершён. Остаток заряда: {self.battery_level}%."

    def charge(self, amount: int = 20) -> str:
        """
        Функция, которая заряжает телефон.
        :param amount: Количество добавляемого заряда.

        :return: Текущий уровень заряда батареи
        :raise ValueError: Если количество заряда задано отрицательным, то возвращается ошибка.
        """
        if amount <= 0:
            raise ValueError("Количество заряда должно быть положительным.")
        self.battery_level = min(100, self.battery_level + amount)
        return f"Телефон заряжен. Текущий уровень заряда: {self.battery_level}%."


# TODO: и ещё один
class ElectricKettle:
    def __init__(self, volume: float, is_on: bool = False):
        """
        Создание и подготовка к работе объекта "Электрический чайник"

        :param volume: Объём чайника.
        :param is_on: Включен ли чайник в данный момент.

        :raise ValueError: Если заданный объём чайника не попадает в необходимый диапазон,
         то возвращается ошибка.

        Примеры:
        >>> kettle = ElectricKettle(volume=1.5) # инициализация чайника
        """
        if volume <= 0 or volume > 5:
            raise ValueError("Объём чайника должен быть от 0 до 5 литров.")

        self.volume: float = volume  # В литрах
        self.is_on: bool = is_on
        self.water_level: float = 0  # Уровень воды в литрах

    def fill(self, amount: float) -> str:
        """
        Функция, которая заполняет чайник водой.
        :param amount: Количество добавляемой воды.

        :return: Текущий уровень воды в чайнике
        :raise ValueError: Если количество воды в чайнике задано отрицательным,
         то возвращается ошибка.
        :raise ValueError: Если объём имеющейся воды в чайнике и долитой больше объёма чайника,
         то возвращается ошибка.
        """
        if amount <= 0:
            raise ValueError("Количество воды должно быть положительным.")
        if self.water_level + amount > self.volume:
            raise ValueError("Невозможно залить больше, чем позволяет объём чайника.")
        self.water_level += amount
        return f"Чайник заполнен. Текущий уровень воды: {self.water_level} литров."

    def boil(self) -> str:
        """
        Функция, которая кипятит воду в чайнике.

        :return: Кипячение воды
        :raise ValueError: Если уровень воды в чайнике меньше или равен нулю,
         то возвращается ошибка.
        """
        if self.water_level <= 0:
            raise ValueError("Нельзя кипятить пустой чайник.")
        self.is_on = True
        return "Чайник кипятит воду."


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
