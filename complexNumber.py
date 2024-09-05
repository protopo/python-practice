# Задача: Создание класса "Комплексное число"
# Создайте класс ComplexNumber для работы с комплексными числами. Каждый объект этого класса должен иметь два атрибута: вещественная часть и мнимая часть.
# 
# Требования к классу:
# 
# Реализуйте магический метод __init__ для инициализации комплексного числа.
# Перегрузите магический метод __str__, чтобы выводить комплексное число в формате: "a + bi", где a — вещественная часть, b — мнимая часть.
# Реализуйте операцию сложения двух комплексных чисел с помощью метода __add__.
# Реализуйте операцию вычитания двух комплексных чисел с помощью метода __sub__.
# Реализуйте операцию умножения двух комплексных чисел с помощью метода __mul__.
# Реализуйте операцию деления двух комплексных чисел с помощью метода __truediv__.
# Добавьте метод сравнения комплексных чисел на равенство __eq__.

class ComplexNumber:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return ComplexNumber(self.a + other.a, self.b + other.b)

    def __sub__(self, other):
        return ComplexNumber(self.a - other.a, self.b - other.b)

    def __mul__(self, other):
       return ComplexNumber(self.a * other.a - self.b * other.b, self.a * other.b + self.b * other.a)

    def __truediv__(self, other):
            return ComplexNumber((self.a * other.a + self.b * other.b) / (other.a ** 2 + other.b ** 2),
                                 (- self.a * other.b + self.b * other.a) / (other.a ** 2 + other.b ** 2))

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b

    def __str__(self):
        if (self.a % 1 > 0) or (self.b % 1 > 0):
            if self.b == 0:
                return '%.16f' % self.a
            if self.a == 0:
                return '%.16fi' % self.b
            if self.b < 0:
                return '%.16f - %.16fi' % (float(self.a), float(-self.b))
            else:
                return '%.16f + %.16fi' % (self.a, self.b)
        if self.b == 0:
            return '%.f' % self.a
        if self.a == 0:
            return '%.fi' % self.b
        if self.b < 0:
            return '%.f - %.fi' % (self.a, -self.b)
        else:
            return '%.f + %.fi' % (self.a, self.b)

num1 = ComplexNumber(2, 3)  # 2 + 3i
num2 = ComplexNumber(1, 4)  # 1 + 4i

print(num1)  # 2 + 3i
print(num2)  # 1 + 4i

print(num1 + num2)  # 3 + 7i
print(num1 - num2)  # 1 - 1i
print(num1 * num2)  # -10 + 11i
print(num1 / num2)  # 0.8235294117647058 - 0.29411764705882354i
print(num1 == num2)  # False