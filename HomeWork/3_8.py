# Дан словарь, ключ - Название страны, значение - список городов, на вход
# поступает город, необходимо сказать из какой он страны
# #

slovar={"Россия":"Москва", "Беларусь":"Минск", "Украина":"Киев"}
#print(slovar)
zapros=input('Введите город')
for i in slovar:
    if zapros in slovar[i]:
        print(i)