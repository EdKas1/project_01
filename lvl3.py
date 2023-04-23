# Задача 3.1.
# Создайте класс матрицы (или таблицы).
# Требования к классу:
#   - каждая колонка является числом от 1 до n (n любое число, которые вы поставите!)
#   - в каждой ячейке содержится либо число, либо None
#   - доступны следующие методы матрицы:
#       * принимать новые значения, 
#       * заменять существующие значения, 
#       * выводить число строк и колонок.

# Пример матрицы 10 на 10 из единиц:
# [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

# Примечание! 
#   - новый класс не запрещено строить на базе существующих типов данных: списков, словарей и тд.
#   - отображать в таблице/матрице название колонки не обязательно!
#   - проявите фантазию :)

class Steal:

    def __init__(self):
      
        self.matrix = []
        self.rows = 0
        self.columns = 0
        self.name = 'noname'

    def __str__(self):
        return self.matrix

    def generate(self, rows, columns, verbose=False):
        '''
        Возвращает список списков, содержащих индексы матрицы (строка, столбец).
        int, int -> [[(int, int), ...], ...]
        '''
        self.rows = rows
        self.columns = columns
        self.matrix = [[(row, col) for col in range(columns)] for row in range(rows)]
        if verbose ==  True:
            print(f'В матрице {self.rows} строк и {self.columns} колонок')
            print('--------' * columns)
            self.printme()
            print('--------' * columns)
        return self.matrix

    def printme(self, verbose=False):
        '''
        Печать построчно
        '''
        if verbose == True:
            print(f'В матрице {self.rows} строк и {self.columns} колонок')
        for row in self.matrix:
            print(row)

    def get_row(self, n, verbose=False):
        '''
        Возвращает строки
        '''
        if verbose ==  True:
            print(f'matrix[row={n}]...')
            print(self.matrix[n])
        return self.matrix[n]

    def get_col(self, n, verbose=False):
        '''
        Возврат столбцов
        '''
        column_items = []
        i = 0
        while i < self.rows:
            column_items.append(self.matrix[i][n])
            i += 1
        if verbose ==  True:
            for item in column_items:
                print(item)
        return column_items

    def get_cell(self, row, col, verbose=False):
        '''
        Возврат ячейки
        '''
        if verbose ==  True:
            print(self.matrix[row][col])
        return self.matrix[row][col]

    def write_cell(self, row, col, data, verbose=False):
        '''
        Перезапись в ячейку
        '''
        self.matrix[row][col] = data
        if verbose ==  True:
            print('Записано в ячейке[row={row}, col={col}]...')
            print(self.matrix[row][col])                            
        return self.matrix[row][col]
