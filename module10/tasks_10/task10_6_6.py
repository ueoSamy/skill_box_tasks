print('Задача 6. Сумма факториалов')

# Напишите программу,
# которая запрашивает у пользователя число N
# и находит сумму факториалов 1! + 2! + 3! +... + N!
# 2 * 3 * 4 + 2 * 3 * 4 * 5
user_in = int(input('Введите значение N: '))
fact = 1
sum_fact = 0
for i in range(1, user_in + 1):
    for k in range(1, i):
        fact = fact * (i * k)
    sum_fact += fact
    print(f'{i}!', end='')
    if i == user_in:
        print(' =', end='')
    else:
        print('+', end='')

print(f' {sum_fact:.2f}')
