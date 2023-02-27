# Дан список чисел, необходимо для каждого элемента посчитать сумму его
# соседей, для крайних чисел одним из соседей является число с противоположной
# стороны списка
#


spisok_chisel = [1,4,7,5,45,7,8,23,231,33]

#arr = list(map(int, input().split()))
arr = list(spisok_chisel)
arr2 = [arr[-1]] + arr + [arr[0]]
print(*(arr2[i]+arr2[i+2] for i in range(len(arr))))