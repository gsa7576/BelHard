# Пользователь вводит 3 числа, найти среднее арифмитическое с
# точность 3

print("Введите первое число")
ch1 = input()

print("Введите второе число")
ch2 = input()

print("Введите третье число")
ch3 = input()

res = float((int(ch1)+int(ch2)+int(ch3)) / 3)
print("%.3f" % res)


