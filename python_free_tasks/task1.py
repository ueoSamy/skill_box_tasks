height = int(input('Введите высоту пирамиды: '))
for i in range(height):
  print(' ' * (height - i - 1) + '#' * (i * 2 + 1))