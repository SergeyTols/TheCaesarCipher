abc = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

while True:
    print('Введите E чтобы зашифровать сообщение, D чтобы расшифровать и Q чтобы выйти')
    choice = input('>>> ').lower()
    if choice == 'q':
        break
    elif not (choice == 'e' or choice == 'd'):
        continue
    new_word = ''
    word = input('Введите слово: ').lower()
    step = int(input('Введите шаг: '))
    if choice == 'd':
        step *= -1
    for letter in word:
        if letter in abc:
            i = abc.index(letter)
            new_letter = (i + step) % 33
            new_word += abc[new_letter]
    print('Результат: ' + new_word)






