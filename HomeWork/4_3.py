# 3. Реализовать класс Category
# Создать атрибут класса categories
# 3.1 Написать метод класса add принимающий на вход название категории, если такой
# категории в атрибуте класса categories нет, добавить данную категорию в список и вернуть
# индекс вхождения новой категории в списке. Если такая категория уже есть, вызвать
# исключение ValueError

# 3.2 Написать метод класса get принимающий индекс и возвращающий категорию из списка
# категорий на этом индексе, если нет элемента на таком индексе, вызвать исключение
# IndexError
# 3.3 Написать метод класса delete принимающий индекс категории в списке категорий и
# удаляющий элемент из списка категорий на этом индексе, если нет элемента на таком
# индексе, ничего не делать, метод ничего возвращать не должен
# 3.4 Написать метод класса update принимающий индекс категорий и новое название
# категории, если нет элемента на таком индексе, то новая категория должна добавляться с
# учетом того, что имена категорий уникальны, если новое имя категории

class Category:

    categories = ['cat1', 'cat2', 'cat3']
    i = -1

    @classmethod
    def add(cls, value: str) -> int:
        """Добавление новой категории

        :param value: название новой категории
        :return: индекс новой категории
        """
        if value.title() not in cls.categories:
            cls.categories.append(value.title())
            return len(cls.categories) - 1
        else:
            raise ValueError('category is not unique')

    @classmethod
    def get(cls, i):
        return cls.categories[i]

    @classmethod
    def delete(cls, i):
        try:
            del cls.categories[i]
        except IndexError:
            pass

    @classmethod
    def update(cls, i, value):
        if i in range(len(cls.categories)):
            if value.title() not in cls.categories:
                cls.categories[i] = value.title()
            else:
                raise ValueError('category is not unique')
        else:
            return cls.add(value)

    def __iter__(self):
        return self

    def __next__(self):
        self.i += 1
        if self.i in range(len(self.categories)):
            return self.categories[self.i]
        else:
            self.i = -1
            raise StopIteration


# print(Category.add.__doc__)
# categories = Category()
# for category in categories:
#     print(category)
