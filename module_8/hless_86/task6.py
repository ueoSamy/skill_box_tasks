print('Задача 6. Письмо')

# У нас есть
# квадратный конверт размера 12х12 сантиметров и письмо на квадратном листе бумаги,
# которое не помещается в конверт.
#
# Напишите программу,
# которая подскажет сколько раз нужно сложить письмо пополам,
# чтобы оно поместилось в конверт.
# Размеры письма вводятся с клавиатуры.
size_of_paper = int(input('Введите размер бумаги: ')) ** 2
size_of_conv = 12 ** 2
count = 0
for val in range(size_of_paper // size_of_conv):
    size_of_paper //= 2
    print(size_of_paper)
    count += 1
    if size_of_paper <= size_of_conv:
        print('finish')
        break

print(f'{count} раза')