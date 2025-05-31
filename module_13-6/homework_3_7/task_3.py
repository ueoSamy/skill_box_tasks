original_list = [5, 6, 7, 1, 2, 3, 4]

shift_amount = int(input("Сдвиг: "))

list_length = len(original_list)

if list_length == 0:
    print("Пустой список")
else:
    shift_amount = shift_amount % list_length

    shifted_list = original_list[-shift_amount:] + original_list[:-shift_amount]

    print("Сдвинутый список:", shifted_list)
