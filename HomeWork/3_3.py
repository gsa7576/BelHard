
# Дан список чисел и на вход поступает число N, необходимо сместить список на
# указанное число, пример: [1,2,3,4,5,6,7] N=3 ответ: [5,6,7,1,2,3,4]
#
spisok_chisel = [1,2,3,4,5,6,7]
print(spisok_chisel)
n=3
for i in range(len(spisok_chisel)-1, len(spisok_chisel)):
    #print(len(spisok_chisel))
    for i in range(n):
        spisok_chisel.insert(0, spisok_chisel.pop())
print(spisok_chisel)








