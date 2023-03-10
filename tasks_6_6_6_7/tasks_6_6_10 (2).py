print('Задача 10. Игра «Компьютер угадывает число»')

# Поменяйте мальчика и компьютер из прошлой задачи местами.
# Теперь мальчик загадывает число между 1 и 100 (включительно).
# Компьютер может спросить у мальчика:
# «Твое число равно, меньше или больше, чем число N?»,
# где N — число, которое хочет проверить компьютер.
# Мальчик отвечает одним из трёх чисел:
# 1 — равно,
# 2 — больше,
# 3 — меньше.

# Напишите программу,
# которая с помощью цепочки таких вопросов и ответов мальчика угадывает число.

# Дополнительно: сделайте так, чтобы можно было гарантированно угадать число за семь попыток.
high = 100
low = 1
number = (low + high) // 2

while True:
    print(f'Твое число равно, меньше или больше, чем число {number}?:')
    user_answer = int(input('1 - равно\n2 - больше\n3 - меньше\nВаш ответ: '))
    if user_answer == 1:
        print('Компьютер угадал число!')
        break
    elif user_answer == 2:
        low = number + 1
        number = (low + high) // 2

    elif user_answer == 3:
        high = number - 1
        number = (low + high) // 2
