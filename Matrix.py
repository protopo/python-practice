# Задача: Класс "Матрица"
# Создайте класс Matrix, который будет представлять собой двумерную матрицу, доступную для индексации и изменения элементов с помощью операторов [].
#
# Требования к классу:
#
# Реализуйте магический метод __init__, который принимает список списков для создания матрицы.
# Перегрузите магический метод __getitem__, чтобы можно было обращаться к элементам матрицы с помощью индексации (например, matrix[i][j]).
# Перегрузите магический метод __setitem__, чтобы можно было изменять элементы матрицы с помощью индексации (например, matrix[i][j] = value).
# Реализуйте магический метод __str__, чтобы красиво выводить матрицу в виде строк, где каждый ряд — это отдельная строка, а элементы разделены пробелами.
# Добавьте метод для сложения двух матриц с помощью оператора + (метод __add__).
# Реализуйте метод транспонирования матрицы.
# Добавьте возможность умножения матриц (с помощью магического метода __mul__).
# Добавьте поддержку работы с не квадратными матрицами.

class Matrix:
    def __init__(self, data):
        self.data = data

    def __getitem__(self, index):
        return self.data[index]

    def __setitem__(self, index, value):
        self.data[index] = value

    def __str__(self):
        return '\n'.join(' '.join(map(str, row)) for row in self.data)

    def __add__(self, other):
        result = [
            [self.data[i][j] + other[i][j] for j in range(len(self.data[0]))]
            for i in range(len(self.data))
        ]
        return Matrix(result)

    def transpose(self):
        transposed = [[self.data[j][i] for j in range(len(self.data))]
                      for i in range(len(self.data[0]))]
        return Matrix(transposed)

    def __mul__(self, other):
        result = [[sum(x * y for x, y in zip(self_row, other_col))
                   for other_col in zip(*other.data)]
                  for self_row in self.data]
        return Matrix(result)

matrix1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix2 = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

print(matrix1)
# Вывод:
# 1 2 3
# 4 5 6
# 7 8 9

print(matrix1[1][2])  # 6 (элемент во второй строке, третий столбец)

matrix1[0][0] = 10
print(matrix1)
# Вывод:
# 10 2 3
# 4 5 6
# 7 8 9

matrix_sum = matrix1 + matrix2
print(matrix_sum)
# Вывод:
# 19 10 10
# 10 10 10
# 10 10 10