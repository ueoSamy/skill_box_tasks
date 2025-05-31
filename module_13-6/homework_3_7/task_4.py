word = input("Введите слово: ").strip().lower()

if word == word[::-1]:
    print("Слово является палиндромом")
else:
    print("Слово не является палиндромом")