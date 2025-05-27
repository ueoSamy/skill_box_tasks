def reverse_number(num):
    reversed_num = int(str(num)[::-1])
    return reversed_num

# Основная программа
N = int(input("Введите первое число: "))
K = int(input("Введите второе число: "))

reversed_N = reverse_number(N)
reversed_K = reverse_number(K)

print(f"Первое число наоборот: {reversed_N}")
print(f"Второе число наоборот: {reversed_K}")