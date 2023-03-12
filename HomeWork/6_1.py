# 1. Написать модели SQLAlchemy к представленной структуре БД
# 2. Инициализировать alembic и провести миграции
# 3. Написать Модели Pydantic для каждой модели SQLALchemy
# 4. Написать функцию, которая будет заполнять любую таблицу на основании файла CSV через SQLAlchemy, предварительно
# валидируя с помощью pydantic
# 5. Написать функцию выгрузки из таблицы в файл CSV с использованием SQLAlchemy


from sqlalchemy import Column, INT, VARCHAR, DECIMAL, ForeignKey
from sqlalchemy.orm import DeclarativeBase, declared_attr


class Base(DeclarativeBase):
    pk = Column('id', INT, primary_key=True)

    @declared_attr
    def __table__(cls):
        return ''.join(f'_{i.lower()}' if i.isupper() else i for i in cls.__name__).strip('_')


class Category(Base):
    # __table__ = "category"

    name = Column(VARCHAR(64), nullable=False, unique=True)


class Product(Base):
    # __table__ = "product"

    pk = Column('id', INT, primary_key=True)
    name = Column(VARCHAR(128), nullable=False)
    price = Column(DECIMAL(8, 2), nullable=False)
    category_id = Column(INT, ForeignKey('category.id', ondelete="CASCADE"), nullable=False)
