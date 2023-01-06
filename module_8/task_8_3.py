# Задача 1. Степень нечётного числа
# Выведите третью степень каждого нечётного числа в диапазоне от единицы до указанного пользователем числа включительно.
# Для этого используйте шаг внутри функции range.

end_number = int(input('Введите число: '))

for num in range(1, end_number, 2):
    print(f'{num} ** 3 =', num ** 3)

# Задача 2. Театр
# Ваню заставили пойти в театр на балет. Ему стало там настолько скучно,
# что он придумал себе очень странное развлечение: считать сумму номеров каждого пятого стула в рядах.
#
# Напишите программу для вычисления суммы каждого пятого числа, лежащего в диапазоне от единицы до N.
# Использовать условный оператор нельзя.
#
# Пример:
#
# Введите число: 21
# Номер стула: 1
# Номер стула: 6
# Номер стула: 11
# Номер стула: 16
# Номер стула: 21
# Сумма: 55

end_num = int(input('Введите число N: '))
count = 0

for num in range(1, end_num, 5):
    count += 1
    print(num)


# Задача 3. Диета
# Саша просыпается когда угодно, но в 23 часа уже точно идёт спать.
# Питается Саша следующим образом: каждые 3 часа он выпивает литр воды и съедает N калорий.
# Пить и есть он, кстати, начинает сразу как только проснётся. Напишите программу,
# которая считает сколько он выпьет литров воды и сколько калорий он съест перед тем как пойдёт спать.

wake_up = int(input('Во сколько проснулся Саша?: '))
water_sum = 0
calories_sum = 0

for hours in range(wake_up, 23, 3):
    water = int(input('Сколько литров воды выпил Саша?: '))
    water_sum += water
    calories = int(input('Сколько ккалорий сьел Саша?: '))
    calories_sum += calories
print('Сьедено калорий', calories_sum, ', выпито воды', water_sum)