# Вы разрабатываете программу, которая заменяет одни слова в тексте на другие. Программа учитывает регистр буквенных символов, то есть python и 
# Python — это разные слова.
# Формат ввода
# Три строки:
# Первая строка — текст произвольной длины до 1000 символов, в котором нужно найти заменяемое слово;
# Вторая строка — исходное слово, которое нужно заменить в исходном в тексте;
# Третья строка — слово, на которые нужно заменить исходный набор.
# Формат вывода
# Две строки:
# Текст с произведенной заменой. Если в тексте не найдено заявленного слова, выводится исходный текст.
# Количество произведенных замен в виде целого числа.

class TextProcessor:
    def __init__(self, text):
        self.text = text

    def replace_word(self, original_word, replacement_word):
        # Replace the word and count the number of replacements
        new_text = self.text.replace(original_word, replacement_word)
        count_replacements = self.text.count(original_word)
        return new_text, count_replacements

input_text = input()
original_word = input()
replacement_word = input()

processor = TextProcessor(input_text)
replaced_text, replacements_count = processor.replace_word(original_word, replacement_word)
print(replaced_text)
print(replacements_count)