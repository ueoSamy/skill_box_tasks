def reverse_number(num):
    reversed_num = int(str(num)[::-1])
    return reversed_num


# Основная программа
first_num = int(input("Введите первое число: "))
second_num = int(input("Введите второе число: "))

reversed_first_num = reverse_number(N)
reversed_second_num = reverse_number(K)

print(f"Первое число наоборот: {reversed_first_num}")
print(f"Второе число наоборот: {reversed_second_num}")
