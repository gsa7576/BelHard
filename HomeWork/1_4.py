# Пользователь вводит 3 числа, сказать сколько из них положительных
# и сколько отрицательных

print("Введите первое число")
ch1 = input()

print("Введите второе число")
ch2 = input()

print("Введите третье число")
ch3 = input()

ch1 = int(ch1)
ch2 = int(ch2)
ch3 = int(ch3)

ch1_is_positie = ch1 > 0
ch2_is_positie = ch2 > 0
ch3_is_positie = ch3 > 0
print("positie")
print(ch1_is_positie + ch2_is_positie + ch3_is_positie)
print("negotive")
ch1_is_negotive = ch1 < 0
ch2_is_negotive = ch2 < 0
ch3_is_negotive = ch3 < 0

print(ch1_is_negotive + ch2_is_negotive + ch3_is_negotive)