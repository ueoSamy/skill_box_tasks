# Задача 3. Табло
# Петя пишет компьютерную спортивную игру, где каждый “гол” это десять очков.
# Он хочет сделать красивое табло с градацией этих очков.

# Пользователь вводит число N (N >= 0). Реализуйте программу, которая выводит в одну строчку каждое десятое число,
# разделяя их символами “-=-”. Эти же символы стоят перед первым числом и после последнего.

# Пример:

# Введите число: 50

# -=- 0 -=- 10 -=- 20 -=- 30 -=- 40 -=- 50 -=-
goal = int(input('Выедите число: '))
for i in range(10, goal + 10, 10):
  print(i, end = '-=-')