from datetime import datetime
from exceptions import ValidationError

class Data:
    """
    параметр name - принимает строку
    параметр age - принимает строку
    __init__ - конструктор класса который инициализируют переменные и обрабатывают, и очищающая от пробелов
    в начале и в конце при вводе данных функция _clear_whitespaces
    """

    def __init__(self, name: str, age: str):
        self.name = name
        self.age = age
        self._clear_whitespaces()
        self.age = int(self.age)

    def _clear_whitespaces(self):
        """очищающая от пробелов
        в начале и в конце при вводе данных функция _clear_whitespaces
        """
        self.name = self.name.strip()
        self.age = self.age.strip()


class DataWithDate(Data):
    """
    Наследуемся от класса Data, принимая две переменные name и age. Это конструктор который инициализирует
    переменные класса родителя Date и записывает значения.

    super() - это функция, которая обращается к классу, от которого наследуется текущий.
    _init__() - это метод инициализации класса, следовательно super().__init__()
    вызывает метод инициализации из родительского класса. Например, чтобы. ДОПОЛНИТЬ его.

    Принимаем строку __init__(self, name, age) из Data, принимаем число(целое) __init__(self, name, age) из Data.
    Это конструктор класса который инициализирует переменные класса Data и записывает значения объекта класса.
    datetime.utcnow() - метод импортирвоания времени datetime.utcnow().
    """
    def __init__(self, name: str, age: str):
        super().__init__(name, age)
        self.time_last = datetime.utcnow()    #дополняем родительский класс Data дататаймем



class Validator:
    """
    Класс Validator.
    Проще говоря создаем пустой список data_history куда будут помещаться введеные пользователем данные.
    """
    def __init__(self):
        """__init__ - это конструктор класса который инициализирует список для хранения объекта DataWithData: name, age, time_close"""
        self.data_history: list[Data] = []

    def validate(self, data: Data) -> tuple:
        """
        Функция validate принимает класс DataWithData и записывает его в список data_history(с нашими данными),
        далее запускаем функции _validate_name и _validate_age из класса Validator, которые берут последний элемент из
        списка обрабатывая его. Возращаем функции name, age.
        """
        self.data_history.append(data)
        self._validate_name()
        self._validate_age()


    def _validate_name(self) -> None:
        """Функция валидации _validate_name возраста на правильность ввода пользователем и возвращает функцию name."""
        name = self.data_history
        if not self.data_history:
            raise ValueError("No object passed!")

        name = name[-1].name
        if not self.data_history[-1].name:
            raise ValidationError("You can enter something!")
        elif self.data_history[-1].name.count(" ") > 1:
            raise ValidationError("Many spaces.")
        elif len(self.data_history[-1].name) < 3:
            raise ValidationError("Yr name very short. Min 3 symbols!")


    def _validate_age(self) -> None:
        """Функция валидации _validate_age возраста на правильность ввода пользователем и возвращает функцию age."""
        if not self.data_history:
            raise ValueError(f"No object passed!")
        if self.data_history[-1].age < 1:
            raise ValidationError(f"You can't be 0 or less than 0!")
        elif self.data_history[-1].age < 14:
            raise ValidationError(f"Minimum age 14!")



