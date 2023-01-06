# Задача 1. Доска
# Используя новые знания с циклами и оператором end, выведете на экран “доску”, которую вы делали в первом модуле

enter_symbol = input('Введите сивол: ')
column = 10
row = 10

for i in range(1, column + 1):
  if i == 1:
    print(' -' * column, end=' \n')
  print('| ', end='')
  print((enter_symbol + ' ') * row, end='')
  print('|')
  if i >= row:
    print(' -' * column, end=' ')