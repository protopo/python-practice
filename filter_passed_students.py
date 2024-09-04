# Легкий
# Основы синтаксиса
# Списки
# Циклы
# Условия
#
# Преподаватель отправил студентам ведомости с оценками за экзамен.
# Определите, кто из студентов набрал проходной балл: 35 баллов или больше.
# Максимальный балл за экзамен — 55 баллов. Если никто не набрал проходной балл, верните «Никто»‎.‎
# Формат ввода
# Две строки. Первая строка — целые числа, означающие баллы учеников (0 ≤ x ≤ 55), они разделены запятой.
# Вторая строка — имена учеников, также разделенные через запятую.
# Гарантируется, что количество оценок и имён в двух строках совпадают.
# Формат вывода
# Имена тех учеников, которые набрали проходной балл на экзамене, в их изначальном порядке.
# Каждое имя должно начинаться с новой строки, в выводе не должно быть запятых.
# Строка «Никто», если никто не набрал проходной балл.
# Пример 1
# Входные данные:
# 0,0,55,55
# Katrin,Marina,Vital,Ramin
# Выходные данные:
# Vital
# Ramin
# Пример 2
# Входные данные:
# 1,2
# Alex,Ivan
# Выходные данные:
# Никто

def filter_passed_students(score_string: str, name_string: str) -> list[str]:
    passed_students = []
    scores = score_string.split(",")
    names = name_string.split(",")
    for i in range(len(scores)):
        if int(scores[i]) > 34 and int(scores[i]) < 56:
            passed_students.append(names[i])
    if not passed_students:
        passed_students.append("Никто")
    return passed_students

score_string = input()
name_string = input()
passed_students = filter_passed_students(score_string, name_string)
for student in passed_students:
    print(student)