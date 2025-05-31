list_of_graphic_cards: list = []
count_number_graphic = int(input('Количество видеокарт: '))

for number_graphic_card in range(count_number_graphic):
    graphic_card = int(input(f'Видеокарта {number_graphic_card + 1}: '))
    list_of_graphic_cards.append(graphic_card)


print(f'Старый список видеокарт: {list_of_graphic_cards}')

max_card = max(list_of_graphic_cards)

new_graphic_cards = [
    card for card in list_of_graphic_cards if card != max_card
    ]

print(f'Новый список видеокарт: {new_graphic_cards}')
