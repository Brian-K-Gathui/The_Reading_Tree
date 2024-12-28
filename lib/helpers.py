# lib/helpers.py

import os
import sys
from sqlalchemy.orm import Session

# Ensure the lib directory is in the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
lib_dir = os.path.join(current_dir, "../")
sys.path.append(lib_dir)

# Import models
from lib.db.models import Base

def validate_input(prompt, expected_type, valid_range=None):
    """
    Validates user input, ensuring it matches the expected type and optional range.
    
    Args:
        prompt (str): The input prompt message.
        expected_type (type): The expected type of the input (e.g., int, float, str).
        valid_range (iterable, optional): A range or list of valid values.
    
    Returns:
        The validated input converted to the expected type.
    """
    while True:
        try:
            user_input = expected_type(input(prompt))
            if valid_range and user_input not in valid_range:
                raise ValueError
            return user_input
        except ValueError:
            valid_range_message = f" in {list(valid_range)}" if valid_range else ""
            print(f"Invalid input. Please enter a {expected_type.__name__}{valid_range_message}.")

def print_table(items, attributes):
    """
    Prints a formatted table of objects with specified attributes.
    
    Args:
        items (list): A list of objects to display.
        attributes (list): A list of attribute names to display from each object.
    """
    if not items:
        print("No records found.")
        return

    # Print headers
    headers = " | ".join(attributes)
    print(headers)
    print("-" * len(headers))
    
    # Print each item's attributes
    for item in items:
        row = " | ".join(str(getattr(item, attr, "N/A")) for attr in attributes)
        print(row)

def initialize_database(engine):
    """
    Ensures that the database schema is created before any operations.

    Args:
        engine: SQLAlchemy engine connected to the database.
    """
    Base.metadata.create_all(engine)

def reset_database(session: Session):
    """
    Drops all tables and recreates the schema. WARNING: This erases all data.

    Args:
        session: SQLAlchemy session connected to the database.
    """
    print("WARNING: This will reset the database and delete all data!")
    confirmation = input("Type 'RESET' to confirm: ")
    if confirmation == "RESET":
        Base.metadata.drop_all(bind=session.bind)
        Base.metadata.create_all(bind=session.bind)
        print("Database has been reset.")
    else:
        print("Reset cancelled.")

def validate_password(min_length=8):
    """
    Prompt the user for a password, validate its length, and return it.
    
    Args:
        min_length (int): The minimum required length of the password.

    Returns:
        str: The validated password string.
    """
    while True:
        password = input("Enter a password: ")
        if len(password) < min_length:
            print(f"Password must be at least {min_length} characters long.")
            continue
        return password
