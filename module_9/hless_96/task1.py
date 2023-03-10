# Задача 1. Календарь
# Что нужно сделать
#
# Мы продолжаем разрабатывать удобный календарь для смартфона. Функцию определения високосного года мы добавили,
# но забыли ещё много разных очевидных вещей.
#
# Напишите программу, которая принимает от пользователя день недели в виде строки и выводит его номер на экран.

# Пример:
#
# Введите день недели: вторник
#
# Номер дня недели: 2

# Советы и рекомендации
#
# Рекомендуется использовать цикл for и список/кортеж для представления дней недели
#
# for day in (‘понедельник’, ‘вторник’, ‘среда’...):

# Советы и рекомендации
#
# Рекомендуется использовать цикл for и список/кортеж для представления дней недели

days = ['', 'понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']
user_input = input('Выедите день недели: ')
count = 1
for day in range(1, len(days[1:]) + 1):
  if user_input == days[day]:
    print(f'Номер дня недели: {day}')
    break