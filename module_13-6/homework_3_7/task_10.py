def find_last_survivor(number_of_people, elimination_number):
    # Создаем список людей в круге
    people_in_circle = list(range(1, number_of_people + 1))
    
    # Текущая позиция, с которой начинается отсчёт
    current_position = 0

    while len(people_in_circle) > 1:
        print(f"\nТекущий круг людей: {people_in_circle}")
        print(f"Начало счёта с номера {people_in_circle[current_position]}")

        # Вычисляем индекс человека, который выбывает
        current_position = (current_position + elimination_number - 1) % len(people_in_circle)
        eliminated_person = people_in_circle.pop(current_position)

        print(f"Выбывает человек под номером {eliminated_person}")

    print(f"\nОстался человек под номером {people_in_circle[0]}")


# Получаем данные от пользователя
number_of_people = int(input("Количество человек: "))
elimination_number = int(input("Какое число в считалке? "))

print(f"\nЗначит, выбывает каждый {elimination_number}-й человек\n")

# Запускаем функцию
find_last_survivor(number_of_people, elimination_number)