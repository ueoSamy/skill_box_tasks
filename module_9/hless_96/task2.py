# Задача 2. Я стал новым пиратом!
# Что нужно сделать
#
# Старому капитану необходимо пополнить команду. Но попадут на его корабль только достойные! Он отобрал 10 человек и те,
# кто из них крикнет слово “Карамба”, попадут на борт.
#
# Пользователь вводит 10 слов. Напишите программу, которая определяет, сколько из них совпадают со словом «Карамба».

words = input('Выедите 10 слов: ')
to_find = 'карамба'
for word in words:
  if to_find in words:
    print('Попадает на борт')
    break
  else:
    print('Не попадает на борт')