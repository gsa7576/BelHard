# Вывести первые N цисел кратные M и больше K

# Сделать калькулятор: у пользователя
# спрашивается число, потом действие и второе
# число

# **Вывести четные числа от 2 до N по 5 в строку

print("Сколько чиссел вывести N")
n = int(input())

print("Чему кратно М")
m = int(input())

print("Больше  какого числа К")
k = int(input())


for i in range(k, k*2, 1):
    if i%m == 0:
        need_i=i
        #print(need_i)
        max=need_i+m*n
        for ii in range(need_i, max, m):

            #print(need_i+m*n)
            print(ii)
        break

# Сколько чиссел вывести N
# 3
# Чему кратно М
# 11
# Больше  какого числа К
# 23
# 33
# 44
# 55
#
# Process finished with exit code 0