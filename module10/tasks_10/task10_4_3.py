# Задача 3. Лестница чисел
# Пользователь вводит число N. Напишите программу, которая по этому числу выводит вот такую лестницу из чисел:

user_enter = int(input('Введите значение: '))
for row in range(user_enter + 1):
    for col in range(user_enter + 1):
        if row <= user_enter:
            if row + col <= user_enter:
                print(row + col, end=' ')
            else:
                print(' ', end='')
    print()
