# Задача 10. Метод бутерброда
# Что нужно сделать
#
# Секретное агентство «Super-Secret-no» решило для шифрования переписки своих сотрудников использовать «метод бутерброда».
# Сначала буквы слова нумеруются в таком порядке: первая буква получает номер 1,
# последняя буква - номер 2, вторая – номер 3, предпоследняя – номер 4, потом третья… и так для всех букв (см. рисунок).
# Затем все буквы записываются в шифр в порядке своих номеров.

# Например, слово «sandwich» зашифруется в «shacnidw».
#
# К сожалению, программист «Super-Secret-no», написал только программу шифрования и уволился.
# И теперь агенты не могут понять, что же они написали друг другу. Помогите им написать программу-дешифратор,
# которая бы расшифровывала введенные сообщения.

# Пример:
#
# Введите зашифрованное сообщение: shacnidw
#
# Расшифрованное сообщение: sandwich

# Правильно:
#
# if a > 1:
#     b = 3
# else:
#     b = 5
#
# Неправильно:
#
# If
# a > 1:
# b = 3
# else:
# b = 5

# Переменные имеют корректные названия, и в качестве имён не используются имена встроенных функций
# (список встроенных функций — официальная документация).

user_input = input('Введите зашифрованое слово: ')
word1 = ' '
word2 = ' '
count = 0

for elem in user_input:
    count += 1
    if (count % 2 == 1):
        word1 += elem
    else:
        word2 += elem

print('Расшифрованое слово:', word1 + word2)