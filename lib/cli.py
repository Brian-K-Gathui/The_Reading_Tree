# lib/cli.py

import sys
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from colorama import Fore, Style, init

init(autoreset=True)

# Add the project root to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.join(current_dir, "../..")
sys.path.append(project_root)

from lib.db.models import Base, Publisher, Author, Book, Warehouse, Customer
from lib.helpers import validate_input, print_table, validate_password

# Database Setup
engine = create_engine('sqlite:///bookstore.db')
Base.metadata.bind = engine
Session = sessionmaker(bind=engine)
session = Session()

def main_menu():
    # Clear the terminal screen
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n")
    print(Fore.GREEN + Style.BRIGHT + """
  _______ _            _____                _ _               _______              __  __  _____ 
 |__   __| |          |  __ \              | (_)             |__   __|            |  \/  |/ ____|         
    | |  | |__   ___  | |__) |___  __ _  __| |_ _ __   __ _     | |_ __ ___  ___  | \  / | (___  
    | |  | '_ \ / _ \ |  _  // _ \/ _` |/ _` | | '_ \ / _` |    | | '__/ _ \/ _ \ | |\/| |\___ \ 
    | |  | | | |  __/ | | \ \  __/ (_| | (_| | | | | | (_| |    | | | |  __/  __/ | |  | |____) |     
    |_|  |_| |_|\___| |_|  \_\___|\__,_|\__,_|_|_| |_|\__, |    |_|_|  \___|\___| |_|  |_|_____/ 
                                                       __/ |                                     
                                                      |___/                                      
    _____
   /    /|_ ___________________________________________
  /    // /|                                          /|
 (====|/ //   Nourish Your Mind,           _QP_      / |
  (=====|/     One Book at a Time         (  ' )    / .|
 (====|/                                   \__/    / /||
/_________________________________________________/ / ||
|  _____________________________________________  ||  ||
| ||                                            | ||
| ||                                            | ||
| |                                             | |   

    """)
    
    print(Fore.GREEN + Style.BRIGHT + "Welcome to The Reading Tree Bookstore Management System")
    print("\n")
    print(Fore.GREEN + Style.BRIGHT + "1. Manage Publishers")
    print(Fore.GREEN + Style.BRIGHT + "2. Manage Authors")
    print(Fore.GREEN + Style.BRIGHT + "3. Manage Books")
    print(Fore.GREEN + Style.BRIGHT + "4. Manage Warehouses")
    print(Fore.GREEN + Style.BRIGHT + "5. Manage Customers")
    print(Fore.GREEN + Style.BRIGHT + "6. Exit")
    print("\n")

    choice = validate_input(Fore.WHITE + Style.BRIGHT +"Enter your choice (1-6): ", int, range(1, 7))
    if choice == 1:
        manage_publishers()
    elif choice == 2:
        manage_authors()
    elif choice == 3:
        manage_books()
    elif choice == 4:
        manage_warehouses()
    elif choice == 5:
        manage_customers()
    elif choice == 6:
        # Clear the terminal screen
        os.system('cls' if os.name == 'nt' else 'clear')
        
        # Goodbye message with new ASCII art
        print(Fore.GREEN + Style.BRIGHT + """
   _____                 _ _                      __  
  / ____|               | | |                  _  \ \ 
 | |  __  ___   ___   __| | |__  _   _  ___   (_)  | |
 | | |_ |/ _ \ / _ \ / _` | '_ \| | | |/ _ \       | |
 | |__| | (_) | (_) | (_| | |_) | |_| |  __/   _   | |
  \_____|\___/ \___/ \__,_|_.__/ \__, |\___|  (_)  | |
                                  __/ |           /_/ 
                                 |___/                """)
        print(Fore.GREEN + Style.BRIGHT + """

              oxoxoo    ooxoo
            ooxoxo oo  oxoxooo
            oooo xxoxoo ooo ooox
            oxo o oxoxo  xoxxoxo
            oxo xooxoooo o ooo
                ooo\oo\  /o/o
                    \  \/ /
                    |   /
                    |  |
                    | D|
                    |  |
                    |  |
            ______/____\_____
            
Thank you for using The Reading Tree Bookstore Management System!!!
        """)
        sys.exit()

