# Вы разрабатываете программу для анализа временного ряда цен акций. Вам нужно написать программу, которая позволит выявлять максимальные значения на # определенном временном промежутке, то есть выводить максимальные значения среди пройденных элементов на каждом шаге.
# Формат ввода
# Одна строка, в которой чередуются целые числа, разделенные пробелами. Длина списка — не больше 100 элементов.
# Формат вывода
# Одна строка, в которой чередуются целые числа, разделенные пробелами. В строке содержатся максимальные значения среди пройденных элементов на 
# каждом шаге.

def solve(input_string: str) -> str:
    numbers = list(map(int, input_string.split()))
    max_values = []
    current_max = float('-inf')

    for number in numbers:
        if number > current_max:
            current_max = number
        max_values.append(current_max)

    return ' '.join(map(str, max_values))

input_string = input()
result = solve(input_string)
print(result)