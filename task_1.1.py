# Задача 1.1.

# Есть строка с перечислением песен

my_favorite_songs = 'Waste a Moment, Staying\' Alive, A Sorta Fairytale, Start Me Up, New Salvation'
# print(len(my_favorite_songs))
print(my_favorite_songs[0:14])
print(my_favorite_songs[64:77])
print(my_favorite_songs[16:30])
print(my_favorite_songs[51:62])
# 
print(my_favorite_songs[0:14] + ", " + my_favorite_songs[-13:] + ", " + my_favorite_songs[16:30] + ", " + my_favorite_songs[51:62])
# Выведите на консоль с помощью индексации строки, последовательно: первый трек, последний, второй, второй с конца
# Нельзя переопределять my_favorite_songs и запятая не должна выводиться.

# нуу, это работает, но зачем же считать в ручную когда у меня есть python))

# Первый вариант это заставить его искать индексы самостоятельно с помощью find()
# Решение с помощью индекции строк

first_song = my_favorite_songs [
    : my_favorite_songs.find(',')
]

last_song = my_favorite_songs [
    my_favorite_songs.rfind('N') :
]

second_song = my_favorite_songs[
     my_favorite_songs.find('S') : 
     my_favorite_songs.find(', A')
]

previous_song = my_favorite_songs [
    my_favorite_songs.rfind('St') : 
    my_favorite_songs.rfind(', N')
    ]

print(first_song, last_song, second_song, previous_song)


# Второй вариант, мы можем воспользоваться методом разделения строк по символам. split.
# Полученный в результате список проиндексируем по песням

# Решение с помощью метода split() и индексации списков
songs = my_favorite_songs.split(', ')

print(songs[0], songs[-1], songs[1], songs[-2])