def manage_publishers():
    while True:
        print(Fore.CYAN + Style.BRIGHT + """
Publisher Management
1. Add Publisher
2. View All Publishers
3. Update Publisher
4. Delete Publisher
5. Find Publisher by Name
6. Go Back
        """)
        choice = validate_input("Enter your choice (1-6): ", int, range(1, 7))
        if choice == 1:
            name = input("Publisher Name: ")
            address = input("Address: ")
            phone = input("Phone: ")
            url = input("URL: ")
            session.add(Publisher(name=name, address=address, phone=phone, url=url))
            session.commit()
            print("Publisher added successfully!")
        elif choice == 2:
            publishers = session.query(Publisher).all()
            print_table(publishers, ["name", "address", "phone", "url"])
        elif choice == 3:
            name = input("Enter the name of the Publisher to update: ")
            publisher = session.query(Publisher).filter_by(name=name).first()
            if publisher:
                publisher.address = input("New Address: ") or publisher.address
                publisher.phone = input("New Phone: ") or publisher.phone
                publisher.url = input("New URL: ") or publisher.url
                session.commit()
                print("Publisher updated successfully!")
            else:
                print("Publisher not found!")
        elif choice == 4:
            name = input("Enter the name of the Publisher to delete: ")
            publisher = session.query(Publisher).filter_by(name=name).first()
            if publisher:
                session.delete(publisher)
                session.commit()
                print("Publisher deleted successfully!")
            else:
                print("Publisher not found!")
        elif choice == 5:
            name = input("Enter the name of the Publisher to search: ")
            publisher = session.query(Publisher).filter_by(name=name).first()
            if publisher:
                print_table([publisher], ["name", "address", "phone", "url"])
            else:
                print("Publisher not found!")
        elif choice == 6:
            os.system('cls' if os.name == 'nt' else 'clear')
            main_menu()
            return

def manage_authors():
    while True:
        print( Fore.MAGENTA + """
Author Management
1. Add Author
2. View All Authors
3. Update Author
4. Delete Author
5. Find Author by Name
6. Go Back
        """)
        choice = validate_input("Enter your choice (1-6): ", int, range(1, 7))
        if choice == 1:
            name = input("Author Name: ")
            address = input("Address: ")
            url = input("URL: ")
            session.add(Author(name=name, address=address, url=url))
            session.commit()
            print("Author added successfully!")
        elif choice == 2:
            authors = session.query(Author).all()
            print_table(authors, ["name", "address", "url"])
        elif choice == 3:
            name = input("Enter the name of the Author to update: ")
            author = session.query(Author).filter_by(name=name).first()
            if author:
                author.address = input("New Address: ") or author.address
                author.url = input("New URL: ") or author.url
                session.commit()
                print("Author updated successfully!")
            else:
                print("Author not found!")
        elif choice == 4:
            name = input("Enter the name of the Author to delete: ")
            author = session.query(Author).filter_by(name=name).first()
            if author:
                session.delete(author)
                session.commit()
                print("Author deleted successfully!")
            else:
                print("Author not found!")
        elif choice == 5:
            name = input("Enter the name of the Author to search: ")
            author = session.query(Author).filter_by(name=name).first()
            if author:
                print_table([author], ["name", "address", "url"])
            else:
                print("Author not found!")
        elif choice == 6:
            os.system('cls' if os.name == 'nt' else 'clear')
            main_menu()
            return

def manage_books():
    while True:
        print(Fore.YELLOW + """
Book Management
1. Add Book
2. View All Books
3. Update Book
4. Delete Book
5. Find Book by ISBN
6. Go Back
        """)
        choice = validate_input("Enter your choice (1-6): ", int, range(1, 7))
        if choice == 1:
            isbn = input("ISBN: ")
            title = input("Title: ")
            price = validate_input("Price: ", float)
            publisher_name = input("Publisher Name: ")
            author_name = input("Author Name: ")
            author_address = input("Author Address: ")
            year = validate_input("Publication Year: ", int)
            book = Book(isbn=isbn, title=title, price=price,
                        publisher_name=publisher_name,
                        year=year)
            # We do not store author_name and author_address on the Book table directly.
            # They belong to Author. This is just an example. A more correct approach:
            #  - check if Author exists; if not, create.
            #  - add the author to the many-to-many relationship.
            session.add(book)
            session.commit()
            print("Book added successfully!")
        elif choice == 2:
            books = session.query(Book).all()
            print_table(books, ["isbn", "title", "price", "publisher_name", "year"])
        elif choice == 3:
            isbn = input("Enter the ISBN of the Book to update: ")
            book = session.query(Book).filter_by(isbn=isbn).first()
            if book:
                book.title = input("New Title: ") or book.title
                new_price = input("New Price: ")
                if new_price.strip():
                    book.price = float(new_price)
                new_year = input("New Publication Year: ")
                if new_year.strip():
                    book.year = int(new_year)
                session.commit()
                print("Book updated successfully!")
            else:
                print("Book not found!")
        elif choice == 4:
            isbn = input("Enter the ISBN of the Book to delete: ")
            book = session.query(Book).filter_by(isbn=isbn).first()
            if book:
                session.delete(book)
                session.commit()
                print("Book deleted successfully!")
            else:
                print("Book not found!")
        elif choice == 5:
            isbn = input("Enter the ISBN of the Book to search: ")
            book = session.query(Book).filter_by(isbn=isbn).first()
            if book:
                print_table([book], ["isbn", "title", "price", "publisher_name", "year"])
            else:
                print("Book not found!")
        elif choice == 6:
            os.system('cls' if os.name == 'nt' else 'clear')
            main_menu()
            return

