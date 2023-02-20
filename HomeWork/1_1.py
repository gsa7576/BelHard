# Пользователь вводит предложение, заменить все пробелы на "-" 2-мя
# способами

print("Введите предложение")
sentense = input()
var1 = sentense.replace(" ", "--")
print(var1)



var2 = sentense.split(" ")
ii = 1
for i in var2:
    if ii != 1:
        print("--",  end="")
    ii += ii
    print(i,   end="")



