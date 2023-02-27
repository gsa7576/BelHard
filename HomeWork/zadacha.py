#while not(a:=input().isdigit()):

#   print(a)

# a=input()
# for(i in range(a)):
#     print (a)

summ = input()
count=0
nominals={25, 10, 5, 1}
for i in nominals:
    #print(i)
    while int(summ) / i >=1:
        print(i)
        summ = int(summ)-i
        count=count+1
print("----------")
print(count)