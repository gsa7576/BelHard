
# Заполнить список степенями числа 2 (от 2^1 до 2^n).

# Без использования collections, написать программу, которая будет
# создавать словарь для подсчитывания количества вхождений каждой
# буквы в текст введенный с клавиатуры

# *Заполнить словарь где ключами будут выступать числа от 0 до n, а
# значениями вложенный словарь с ключами "name" и "email", а значения
# для этих ключей будут браться с клавиатуры.



print("Введите текст с клавиатуры")
text = input()
listt=[*text]
print(listt)
unique_letters = list(set(listt))
print(unique_letters)
slovar = dict()
for i in unique_letters:
    print(i, end='')
    print(' = ', end='')
    print(text.count(i))
    slovar[i] = text.count(i)
print(slovar)

# Введите текст с клавиатуры
# fcqadc werg yik 6i
# <class 'list'>
# ['6', 'c', 'q', 'i', 'r', 'y', 'e', 'k', 'g', 'w', ' ', 'f', 'a', 'd']
# 6 = 1
# c = 2
# q = 1
# i = 2
# r = 1
# y = 1
# e = 1
# k = 1
# g = 1
# w = 1
#   = 3
# f = 1
# a = 1
# d = 1
# {'6': 1, 'c': 2, 'q': 1, 'i': 2, 'r': 1, 'y': 1, 'e': 1, 'k': 1, 'g': 1, 'w': 1, ' ': 3, 'f': 1, 'a': 1, 'd': 1}
#
# Process finished with exit code 0
