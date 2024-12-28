# Phase 3 Final Project – The Reading Tree Bookstore Management System

**Author:** Brian Kinyanjui Gathui  
**Email:** briankgathui@gmail.com

## Project Description
The Reading Tree Bookstore Management System is a Command-Line Interface (CLI) application developed for "The Reading Tree," a small bookstore in Nairobi. This Python-based application utilizes SQLAlchemy for Object-Relational Mapping (ORM) and Alembic for database migrations, streamlining the management of book inventory, authors, and sales transactions. This project aims to enhance operational efficiency for "The Reading Tree" by providing a robust and user-friendly system for managing core business aspects.

## User Stories for the MVP

1. **Inventory Management**  
   As a store manager, I want to add new books (with details like title, author, genre, and price) so that the store’s inventory is always up-to-date and accurate.

2. **Book Search**  
   As a staff member, I want to search and view all books by author or genre so that I can quickly recommend titles to customers.

3. **Inventory Update**  
   As a manager, I want to delete or edit the details of a book (e.g., when the price changes or a book is out of stock) so that the store’s records reflect real-time availability and pricing.

## Key Features

- **Comprehensive Entity Management**:  
  - Manage publishers: Add, view, update, delete, and search publishers by name.  
  - Manage authors: Add, view, update, delete, and search authors by name.  
  - Manage books: Add, view, update, delete, and search books by ISBN.  
  - Manage warehouses: Add, view, update, delete, and search warehouses by code.  
  - Manage customers: Add, view, update, delete, and search customers by email.

- **User-Friendly CLI**:  
  - Intuitive and user-friendly CLI with clear prompts, input validation, and error handling for seamless data entry and retrieval.  
  - Utilizes color and ASCII art to enhance the user experience (optional based on preference).

- **Robust Database Management**:  
  - Well-structured relational database with at least six tables: Books, Authors, Publishers, Warehouses, Customers, and Transactions (depending on implementation).  
  - Leverages SQLAlchemy ORM for efficient data manipulation.  
  - Employs Alembic for database migrations, facilitating future database schema changes.

## Technologies Used

- Python
- SQLAlchemy ORM
- Alembic for database migrations
- Pipenv for virtual environment and dependency management

## Project Structure

```
.
├── Pipfile
├── Pipfile.lock
├── README.md
└── lib
    ├── cli.py                # CLI main script
    ├── db
    │   ├── models.py         # SQLAlchemy models for Books, Authors, Transactions
    │   ├── seed.py           # Database seeding script
    │   ├── migrations        # Alembic migration files
    ├── helpers.py            # Helper functions for CLI logic
    ├── debug.py              # Debugging utilities
```


## How to Use and Access The Reading Tree Bookstore Management System

### Setup Instructions
#### Clone the Repository

```bash
git clone <repository-url>
cd <repository-directory>
```

#### Set Up Environment

Install dependencies and activate the virtual environment using Pipenv. Run these commands in the root directory:

```bash
pipenv install
pipenv shell
```

#### Database Initialization

Run the following commands in the root directory to initialize and seed the database:

```bash
python -m lib.db.seed
```

This creates and seeds a `bookstore.db` file in the root directory. You will see a confirmation message upon completion.

#### Run The Application

Start the CLI application by running the following command in the root directory:

```bash
python -m lib.cli
```


## License

MIT License  
Copyright © 2025 Brian Kinyanjui Gathui

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
