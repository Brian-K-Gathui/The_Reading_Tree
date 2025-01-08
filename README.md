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
  - Well-structured relational database with at least six tables: Books, Authors, Publishers, Warehouses, and Customers.  
  - Leverages SQLAlchemy ORM for efficient data manipulation.  
  - Employs Alembic for database migrations, facilitating future database schema changes.

## Technologies Used

- Python
- SQLAlchemy ORM
- Alembic for database migrations
- Pipenv for virtual environment and dependency management

## Project Structure

```
THE_READING_TREE/            # Project root
├── .github/
│   └── workflows/
├── .venv/                   # Virtual environment (auto-created by Pipenv)
├── lib/                     # Core logic and database modules
│   ├── __init__.py          # Makes helper functions and models accessible
│   │   from .helpers import validate_input, print_table
│   │   from .db import models  # Makes all models accessible via lib.db.models
│   ├── db/
│   │   ├── __init__.py      # Imports base models
│   │   │   from .models import Base, Publisher, Author, Book, Warehouse, Customer
│   │   ├── models.py        # SQLAlchemy models
│   │   ├── seed.py          # Database seeding script
│   │   └── helpers.py       # Helper functions for CLI
│   └── cli.py               # Main CLI application
├── migrations/              # Alembic migration scripts
├── Pipfile                  # Pipenv dependency file
├── Pipfile.lock             # Locked dependencies
└── README.md                # Project documentation
```


## Project Setup, Intializations and Access
### 1. Clone the Repository
```bash
git clone <repository-url>
cd <repository-directory>
```

### 2. Set Up the Virtual Environment
Install dependencies using Pipenv:
```bash
pipenv install
```

Activate the virtual environment:
```bash
pipenv shell
```

### 3. Seed the Database
Run the database seeding script:
```bash
python -m lib.db.seed
```
This creates and seeds the `bookstore.db` file.

### 4. Run the Application
Start the CLI application:
```bash
python -m lib.cli
```

## Database Configuration and Migration Check

### Configure the Database
The `sqlalchemy.url` in the `alembic.ini` file is set as a placeholder. Update it to point to your actual database URL:
```ini
sqlalchemy.url = sqlite:///bookstore.db
```

### Generate and Apply Migrations
Follow these steps to set up the database schema using Alembic migrations:

1. **Generate the initial migration script:**  
   This step creates the migration script to define the database schema:
   ```bash
   alembic revision --autogenerate -m "Initial migration to create tables"
   ```

2. **Apply the migration:**  
   Run the migration to apply the schema to the database:
   ```bash
   alembic upgrade head
   ```

3. **Revert a migration (if necessary):**  
   To undo a migration, use the following command:
   ```bash
   alembic downgrade -1
   ```

Ensure the database configuration and migrations are correct if any errors might occur.


## Future Works

As we continue to enhance and expand the Bookstore Management System for **The Reading Tree**, several exciting features are planned for future development. These improvements aim to provide more functionality, increase efficiency, and deliver a better user experience. Below are the upcoming additions:

### Authentication and Role-Based Access
- **Login System for Managers and Staff**: Implement user authentication to ensure secure access. Managers and staff will have distinct roles, with functionality restricted based on their role.
- **Role-Based Access Control**: Managers will have full access to the system, while staff access will be limited to specific features, such as viewing inventory or logging transactions.

### Transaction Management
- **Enterprise Transactions**: Introduce a model to track enterprises that require bulk orders, ensuring efficient handling of large transactions.
- **Customer Transactions**: Record individual customer purchases to analyze trends and generate insights on buying behavior.

### Sales and Transactions Tracking
- **Sales Logging**: Track daily or weekly sales data for business analytics.
- **Best-Selling Titles**: Identify top-selling books and generate reports.
- **Sales Reports**: Print detailed sales reports to facilitate business analysis and decision-making.

### Membership and Loyalty Programs
- **Customer Accounts**: Allow customers to create accounts that store their purchase history.
- **Loyalty Points**: Implement a loyalty program that rewards frequent buyers with points or discounts, enhancing customer retention.

### Supplier Management
- **Supplier Data Monitoring**: Track supplier details and order statuses for efficient restocking of popular books.
- **Restocking Alerts**: Automate notifications for low-stock items, ensuring inventory is always prepared.

### Additional Notes
These future features will enhance the system's scalability and usability, aligning with **The Reading Tree**'s growth and operational needs. Each addition will be carefully designed to ensure seamless integration with the current architecture while maintaining high standards of performance and security.

I look forward to implementing these features in subsequent updates, making the system even more robust and user-friendly!

## License

MIT License  

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

---

Copyright © 2025 Brian Kinyanjui Gathui
