# s = 'Python'
# # s[3] = 'y' error (immutable)
# # Индекс может быть отрицательным (с конца)
# print(f'Длина слова: {len(s)}')
# print(s[-2])




abc = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
word = 'абстрактно'
# word = 'гдфхугнхрсваяб'
step = 3
new_word = ''
g = ''
n = 33

for letter in word:
        if letter in abc:
            i = abc.index(letter)
            new_letter = (i + step) % 33
            new_word += abc[new_letter]
print('Результат: ' + new_word)

print((0 + 3) % 33)

# гдфхугнхрс






