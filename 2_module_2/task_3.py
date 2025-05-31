nums_list = []

N = int(input('Кол-во чисел в списке: '))

for _ in range(N):

    num = int(input('Очередное число: '))

    nums_list.append(num)


maximum = 0

minimum = -1

for i in nums_list:

    if maximum < i:
        maximum = i
    elif minimum > i:
        minimum = i
    else:
        minimum = minimum

print('Максимальное число в списке:', maximum)

print('Минимальное число в списке:', minimum)