def manage_warehouses():
    while True:
        print(Fore.BLUE + """
Warehouse Management
1. Add Warehouse
2. View All Warehouses
3. Update Warehouse
4. Delete Warehouse
5. Find Warehouse by Code
6. Go Back
        """)
        choice = validate_input("Enter your choice (1-6): ", int, range(1, 7))
        if choice == 1:
            code = validate_input("Warehouse Code: ", int)
            phone = input("Phone: ")
            address = input("Address: ")
            warehouse = Warehouse(code=code, phone=phone, address=address)
            session.add(warehouse)
            session.commit()
            print("Warehouse added successfully!")
        elif choice == 2:
            warehouses = session.query(Warehouse).all()
            print_table(warehouses, ["code", "phone", "address"])
        elif choice == 3:
            code = validate_input("Enter the Warehouse Code to update: ", int)
            warehouse = session.query(Warehouse).filter_by(code=code).first()
            if warehouse:
                warehouse.phone = input("New Phone: ") or warehouse.phone
                warehouse.address = input("New Address: ") or warehouse.address
                session.commit()
                print("Warehouse updated successfully!")
            else:
                print("Warehouse not found!")
        elif choice == 4:
            code = validate_input("Enter the Warehouse Code to delete: ", int)
            warehouse = session.query(Warehouse).filter_by(code=code).first()
            if warehouse:
                session.delete(warehouse)
                session.commit()
                print("Warehouse deleted successfully!")
            else:
                print("Warehouse not found!")
        elif choice == 5:
            code = validate_input("Enter the Warehouse Code to search: ", int)
            warehouse = session.query(Warehouse).filter_by(code=code).first()
            if warehouse:
                print_table([warehouse], ["code", "phone", "address"])
            else:
                print("Warehouse not found!")
        elif choice == 6:
            main_menu()
            return

def manage_customers():
    while True:
        print(Fore.RED + """
Customer Management
1. Add Customer
2. View All Customers
3. Update Customer
4. Delete Customer
5. Find Customer by Email
6. Go Back
        """)
        choice = validate_input("Enter your choice (1-6): ", int, range(1, 7))
        if choice == 1:
            email = input("Email: ")
            name = input("Name: ")
            phone = input("Phone: ")
            address = input("Address: ")
            session.add(Customer(email=email, name=name, phone=phone, address=address))
            session.commit()
            print("Customer added successfully!")
        elif choice == 2:
            customers = session.query(Customer).all()
            print_table(customers, ["email", "name", "phone", "address"])
        elif choice == 3:
            email = input("Enter Email to Update: ")
            customer = session.query(Customer).filter_by(email=email).first()
            if customer:
                customer.name = input("Name (leave blank to keep current): ") or customer.name
                customer.phone = input("Phone (leave blank to keep current): ") or customer.phone
                customer.address = input("Address (leave blank to keep current): ") or customer.address
                session.commit()
                print("Customer updated successfully!")
            else:
                print("Customer not found!")
        elif choice == 4:
            email = input("Enter Email to Delete: ")
            customer = session.query(Customer).filter_by(email=email).first()
            if customer:
                session.delete(customer)
                session.commit()
                print("Customer deleted successfully!")
            else:
                print("Customer not found!")
        elif choice == 5:
            email = input("Enter Email to Search: ")
            customer = session.query(Customer).filter_by(email=email).first()
            if customer:
                print_table([customer], ["email", "name", "phone", "address"])
            else:
                print("Customer not found!")
        elif choice == 6:
            os.system('cls' if os.name == 'nt' else 'clear')
            main_menu()
            return

if __name__ == "__main__":
    main_menu()
