# Задача 1. Неправильный таймер
# Петя писал таймер для телефона, но у него что-то пошло не так.

count = 10
while count > 0:
    print(count)
    count -= 1
    if count == 0:
        print('Время вышло!')

