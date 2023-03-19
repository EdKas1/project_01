# Задача 1.2.

import random      # Пункт A. 
import math        # Приведем плейлист песен в виде списка списков
import datetime    # Список my_favorite_songs содержит список названий и длительности каждого трека
                   # Выведите общее время звучания трех случайных песен в формате:
                   # Три песни звучат ХХХ минут
                   # Пункт D: Переведите минуты и секунды в формат времени. Используйте модуль datetime 

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]

res = random.sample(my_favorite_songs, 3)
res1 = int(res[0][1])
res2 = int(res[1][1])
res3 = int(res[2][1])
sum_res = res1 + res2 + res3
res10 = res[0][1]%1 * 100
res20 = res[1][1]%1 * 100
res30 = res[2][1]%1 * 100
sum_res2 = int(res10 + res20 + res30)
if sum_res2 > 59:
    sum_res += 1
    sum_res2 -= 60
    

print(res)
print("Секунды:", sum_res2)
print("А,С: Три песни звучат:", sum_res,  "минут")
print("Д:", datetime.time(00, sum_res, sum_res2).strftime('%M:%S'), "мин:сек")
print()
print("Словарик")
# Пункт B. 
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}

#print(type(my_favorite_songs_dict))
Songlis = list(my_favorite_songs_dict)
res01 = random.sample(Songlis, 3)
res11 = int(res[0][1])
res21 = int(res[1][1])
res31 = int(res[2][1])
sum_res01 = res1 + res2 + res3
res101 = res[0][1]%1 * 100
res201 = res[1][1]%1 * 100
res301 = res[2][1]%1 * 100
sum_res02 = int(res10 + res20 + res30)
if sum_res02 > 59:
    sum_res01 += 1
    sum_res02 -= 60
print(res01)
print("Секунды:", sum_res02)
print("А,С: Три песни звучат:", sum_res01,  "минут")
print("Д:", datetime.time(00, sum_res01, sum_res02).strftime('%M:%S'), "мин:сек")
# Дополнительно 
# Пункт D.
# Переведите минуты и секунды в формат времени. Используйте модуль datetime 