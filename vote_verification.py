# Функция для ввода данных, их проверки и форматирования:
# проверка ввода числа с повторным запросом при ошибке ввода,
# удаление возможных пробелов по краям каждого из ответов,
# перевод букв в нижний регистр,
# ошибочный ввод ДА и НЕТ не фильтруется (кроме регистра).'
def input_and_formatting():
    while True:
        try:
            age = int(input("Введите Ваш возраст ").strip())
            break
        except ValueError:
            print("Пожалуйста, введите число для возраста.")
    citizen = input("Являетесь ли Вы гражданином страны? Введите ДА или НЕТ ").strip().lower()
    disqualification = input("""Есть ли у Вас диквалификация на участие в выборах? 
(например, по причине уголовного наказания)
Введите ДА или НЕТ """).strip().lower()
    return age, citizen, disqualification


# Функция проверки условий участия в выборах и вывода результата
def analyzing_and_output(age, citizen, disqualification):
    if age >= 18 and citizen == "да" and disqualification == "нет": # проверка выполнения 3х условий одновременно
        print('Вы можете голосовать на выборах.')
    else:
        print('Вы не можете голосовать на выборах.')


age, citizen, disqualification = input_and_formatting()
analyzing_and_output(age, citizen, disqualification)