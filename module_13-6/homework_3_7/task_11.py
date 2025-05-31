number_count = int(input("Количество чисел: "))

number_list = [int(input("Число: ")) for _ in range(number_count)]

print(f"\nПоследовательность: {number_list}")

numbers_to_append = []

for start_index in range(number_count):
    subsequence = number_list[start_index:]

    is_palindrome = True
    left = 0
    right = len(subsequence) - 1

    while left < right:
        if subsequence[left] != subsequence[right]:
            is_palindrome = False
            break
        left += 1
        right -= 1

    if is_palindrome:
        numbers_to_append = number_list[:start_index][::-1]
        break

print(f"Нужно приписать чисел: {len(numbers_to_append)}")
print(f"Сами числа: {numbers_to_append}")