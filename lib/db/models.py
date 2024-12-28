# lib/db/models.py

from sqlalchemy import Column, String, Integer, Numeric, ForeignKey, Table
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

# Association table for Book <-> Author (many-to-many)
book_author = Table(
    'book_author',
    Base.metadata,
    Column('book_isbn', String, ForeignKey('book.isbn'), primary_key=True),
    Column('author_name', String, ForeignKey('author.name'), primary_key=True)
)

# Association table for Book <-> Warehouse (many-to-many)
warehouse_book = Table(
    'warehouse_book',
    Base.metadata,
    Column('warehouse_code', Integer, ForeignKey('warehouse.code'), primary_key=True),
    Column('book_isbn', String, ForeignKey('book.isbn'), primary_key=True),
    Column('count', Integer)
)

class Publisher(Base):
    __tablename__ = 'publisher'

    name = Column(String(255), primary_key=True)
    address = Column(String(255))
    phone = Column(String(255))
    url = Column(String(255))

    books = relationship('Book', back_populates='publisher')

class Book(Base):
    __tablename__ = 'book'

    isbn = Column(String(255), primary_key=True)
    publisher_name = Column(String(255), ForeignKey('publisher.name'))
    year = Column(Integer)
    title = Column(String(255))
    price = Column(Numeric(19, 2))

    publisher = relationship('Publisher', back_populates='books')
    authors = relationship('Author', secondary=book_author, back_populates='books')
    warehouses = relationship('Warehouse', secondary=warehouse_book, back_populates='books')

class Author(Base):
    __tablename__ = 'author'

    name = Column(String(255), primary_key=True)
    address = Column(String(255))
    url = Column(String(255))

    books = relationship('Book', secondary=book_author, back_populates='authors')

class Warehouse(Base):
    __tablename__ = 'warehouse'

    code = Column(Integer, primary_key=True)
    phone = Column(String(255))
    address = Column(String(255))

    books = relationship('Book', secondary=warehouse_book, back_populates='warehouses')

class Customer(Base):
    __tablename__ = 'customer'

    email = Column(String(255), primary_key=True)
    name = Column(String(255))
    phone = Column(String(255))
    address = Column(String(255))
