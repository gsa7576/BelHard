# 4. Изменить класс выше, список категорий должен содержать не просто имена категорий, а
# словари с данными о каждой категории (name: str, is_published: bool), а так же изменить
# методы add, get, delete, update для работы с списком словарей

# 4.1 Добавить метод make_published принимающий индекс категории и меняющий значение
# ключа is_published на True, если такого индекса нет, вызвать исключение IndexError
# 4.2 Добавить метод make_unpublished принимающий индекс категории и меняющий
# значение ключа is_published на False, если такого индекса нет, вызвать исключение
# IndexError


class Category:
    categories = [{"name": "журнал", "is_published": 1}, {"name": "книга", "is_published": 0},
                  {"name": "тетрадь", "is_published": 1}, ]
    i = -1

    @classmethod
    def add(cls, value: dict) -> int:
        for x in cls.categories:
            #print(x['name'], end=' = ')
            #print(value['name'])
            need_t_add = 0
            if x['name'] == value['name']:
                pass
            else:
                need_t_add = 1
        if need_t_add == 1:
            print("Добавляем значение")
            cls.categories.append(value)
        else:
            raise ValueError('category is not unique')

    @classmethod
    def gettt(cls, i):
        return cls.categories[i]

    @classmethod
    def delete(cls, i):
        try:
            del cls.categories[i]
        except IndexError:
            pass

    @classmethod
    def update(cls,  value):
        updated=0
        for i in cls.categories:
            if i['name'] == value['name']:
                i['is_published']=value['is_published']
                updated = 1


    @classmethod
    def make_published(cls,  index):
        updated = 0
        for i in cls.categories:
            if i['name'] == index:
                i['is_published'] = 1
                updated = 1
        if updated == 0:
            raise IndexError('category is not ')

    @classmethod
    def make_unpublished(cls,  index):
        updated = 0
        for i in cls.categories:
            if i['name'] == index:
                i['is_published'] = 0
                updated = 1
        if updated == 0:
            raise IndexError('category is not ')

cat = Category()
print(cat.categories)
new = {"name": "дневник", "is_published": 1}
cat.add(new)
print(cat.categories)

print(cat.gettt(2)) # {'name': 'тетрадь', 'is_published': 1}

cat.delete(2)
print(cat.categories)

new2 = {"name": "дневник", "is_published": 0}
print(cat.update(new2))
print(cat.categories)

cat.make_published('дневник')
print(cat.categories)

cat.make_unpublished('дневник')
print(cat.categories)