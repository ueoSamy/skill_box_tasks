print('Задача 7. Стипендия')

# Ежемесячная стипендия студента составляет educational_grant руб.,
# а расходы на проживание превышают стипендию и составляют expenses руб. в месяц.
# Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца.
#
# Составьте программу расчета суммы денег,
# которую необходимо получить у родителей один раз в начале обучения,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.
educational_grant = int(input('Введите значение: '))
expenses = int(input('Введите значение: '))
edu_month = 10
for i in range(1, edu_month):
    i += 1
    expenses += expenses * 0.03
    print(f'Расход {i} месяца: {expenses}')

print(f'Необходамая сумма от родителей {expenses - educational_grant} руб')