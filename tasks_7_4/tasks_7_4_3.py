# Задача 3. Поел - можно и поспать, поспал - можно и поесть
# Напишите программу, разобранную в уроке.
#
# У Саши интересный режим сна: он может проснуться когда угодно, хоть ночью,
# но засыпает всегда до того, как наступит полночь, обычно в 23 часа. А ещё он очень любит поесть.
# Он ест каждый час и если съедает больше 2000 калорий, то он просто падает спать.
# Напишите программу, которая поможет Саше понять, всё ли с ним хорошо.
# Для этого нужно посчитать, сколько он всего съест калорий и сколько часов будет бодрым.

wake_up = int(input('Во сколько Саша проснулся?: '))
awake_h = 0
calories_summ = 0

for i in range(wake_up, 23):
    print('Сейчас ', i, 'часов')
    calories = int(input('Сколько калорий употреблял Саша?: '))
    calories_summ += calories
    if calories_summ >= 2000:
        print('Хорошо поели можно поспать!')
        break
    awake_h += 1

print('Саша съел калорий: ', calories_summ, 'и был бодрым ', awake_h, 'часов')