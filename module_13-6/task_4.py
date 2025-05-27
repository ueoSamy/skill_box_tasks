def count_numbers(num):
    return len(str(num))


def change_number(num):
    num_str = str(num)
    first_digit = num_str[0]
    last_digit = num_str[-1]
    middle = num_str[1:-1]
    changed_num = int(last_digit + middle + first_digit)
    return changed_num


def main():
    num1 = input("Введите первое число (не менее 3 цифр): ")
    num2 = input("Введите второе число (не менее 4 цифр): ")

    if count_numbers(num1) < 3 or count_numbers(num2) < 4:
        print("Ошибка: числа должны содержать необходимое количество цифр!")
        return

    num1 = int(num1)
    num2 = int(num2)

    changed_num1 = change_number(num1)
    changed_num2 = change_number(num2)

    print(f"Изменённое первое число: {changed_num1}")
    print(f"Изменённое второе число: {changed_num2}")
    print(f"Сумма изменённых чисел: {changed_num1 + changed_num2}")


main()
