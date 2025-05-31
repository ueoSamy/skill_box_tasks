films = [
    'Крепкий орешек', 'Назад в будущее', 'Таксист', 'Леон', 
    'Богемская рапсодия', 'Город грехов', 'Мементо', 'Отступники', 'Деревня']

count_of_fav_films = int(input('Сколько фильмов хотите добавить?: '))
list_of_fav_films = []

for number in range(count_of_fav_films):
    name_of_film = input('Введите название фильма: ')
    if name_of_film in films:
        list_of_fav_films.append(name_of_film)
    else:
        print(f'Ошибка: фильма {name_of_film} у нас нет :(')

print(f'Ваш список любимых фильмов: {', '.join(list_of_fav_films)}')
