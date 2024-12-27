# CLI Application for Data Management of a Book Store

## Project Description
This project is a Python-based Command-Line Interface (CLI) application for managing a dataset. It is built with SQLAlchemy for database management and provides a user-friendly interface to perform CRUD operations. The application is modular, scalable, and follows best practices in software design.

## Features
- **Interactive CLI:** Navigate through menus to perform actions.
- **Database Integration:** Uses SQLAlchemy ORM for efficient data management.
- **CRUD Operations:** Create, read, update, and delete records seamlessly.
- **Data Seeding:** Populate the database with initial data for testing or usage.

---

## Installation

### Prerequisites
1. Python 3.8+
2. Pipenv installed globally (`pip install pipenv`)

### Steps
1. Clone the repository:
    ```bash
    git clone <repository-url>
    cd <project-directory>
    ```

2. Install dependencies and activate the virtual environment:
    ```bash
    pipenv install
    pipenv shell
    ```

3. Set up the database:
    ```bash
    alembic upgrade head
    python lib/db/seed.py
    ```

4. Run the CLI application:
    ```bash
    python lib/cli.py
    ```

---

## Usage
The CLI application provides a menu-driven interface. Follow the prompts to interact with the system.

### Example Commands
- **View All Records**:
    ```
    Select option: 1
    ```
- **Add a New Record**:
    ```
    Select option: 2
    Enter details...
    ```
- **Update a Record**:
    ```
    Select option: 3
    Enter record ID and new details...
    ```
- **Delete a Record**:
    ```
    Select option: 4
    Enter record ID...
    ```

---

## File Structure

### `lib/cli.py`
Contains the main logic for the CLI. Users interact with this script to perform operations. It includes menu definitions and the flow of user inputs to various helper functions.

### `lib/helpers.py`
Defines helper functions used by the CLI for tasks like input validation, formatting, and database operations.

### `lib/db/models.py`
Defines the database schema using SQLAlchemy ORM. Models include attributes and relationships.

### `lib/db/seed.py`
Populates the database with initial data for testing or as a starting point for usage.

---

## Contribution Guidelines
- Fork the repository and create a new branch for your feature or bug fix.
- Follow the coding style and conventions used in the project.
- Submit a pull request with a clear description of changes.

---

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.
