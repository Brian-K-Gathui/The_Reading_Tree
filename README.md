Bookstore Management System

Project Description

"My Phase 3 project is a Bookstore Management System tailored for a small bookstore in Nairobi, The Reading Tree. The CLI-based application will streamline store operations by providing features for managing book inventory, authors, and sales transactions. Built with Python and SQLAlchemy, the system will include a well-structured database with at least three related tables: Books, Authors, and Transactions (or Categories, if implemented).

The CLI will offer an intuitive user experience, complete with input validation, organized menus, and seamless data retrieval, ensuring efficient management of store operations."

Overview

The Bookstore Management System is a Command-Line Interface (CLI) application designed for a small bookstore in Nairobi, The Reading Tree. This Python-based application leverages SQLAlchemy ORM and Alembic to manage a relational database for the bookstore's inventory and sales. The system allows users to manage book inventory, authors, and transactions efficiently.

The application is organized following best practices for CLI design, Object-Oriented Programming (OOP), and Python project structure. It includes clear user prompts, error handling, and input validation for an intuitive user experience.

User Stories for the Minimum Viable Product (MVP)

1. Inventory Management

As a store manager, I want to add new books (with details like title, author, genre, and price) so that the store’s inventory is always up-to-date and accurate.

2. Book Search

As a staff member, I want to search and view all books by author or genre so that I can quickly recommend titles to customers.

3. Inventory Update

As a manager, I want to delete or edit the details of a book (e.g., when the price changes or a book is out of stock) so that the store’s records reflect real-time availability and pricing.

Features

Core Features

Inventory Management

Add new books with details such as title, author, genre, and price.

Search and view books by author or genre.

Edit or delete book details to ensure accurate and up-to-date records.

Database Management

SQLAlchemy ORM for managing the database schema.

Alembic for handling migrations and maintaining database history.

Stretch Goals

1. Sales/Transactions Tracking

Enable daily or weekly sales logging, tracking of best-selling titles, and generation of sales reports for business analysis.

2. Membership & Loyalty Program

Implement customer accounts with loyalty points or discounts for frequent buyers.

3. Supplier Management

Add functionality to monitor supplier data and order statuses, aiding in the restocking of popular books.

4. Dark Mode

Include a CLI "dark mode" styling option to reduce eye strain for staff working in dim lighting conditions.

Directory Structure

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

Setup Instructions

Clone the Repository

git clone <repository-url>
cd <repository-directory>

Set Up Environment

Install dependencies and activate the virtual environment using Pipenv:

pipenv install
pipenv shell

Database Initialization

Set up and migrate the database:

cd lib/db
alembic init migrations
alembic revision --autogenerate -m "Initial migration"
alembic upgrade head

Run the Application

python lib/cli.py

Key Components

CLI (lib/cli.py)

The entry point for the application. Handles user interaction via menus and prompts. Includes:

main(): The main loop for user interaction.

menu(): Displays options and routes user choices.

Database Models (lib/db/models.py)

Defines the database schema:

Books: Represents inventory items with attributes for title, author, genre, price, and availability.

Authors: Tracks author details, supporting a one-to-many relationship with Books.

Transactions: Logs sales or other bookstore transactions.

Helper Functions (lib/helpers.py)

Reusable functions for:

Input validation.

Displaying formatted data to the user.

Exiting the application gracefully.

Seed Script (lib/db/seed.py)

Populates the database with initial data for testing.

Dependencies

SQLAlchemy: ORM for database interactions.

Alembic: Handles migrations.

Pipenv: Manages the Python environment and dependencies.

Usage Guide

Inventory Management

Add a new book:

Enter the title, author, genre, and price as prompted.

Search books by author:

Input the author’s name to view related books.

Edit book details:

Choose a book ID and specify the new details.

Learning Goals

This project demonstrates the following:

Use of SQLAlchemy ORM and Alembic for database management.

Best practices in CLI design, including input validation and user feedback.

Use of Python data structures (lists, tuples, dictionaries) for data handling.

Modular and maintainable Python codebase.

Future Enhancements

Dark mode for the CLI.

Integration of a loyalty program.

Automated supplier management and notifications.

