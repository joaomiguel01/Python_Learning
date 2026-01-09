import sqlite3
from contextlib import contextmanager
from utils_module_u import check_string
from datetime import date
from email_validator import validate_email, EmailNotValidError
from utils_module_u import title


# Classes
class Customer:
    def __init__(self, id: str, name: str, email: str, birth_year: int, total_debt: float = 0.0):
        self.id = id
        self.name = name
        self.email = email
        self.birth_year = birth_year
        self.total_debt = total_debt


    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, id: str):
        if check_string(id):
            if len(id) == 3:
                self._id = id.strip().upper()
            else:
                raise ValueError("ERROR: The ID must be 3 characters!")
        else:
            raise ValueError("ERROR: The ID can't be a blank string!")
    

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name: str):
        if check_string(name):
            self._name = name.strip()
        else:
            raise ValueError("ERROR: The name can't be a blank string")
    

    @property
    def email(self):
        return self._email
    @email.setter
    def email(self, email: str):
        try:
            v = validate_email(email)
            self._email = v.email
        except EmailNotValidError:
            raise ValueError("ERROR: The email is invalid!")
        
    
    @property
    def birth_year(self):
        return self._birth_year
    @birth_year.setter
    def birth_year(self, birth_year: int):
        if isinstance(birth_year, int) and 1900 <= birth_year <= date.today().year:
            self._birth_year = birth_year
        else:
            raise ValueError("ERROR: The birth_year must be between 1900 and current year!")
    

    @property
    def total_debt(self):
        return self._total_debt
    @total_debt.setter
    def total_debt(self, total_debt: float):
        if isinstance(total_debt, (int, float)) and total_debt >= 0:
            self._total_debt = float(total_debt)
        else:
            raise ValueError("ERROR: The total_debt must be greater than or equal to 0!")


    def calculate_age(self) -> int:
        return date.today().year - self.birth_year
    



    def __repr__(self):
        return f"{self.id:^3} | {self.name.upper():<30} | {str(self.calculate_age()):<5} | {self.email:<30} | {self.total_debt:<8.2f}"
    def __str__(self):
        return f"{self.id:^3} | {self.name.upper():<30} | {str(self.calculate_age()):<5} | {self.email:<30} | {self.total_debt:<8.2f}"
    



# Utils Functions
@contextmanager
def get_connection(data_path="customers.db"):
    conn = sqlite3.connect(data_path)
    conn.row_factory = sqlite3.Row # access by column name
    conn.execute("PRAGMA foreign_keys = ON") # Active foreign keys

    try:
        yield conn # delivers the connection to the 'with' block.
        conn.commit() # Save modifications
    except Exception:
        conn.rollback() # Undo everything in case of error.
        raise
    finally:
        conn.close() # Close connection


def create_tables():
    with get_connection() as conn:
        conn.execute(f"""
        CREATE TABLE IF NOT EXISTS customer(
            id TEXT NOT NULL PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT UNIQUE COLLATE NOCASE,
            birth_year INTEGER CHECK (birth_year BETWEEN 1900 AND {date.today().year}), 
            total_debt REAL DEFAULT 0 CHECK (total_debt >= 0)
        )
        """)


# DB functions
def print_data():
    customers = list_customers()

    title("LISTA DE CLIENTES CADASTRADOS")
    print(f"{'ID':^3} | {'NOME':<30} | {'IDADE':5} | {'E-MAIL':<30} | {'DÍVIDA(R$)':^10}")
    print("-"*90)
    for c in customers:
        print(c)


def add_customer(customer: Customer):
    with get_connection() as conn:
        conn.execute("""
            INSERT INTO customer (id, name, email, birth_year, total_debt)
            VALUES (?, ?, ?, ?, ?)
        """, (customer.id, 
              customer.name, 
              customer.email, 
              customer.birth_year, 
              customer.total_debt
              ))


def search_customer(customer_id: str) -> Customer:
    if not check_string(customer_id):
        raise ValueError("ERROR: Invalid customer ID!")
    

    customer_id = customer_id.strip()

    with get_connection() as conn:
        row = conn.execute("""
            SELECT * FROM customer
            WHERE id = ?
        """, (customer_id,)).fetchone()
    
    if row is None:
        raise ValueError("Customer not found!")
    

    return Customer(
        row['id'],
        row['name'],
        row['email'],
        row['birth_year'],
        row['total_debt']
    )


def list_customers():
    with get_connection() as conn:
        rows = conn.execute("""
            SELECT * FROM customer ORDER BY name
        """).fetchall()
    
    return [Customer(row['id'], 
                     row['name'], 
                     row['email'], 
                     row['birth_year'], 
                     row['total_debt']) for row in rows]


def delete_customer(customer_id: str):
    if not check_string(customer_id):
        raise ValueError("ERROR: Invalid customer ID!")
    
    with get_connection() as conn:
        cursor = conn.execute("""
            DELETE FROM customer
            WHERE id = ?
        """, (customer_id.strip(),))

    if cursor.rowcount == 0:
        raise ValueError("Customer not found!")


def update_customer(customer: Customer):
    with get_connection() as conn:
        cursor = conn.execute("""
            UPDATE customer
            SET name = ?,
                email = ?,
                birth_year = ?,
                total_debt = ?
            WHERE id = ?
        """, (
            customer.name,
            customer.email,
            customer.birth_year,
            customer.total_debt,
            customer.id
        ))


        if cursor.rowcount == 0:
            raise ValueError("Customer not found")