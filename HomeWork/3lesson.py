# from string import printable
# text=input('введите текст для отправки')
# llistt=[*text]
# #int(llistt)
# count1: int=0
# for i in llistt:
#    #print(i)
#     if i in printable:
#         count1+=1
#     else:
#         count1+= 2
# #print(count1)
# res = count1//140 +1
# print(res)



# soob='LONDON'
# key='SYSTEM'
# for i in soob:
#     s=bin(ord(i))[2:].zfill(8)
#
#     print(s)


spis=[1,2,5,8,3,6,2,6,8,0,2,5,1,7]
for i in range(len(spis)):
    now=spis[int(i)]
    sort(now, spis)


    print(now);
    for ii in range(len(spis)):
        if now>spis[ii]:
            arr[-1], arr[i] = arr[i], arr[-1]
