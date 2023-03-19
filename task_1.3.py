# Задача 1.3.

import datetime

number = int(input('Введите номер месяца: '))
if number < 1 or number > 12:
    print('Такого месяца нет, повторите ввод')
elif number == 2:
    print("28 дней")
    month = datetime.date(2023,number,1).strftime('%B')
    print(f'Месяц: {month}')
elif number == 1 or number == 3 or number == 5 or number == 7 or number == 8 or number == 10 or number == 12:
    print("31 день")
    month = datetime.date(2023,number,1).strftime('%B')
    print(f'Месяц: {month}')
elif number == 4 or number == 6 or number == 9 or number == 11:
    print("30 дней")
    month = datetime.date(2023,number,1).strftime('%B')
    print(f'Месяц: {month}')
# Напишите скрипт, который принимает от пользователя номер месяца, 
# а возвращает количество дней в нем.
# Результат проверки вывести на консоль
# Допущение: в феврале 28 дней
# Если номер месяца некорректен - сообщить об этом

# Например,
    # Введите номер месяца: 3
    # Вы ввели март. 31 дней

    # Введите номер месяца: 2
    # Вы ввели февраль. 28 дней

    # Введите номер месяца: 15
    # Такого месяца нет!
