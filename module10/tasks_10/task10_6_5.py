print('Задача 5. Простые числа')


# Напишите программу,
# которая считает количество простых чисел в заданной последовательности
# и выводит ответ на экран.

lower_value = int(input("Введите наименьшее значение диапазона: "))
upper_value = int(input("Введите значение верхнего диапазона: "))

print("Простые числа в заданной последовательности: ")
for number in range(lower_value, upper_value + 1):
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                break
        else:
            print(number)
