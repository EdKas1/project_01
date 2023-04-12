# Задача 2.1. 

# Создайте две функции maximum и minimum,
# которые получают список целых чисел в качестве входных данных 
# и возвращают наибольшее и наименьшее число в этом списке соответственно.
# Например,
arr1 = [4,6,2,1,9,63,-134,566] #        -> max = 566, min = -134
arr2 = [-52, 56, 30, 29, -54, 0, -110] #-> min = -110, max = 56
arr3 = [42, 54, 65, 87, 0]    #         -> min = 0, max = 87
arr4 = [5]        #                     -> min = 5, max = 5
# функции max и min использовать нельзя!

def minimum(arr):
    list.sort(arr)
    return arr[0]

def maximum(arr):
    list.sort(arr)
    return arr[-1]
print ("max =", maximum(arr4), "min =", minimum(arr4))