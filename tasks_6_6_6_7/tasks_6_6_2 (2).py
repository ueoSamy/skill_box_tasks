print('Задача 2. Коллекторы')

# Напишите робота для коллекторов.
# В самом начале он спрашивает имя должника и сумму долга,
# а затем начинает требовать у него погашения до тех пор,
# пока он не введёт нужную сумму (равную сумме долга или больше).
# После погашения долга сообщите об этом пользователю и поблагодарите его.

# Пример:
# Василий, ваша задолженность составляет 100 рублей.
# Сколько рублей вы внесёте прямо сейчас, чтобы её погасить? 50

# Маловато, Василий. Давайте ещё раз.
# Сколько рублей вы внесёте прямо сейчас, чтобы её погасить? 90
# Маловато, Василий. Давайте ещё раз.

# Сколько рублей вы внесёте прямо сейчас, чтобы её погасить? 110
# Отлично, Василий! Вы погасили долг. Спасибо!

user_name = input('Имя должника: ')
user_debt = int(input('Размер долга: '))
user_deposite = 0  # внесенная сумма
while user_debt > user_deposite:
    print(f'{user_name} ваша задолженность составляет {user_debt} рублей.')
    user_enter = int(input('Сколько рублей вы внесёте прямо сейчас, чтобы её погасить?: '))
    user_deposite += user_enter
    user_debt -= user_deposite

print('Ваш долг погашен')