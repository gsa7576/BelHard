# **Вывести четные числа от 2 до N по 5 в строку

print("Какое максимальное число")
n = int(input())
ii=1
for i in range(2, n, 2):
    print(i, end=' ')
    if ii%5==0:
        print("")
    ii+=1

