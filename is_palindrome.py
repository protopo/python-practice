# Вы разрабатываете программу для проверки строк на палиндромы. Палиндромом называется строка, которая читается одинаково как с начала, так и с 
# конца. При этом пробелы и регистр букв игнорируются.
# Напишите программу, которая определяет, является ли заданная строка палиндромом.
# Формат ввода
# Одна строка, содержащая только строчные буквы русского алфавита и, в некоторых случаях, пробелы. Длина строки от 2 до 100 символов включительно.
# Формат вывода
# Одна из двух фраз (без кавычек): «Палиндром»‎ или «Не палиндром»‎.

def is_palindrome(input_string: str) -> bool:
    cleaned_string = ''.join(input_string.split()).lower()
    return cleaned_string == cleaned_string[::-1]

input_string = input()
if is_palindrome(input_string):
    print('Палиндром')
else:
    print('Не палиндром')