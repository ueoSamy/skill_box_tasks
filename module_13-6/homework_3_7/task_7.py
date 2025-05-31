shop = [
    ['каретка', 1200],
    ['шатун', 1000],
    ['седло', 300],
    ['педаль', 100],
    ['седло', 1500],
    ['рама', 12000],
    ['обод', 2000],
    ['шатун', 200],
    ['седло', 2700]
]

detail_name = input("Название детали: ").lower()

count = 0
total_price = 0

for name, price in shop:
    if name.lower() == detail_name:
        count += 1
        total_price += price

print(f"Количество деталей: {count}")
print(f"Общая стоимость: {total_price}")
