print('Задача 7. Наибольшая сумма цифр')

# Вводится N чисел.
# Среди натуральных чисел, которые были введены,
# найдите наибольшее по сумме цифр. Выведите на экран это число и сумму его цифр.

numbers = int(input('Сколько чисел будет?: '))
sum_num = 0
sum_loc = 0

for i in range(1, numbers + 1):
    user_input = int(input(f'Введите {i}е число: '))
    print('Введено число:', user_input)
    while user_input > 0:
        sum_loc += (user_input % 10)
        user_input //= 10

    if sum_loc > sum_num:
        sum_num = sum_loc

    print('сумма ее цифр:', sum_loc)
    sum_loc = 0
    print()

print(f'наибольшее сумма цифр {sum_num}')

