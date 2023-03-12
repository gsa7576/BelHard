from sqlalchemy import Column, INT, VARCHAR, DECIMAL, ForeignKey, BOOLEAN
from sqlalchemy.orm import DeclarativeBase, declared_attr


class Base(DeclarativeBase):
    pk = Column('id', INT, primary_key=True)

    @declared_attr
    def __tablename__(cls):
        return ''.join(f'_{i.lower()}' if i.isupper() else i for i in cls.__name__).strip('_')


class statuses(Base):
    name = Column(VARCHAR(10), nullable=False, unique=True)


class orders(Base):
    user_id = Column(INT, ForeignKey('users.id', ondelete='CASCADE'),  nullable=False)
    status_id = Column(INT, ForeignKey('statuses.id', ondelete='CASCADE'), nullable=False)


class users(Base):
    name = Column(VARCHAR(24), nullable=False)
    email = Column(VARCHAR(24), nullable=False, unique=True)


class categories(Base):
    name = Column(VARCHAR(24), nullable=False, unique=True)


class products(Base):
    title = Column(VARCHAR(36), nullable=False)
    description = Column(VARCHAR(140), nullable=False)
    category_id = Column(INT, ForeignKey('categories.id', ondelete='CASCADE'), nullable=False)


class order_items(Base):
    order_id = Column(INT, ForeignKey('orders.id', ondelete='CASCADE'), nullable=False)
    product_id = Column(INT, ForeignKey('products.id', ondelete='CASCADE'), nullable=False)