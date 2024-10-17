# Преподаватель отправил студентам ведомости с оценками за экзамен. Определите, удалось ли всем студентам в группе набрать проходной балл или выше. 
# Проходной балл — 35. Если есть студенты, которые не набрали проходной балл, выведите их имена.
# Формат ввода
# Первая строка: целые числа, разделенные запятыми, означающие баллы учеников (1 ≤ x ≤ 55). Вторая строка: имена учеников, также разделенные 
# запятыми. Гарантируется, что число баллов равно числу имен учеников.
# Формат вывода
# Одна строка: «Все сдали», если все ученики набрали баллы 35 и выше.
# В противном случае — «Есть несдавшие» (обе фразы без кавычек), а на следующих строках вывести имена студентов, которые не сдали.

def check_all_students_passed(scores_input: str, names_input: str) -> str:
    scores = list(map(int, scores_input.split(',')))
    names = names_input.split(',')

    failed_students = [names[i] for i in range(len(scores)) if scores[i] < 35]

    if not failed_students:
        return "Все сдали"
    else:
        return "Есть несдавшие\n" + '\n'.join(failed_students)


scores_input = input()
names_input = input()
result = check_all_students_passed(scores_input, names_input)
print(result)