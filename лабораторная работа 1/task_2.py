# TODO: импортируйте классы, созданные в ходе выполнения прошлого задания
from task_1 import Refrigerator, Phone, ElectricKettle


if __name__ == "__main__":
    fridge = Refrigerator(temperature=4, capacity=200)
    phone = Phone(brand="Samsung", battery_capacity=4000)
    kettle = ElectricKettle(volume=1.5)
    # TODO: инстанцировать все описанные классы, создав три объекта.

    try:
        print(fridge.adjust_temperature(-40))
        # TODO: вызвать метод с некорректными аргументами(b)
    except ValueError:
        print('Ошибка: неправильные данные')

    try:
        print(phone.make_call(-5))
        # TODO: вызвать метод с некорректными аргументами(a)
    except ValueError:
        print('Ошибка: неправильные данные')

    try:
        print(kettle.fill(3))
        # TODO: вызвать метод с некорректными аргументами(a)
    except ValueError:
        print('Ошибка: неправильные данные')


