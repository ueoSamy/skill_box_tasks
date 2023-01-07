size_y = int(input('Введите размер y row: '))
size_x = int(input('Введите размер x col: '))

for row in range(size_y):
    for col in range(size_x):
        if row == size_y // 2:
            if col == size_x // 2:
                print('+', end='')
            else:
                print('-', end='')
        elif col == size_x // 2:
            print('|', end='')
        else:
            print(' ', end='')
    print()
