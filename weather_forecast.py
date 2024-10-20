# Вы работаете в команде веб-платформы с прогнозом погоды. Вы работаете над модулем, который будет выдавать статистическую информацию о температуре 
# за определенный период. На вход подается список из целых чисел. Ваша задача — определить, сколько чисел в этом списке являются положительными, 
# сколько отрицательными и сколько из них равны нулю. Вам нужно вывести не сами числа, а их количество в каждой категории.
# Формат ввода
# Входные данные состоят из одной строки, в которой чередуются целые числа, разделенные пробелами. Длина списка не превышает 100 элементов.
# Формат вывода
# Одна строка в формате: «выше нуля: A, ниже нуля: B, равна нулю: C», где A, B и C — количество положительных, отрицательных и нулевых чисел в списке # соответственно. Будьте внимательны с пробелами и знаками препинания.

def process(input_string: str) -> str:
    positive_count = 0
    negative_count = 0
    zero_count = 0

    numbers = map(int, input_string.split())

    for number in numbers:
        if number > 0:
            positive_count += 1
        elif number < 0:
            negative_count += 1
        else:
            zero_count += 1

    return f'выше нуля: {positive_count}, ниже нуля: {negative_count}, равна нулю: {zero_count}'

input_string = input()
output_string = process(input_string)
print(output_string)