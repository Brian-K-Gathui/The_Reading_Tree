from faker import Faker
from sqlalchemy import create_engine, insert
from sqlalchemy.orm import sessionmaker
import random

from colorama import Fore, Style, init
init(autoreset=True)

from .models import Base, Publisher, Author, Book, Warehouse, Customer, book_author, warehouse_book

faker = Faker()
engine = create_engine('sqlite:///bookstore.db')

Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

used_isbns = set()
used_emails = set()

def unique_isbn():
    while True:
        isbn = faker.isbn13()
        if isbn not in used_isbns:
            used_isbns.add(isbn)
            return isbn

def unique_email():
    while True:
        email = faker.email()
        if email not in used_emails:
            used_emails.add(email)
            return email

def generate_kenyan_address():
    cities = ["Nairobi", "Mombasa", "Kisumu", "Nakuru", "Eldoret", "Thika", "Nyeri", "Meru"]
    streets = [
        "Moi Avenue", "Kenyatta Avenue", "Haile Selassie Avenue", "Kimathi Street", 
        "Tom Mboya Street", "Mama Ngina Street", "Uhuru Highway", "Ronald Ngala Street", 
        "Argwings Kodhek Road", "Dennis Pritt Road", "Langata Road", "Ngong Road",
        "Kenyatta Highway", "Nyerere Road"
    ]
    return f"{faker.building_number()} {random.choice(streets)}, {random.choice(cities)}"

# Seed Publishers
publishers = [
    Publisher(
        name=faker.company(),
        address=generate_kenyan_address(),
        phone=f"+254{random.randint(700000000, 799999999)}",
        url=faker.url()
    )
    for _ in range(10)
]
session.add_all(publishers)
session.commit()

# Seed Authors
authors = [
    Author(
        name=faker.name(),
        address=generate_kenyan_address(),
        url=faker.url()
    )
    for _ in range(20)
]
session.add_all(authors)
session.commit()

# Seed Books
books = []
for _ in range(50):
    books.append(
        Book(
            isbn=unique_isbn(),
            publisher_name=random.choice(publishers).name,
            year=random.randint(1990, 2023),
            title=faker.sentence(nb_words=5),
            price=round(random.uniform(10, 500), 2)
        )
    )
session.add_all(books)
session.commit()

# Assign Authors to Books
for book in books:
    selected_authors = random.sample(authors, random.randint(1, 3))
    for author in selected_authors:
        stmt = insert(book_author).values(
            book_isbn=book.isbn,
            author_name=author.name
        )
        session.execute(stmt)

# Seed Warehouses
warehouses = [
    Warehouse(
        code=i,
        phone=f"+254{random.randint(700000000, 799999999)}",
        address=generate_kenyan_address()
    )
    for i in range(1, 6)
]
session.add_all(warehouses)
session.commit()

# Assign Books to Warehouses
for warehouse in warehouses:
    selected_books = random.sample(books, random.randint(5, 15))
    for book in selected_books:
        stmt = insert(warehouse_book).values(
            warehouse_code=warehouse.code,
            book_isbn=book.isbn,
            count=random.randint(1, 50)
        )
        session.execute(stmt)

# Seed Customers
customers = [
    Customer(
        email=unique_email(),
        name=faker.name(),
        phone=f"+254{random.randint(700000000, 799999999)}",
        address=generate_kenyan_address()
    )
    for _ in range(100)
]
session.add_all(customers)
session.commit()

print("\n")
print(Fore.GREEN + Style.BRIGHT + "Database seeded successfully! The Reading Tree Bookstore Management System is now ready to use :) ")
print(Fore.GREEN + Style.BRIGHT + """
                       (
                          )     (
                   ___...(-------)-....___
               .-""       )    (          ""-.
         .-'``'|-._             )         _.-|
        /  .--.|   `""---...........---""`   |
       /  /    |                             |
       |  |    |                             |
        \  \   |                             |
         `\ `\ |                             |
           `\ `|                             |
           _/ /\                             /
          (__/  \                           /
       _..---""` \                         /`""---.._
    .-'           \                       /          '-.
   :               `-.__             __.-'              :
   :                  ) ""---...---"" (                 :
    '._               `"--...___...--"`              _.'
      \  --..__                              __..--  /
       '._        ----.....______.....----        _.'
""")
print("\n")
