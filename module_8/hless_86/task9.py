print('Задача 9. Выражение')

# Дано число x.
# Напишите программу для вычисления следующего выражения

# ((x-1)(x-3)(x-7)…(x-63)/
# ((x-2)(x-4)(x-8)…(x-64))
result = True
down_n = 1
up_n = 1
x = int(input('Значение для x: '))
for i in range(1, 7):
    if i % 2 == 0:
        down_n *= (x - 2 ** i)
        print(f'down = {x} - {i}')
    else:
        if down_n == 1:
            up_n = up_n * (x - i)
            print(f'up = {x} - {i}')
        else:
            up_n = up_n * (x - (down_n - i))
            print(f'up = {x} - {i}')
        if up_n == 0:
            print('Деления на 0!')
            result = False
            break
    print('*************')

if result:
    res = up_n / down_n
    print(f'Результат: {res}')