# def palindrome(palidromus):
#     """Проверяет является ли слово палидромом"""
#     return palindromus[::-1] == palindromus
# while True:
#     palindromus = input("Enter a word: ")
#     print(f"{palindromus} is palindrome!" if palindrome(palindromus) else "not a palindrome")

from exceptions import ValidationError
from validator import Validator
from validator import DataWithDate
from random import randint
from datetime import datetime



__author__ = "ilia kavaleu"
__andrzej__ = "andrzej 'Super Experience' sherlat"
__nick__ = "nikitos 'Super Experience Number Two' kerz"
def get_passport_advice(pas:int) -> str:
    """Функция валидации пасспортных данных,
    Параметр pas: принимает целочисленный аргумент,
    Метод return: возращает ошибку строки,
    Функция get_passport_advice принимает ответ и проводит проверку на сходство с условием.
    """
    if pas <= 17:
        return " You need to get a passport at the age of 16.\n"
    elif pas <= 26:
        return " You need to exchange yr passport at the age of 25.\n"
    elif pas <= 46:
        return " You need to exchange yr passport at the age of 45 second time.\n"


def clear_whitespaces(clear_all: str) -> str:
    """
    Функция clear_whitespaces очищает от пробелов вначале и в конце введеные пользователем данные
    Параметр сlear_all: возращает строку
    Метод return: возращает нашу функцию clear_whitespaces
    """
    return clear_all.strip()


#random number
def guess_number_game() -> None:
    """
    Фунцкия guess_number_game - игра, угадай число от 1 до 5, генерируте случайное число и просит юзера его угадать,
    процесс продолжается пока пользователь его не угадает, в конце выводит количество попыток
    В переменной count = 0 начинаем отсчет с 0 о количестве попыток,
    Метод randint - возращает случайное целочисленное число в пределах между двумя аргументами(1 и 5 в нашем случае)

    Запускаем цикл While: приветствие, применение функции очищения на случай неправильности ввода нашего числа(например буквы),
    следующая попытка и досчет +1,

    Операция continue позволяет пропустить часть цикла в случае возникновения какаго-нибудь фактора и приступить к следующей
    итерации цикла, то есть если что-то пошло не так возращаемся в начало цикла.
    Далее обычная проверка если наше число == загаданному числу программой, мы победили, break - игра окончена, если
    наше число > 5, то в связи с условиями от 1 до 5, выводит соответсвующее сообщение, если наше число != 5, то возвращаемся в
    начало цикла, также идет счет +1 на каждую попытку.
    """
    count = 0

    game_number =  randint(1, 5)

    while True:
        guess = input("Hello! Guess the number from 1 to 5: ")
        try:
            guess = int(clear_whitespaces(guess))
        except ValueError:
            print("You have entered symbols, you need to enter numbers")
            count += 1
            continue

        if guess == game_number:
            print("You guesses!")
            break
        if guess > 5:
            print("Your number should less or equals 5!")
        elif guess != game_number:
            print(f"No guessed")
        count += 1

def main() -> None:
    """
     Главная функция main в которой пользователь вводит данные имя и возраст.
     С помощью этих данных будет создаваться класс DataWithData.
     Также при вводе пользователем данных будет отображаться сообщение об ошибке, если что-то введено не верно в соответсвии
     с условиями, затем при непрваильности ввода пользователь внова пробует ввести данные и показывает номер попытки ввода.

     error_count = 1 - переменная позволяющая начать начало отсчета(попытки ввода)
     В переменную val_obj присваиваем класс Validator с нашими функциями (_validate_name, _validate_age, validate)

     Запускаем цикл While:
     Первым делом показываем попытку ввода, если она больше одного, то выводит сообщение о номере твоей попытки ввода.
     Далее пользователь вводит данные имя и возраст.

     Исключение:
     В переменной data присваиваем класс DataWithDate в который помещаем введенные пользователем данные, если что-то
     пошло не так выдаем сообщение о неверности введенных данных и добавляем попытку ввода + continue для возврата в начало
     цикла.
     В следующем исключении если все прошло гладко мы получаем наши данные, если нет +1 попытка ввода и по новой.

     Далее в переменной text мы помещаем введеные пользователем данные, в переменную pas помещаем функцию get_passport_advice(валидация возраста
     для паспортных данных) с yr_age(ввод возраста). Далее в text присваиваем pas и выводим.

     Запускаем в конце игру guess_number_game().
     Специальная переменная __name__ будет равна "__main__", так как файл запускается как основаня программа. Если запускали
     код в качестве модуля то main содерживое внутри main исполнено не будет. Возращаем main()
     """

    error_count = 1
    val_obj = Validator()
    time_first = datetime.utcnow()     # Время запуска программы

    while True:

        if error_count > 1:
            print(f"Your trying: {error_count}")

        yr_name = input("Enter your name: ")
        yr_age = input("Enter your age: ")


        try:
            obj_data = DataWithDate(yr_name, yr_age)
        except ValueError as e:
            error_count += 1
            print(f"Data entered wrong: {e}\n")
            continue


        try:
            val_obj.validate(obj_data)
        except ValidationError as e:
            error_count += 1
            print(f"Data entered wrong. Check out the text error: {e}\n")
            continue
        break

    pas = get_passport_advice(obj_data.age)
    text = f"Hello {yr_name .title()}! You age is {yr_age}."

    if pas:
        text += pas

    print(f"{time_first.strftime('%H:%M:%S')} | first time. ")
    print(f"{obj_data.time_last.strftime('%H:%M:%S')} | last time. ")
    print(f"{obj_data.time_last - time_first} | difference in time\n")
    print(text)

    guess_number_game()


if __name__ == '__main__':
    main()
    print(f"First of all i want to thank The program made by {__andrzej__.title()} and {__nick__.title()}.\n "
        f"Without you it wouldn's have happened!"
        f"And This is program made by {__author__.title()}!")
