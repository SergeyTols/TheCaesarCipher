abc = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
#  abc += abc.upper()
#  abc_u = abc.upper()
while True:
    print('Введите E - чтобы зашифровать сообщение, D - чтобы расшифровать или Q -  чтобы выйти')
    choice = input('>>> ').lower()
    if choice == 'q':
        break
    elif not (choice == 'e' or choice == 'd'):
        continue
    new_word = ''
    word = input('Введите слово: ').lower()
    #  word = input('Введите слово: ')
    step = int(input('Введите шаг: '))
    if choice == 'd':
        step *= -1
    for letter in word:
        if letter in abc:
            i = abc.index(letter)
            new_letter = (i + step) % len(abc)
            new_word += abc[new_letter]
    print('Результат: ' + new_word)







