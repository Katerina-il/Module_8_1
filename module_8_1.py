"""
Домашнее задание по теме "Try и Except"
Задание "Программистам всё можно":

Пора разрушать шаблоны привычного нам Python! Вот вас раздражает,
что мы не можем сложить число(int) и строку(str)? Давайте исправим это недоразумение!

"""



def add_everything_up(number1, number2):
    """будет складывать числа(int, float) и строки(str)"""
    # result = number1 + number2
    try:
        if isinstance(number1, (int, float)) and isinstance(number1, (int, float)):
            return number1 + number2
        else:
           raise TypeError
    except TypeError as exc:
        return f"{number1}{number2}"


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))