# Задача 3. Бактерии живут комфортно
# Биолог Арсений изучает микробы и их поведение при разных температурных нагрузках.
# Он помещает их в специальную среду, где температура скачет в промежутке от 0 до 100 градусов.
# Если же температура в среде выходит за рамки промежутка, то выводится предупреждение.
# Напишите программу, которая запрашивает у пользователя температуру, и, если она меньше нуля или больше 100,
# то выводится сообщение об опасности

temperature = int(input('Введите температуру: '))
if temperature < 0 or temperature > 100:
    print('Внимание опасность!')
else:
    print('Температура в пределах нормы!')
