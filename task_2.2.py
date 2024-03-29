# Задача 2.2. 

# Напишите функцию, которая возвращает номер квартал по номеру месяца
# Например: 
# месяц 2 (февраль) является частью первого квартала; 
# месяц 6 (июнь) является частью второго квартала; 
# месяц 11 (ноябрь) является частью четвертого квартала.

def quarter_of(month):
    if 1 <= month <= 3:
        return f"месяц № {month} является частью первого квартала"
    elif 4<= month <= 6:
        return f"месяц № {month} является частью второго квартала"
    elif 7<= month <= 9:
        return f"месяц № {month} является частью третьего квартала"
    elif 10<= month <= 12:
        return f"месяц № {month} является частью четвёртого квартала"
    else:
        return f"некорректно! Введите номер месяца от 1 до 12"

print(quarter_of(111))  
