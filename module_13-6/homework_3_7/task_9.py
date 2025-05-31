number_of_skates = int(input("Количество роликов: "))
roller_sizes = [int(input(f"Размер пары {i + 1}: ")) for i in range(number_of_skates)]

number_of_people = int(input("Количество людей: "))
foot_sizes = [int(input(f"Размер ноги человека {i + 1}: ")) for i in range(number_of_people)]

roller_sizes.sort()
foot_sizes.sort()

roller_index = 0
person_index = 0
people_fitted = 0

while roller_index < number_of_skates and person_index < number_of_people:
    current_roller_size = roller_sizes[roller_index]
    current_foot_size = foot_sizes[person_index]

    if current_roller_size == current_foot_size:
        people_fitted += 1
        roller_index += 1
        person_index += 1
    elif current_roller_size < current_foot_size:
        roller_index += 1
    else:
        person_index += 1

print("Наибольшее количество людей, которые могут взять ролики:", people_fitted)