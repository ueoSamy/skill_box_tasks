# Задача 2. Таблица суммы
# Напишите программу, которая запрашивает у пользователя число N и выводит таблицу суммы для чисел от 1 до N.

# Пример:

user_input = int(input('Введите число N: '))

for row in range(user_input + 1):
    for col in range(user_input + 1):
        print(row + col, end='\t')
    print()
