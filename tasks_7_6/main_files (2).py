# Цель задания
# Научиться работать с циклом For и счетчиками.

# Что нужно сделать:
# Зайдите в файлы с заданиями и выполните так чтобы вывод соотвествовал
# ЗАДАНИЕ 1
print('Задача 1. Тайны археологии')

for i in 114, 12, 14, 10605, 4907, 450:
    if i % 2 == 0 and i % 3 != 0:
        print('Число подходит!')
    else:
        print('Число не подходит!')

# ЗАДАНИЕ 2
print('Задача 2. Должники')
even_nums = 0
count_numbers = int(input('Количество чисел: '))
for count in range(count_numbers + 1):
    number = int(input('Введите число: '))
    if number > 0:
        if number % 2 == 0:
            even_nums += 1

print(even_nums, 'чисел из введенных являются четными и положительными')

# ЗАДАНИЕ 3
print('Задача 3. Посчитай чужую зарплату...')

month_count = 12
summ_salary = 0
result = 0
for count in range(1, month_count + 1):
    emp_salary = int(input('Введите зарплату сотрудника за текущий месяц: '))
    summ_salary += emp_salary
    if count == month_count:
        result = summ_salary / month_count
print('Средняя зарплата сотрудника за год составляет', result)

# ЗАДАНИЕ 4
print('Задача 4. С заботой о природе')

start_sector = int(input('Начальный сектор: '))
end_sector = int(input('Конечный сектор: '))
violations = 0
for sector in range(start_sector, end_sector):
    people = int(input('Сколько людей на секторе: '))
    if people <= 10:
        print('Все спокойно!')
    else:
        violations += 1
        print('Нарушение! Слишком много людей на секторе!')

print('Количество нарушений:', violations)

# ЗАДАНИЕ 5
print('Задача 5. Факториал')

N = int(input('Введите число: '))
factorial = 0
for num in range(1, N):
    factorial *= num

print('Факториал числа равен:', factorial)

# ЗАДАНИЕ 6
print('Задача 6. Успеваемость в классе')

count_marks = 0
five_students = 0
four_studets = 0
three_students = 0

for elem in range(1, count_marks):
    enter_mark = int(input('Введите оценку: '))
    if enter_mark == 5:
        five_students += 1
    elif enter_mark == 4:
        four_studets += 1
    else:
        three_students += 1

if five_students > four_studets > three_students:
    print('Сегодня отличников больше')
elif four_studets > five_students > three_students:
    print('Сегодня больше хорошистов')
elif three_students > four_studets > five_students:
    print('Сегодня больше троечников')
else:
    print('Количество одинаковы')

# ЗАДАНИЕ 7
print('Задача 7. Отрезок')

start_num = int(input('Введите начальное значение: '))
end_num = int(input('Введите конечное значение: '))
count = 0
summ_num = 0

for num in range(start_num, end_num):
    if num % 3 == 0:
        summ_num += num
        count += 1

print(count, 'числы кратны к 3 от', start_num, 'до', end_num)
print('Среднее арифметическое всех чисел', summ_num // count)

# ЗАДАНИЕ 8
print('Задача 8. Замечательные числа')

for elem in range(10, 100):
    if elem // 100 == 0:
        num_1 = elem % 10
        num_2 = elem // 10
        if (num_1 * num_2) * 3 == elem:
            print(elem, '- замечательное число')

# ЗАДАНИЕ 9
print('Задача 9. ...Теперь можно посчитать и свою')

var_salary = 0

for i in range(1, 10):
    salary = int(input('выедите число: '))
    if salary >= var_salary:
        print('все в порядке')
    else:
        print('числа не по порядку')
    var_salary = salary

# ЗАДАНИЕ 10
print('Задача 10.')

total_cards = int(input('Введите количество карточек: '))
cards_sum1 = total_cards
cards_sum2 = 0
lost_card = 0

for num in range(1, total_cards):
    cards_sum1 += num
    cards_sum2 += int(input('Введите остальные карты: '))

lost_card = cards_sum1 - cards_sum2
print('Номер пропавшей карточки:', lost_card)


