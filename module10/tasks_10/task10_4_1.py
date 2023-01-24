# Практика
#
# Задача 1. Электронная очередь
# Нам дали заказ написать программу для электронной очереди. У каждого человека в очереди есть номер:
# нулевой, первый, второй, третий и так далее. Каждый час очередь уменьшается на одного человека,
# то есть уходит сначала нулевой номер, затем первый, второй и так далее.
# Наша программа получает на вход одно число — количество людей в очереди —
# и выводит на экран историю обслуживания очереди: какие номера в какой час оставались.
#
people = int(input('Кол-во людей в очереди: '))

for hour in range(people + 1):
    print('Идет час', hour)
    for num in range(hour, people):
        print('Номер в очереди', num)
    print()

print('Очередь обслужена!')