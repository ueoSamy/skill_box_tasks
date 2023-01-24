size = int(input('Введите размер матрицы: '))

for row in range(size):
    for col in range(size):
        if row < col:
            print(0, end=' ')
        elif row > col:
            print(2, end=' ')
        else:
            print(1, end=' ')
    print()

# результат:
# 1 0 0 0 0 0
# 2 1 0 0 0 0
# 2 2 1 0 0 0
# 2 2 2 1 0 0
# 2 2 2 2 1 0
# 2 2 2 2 2 1
