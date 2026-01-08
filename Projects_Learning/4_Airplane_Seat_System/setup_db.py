from beans import Flight, Seat, StatusSeat
from contextlib import contextmanager
import sqlite3

@contextmanager
def get_connection(db_path="flights.db"):
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row # Acesso de dados em formato de dicionários
    conn.execute("PRAGMA foreign_keys = ON") # Ativa chaves estrangeiras
    try:
        yield conn # Entrega o objeto para quem usar "with get_connect() as conn"
        conn.commit() # Salva as mudanças
    except:
        conn.rollback() # Desfaz todas as operações em caso de erro
        raise
    finally:
        conn.close() # Fecha a conexão


def create_tables():
    with get_connection() as conn: # Abrindo uma conexão
        # Criação das tabelas
        conn.execute("""
        CREATE TABLE IF NOT EXISTS flight (
            code TEXT PRIMARY KEY,
            description TEXT NOT NULL,
            plane TEXT NOT NULL
        )
        """)

        conn.execute("""
        CREATE TABLE IF NOT EXISTS seat(
            code TEXT,
            status TEXT NOT NULL,
            flight_code TEXT NOT NULL,
            PRIMARY KEY (code, flight_code),
            FOREIGN KEY (flight_code) 
                REFERENCES flight(code)
                ON DELETE CASCADE
        )
        """)




class FlightRepository:
    def save(self, flight: Flight, conn):
        # Salva o voo no banco de dados
        conn.execute("""
        INSERT INTO flight (code, description, plane)
        VALUES(?, ?, ?)
        """, (flight.code, flight.description, flight.plane))
    

    def exists(self, code: str) -> bool:
        with get_connection() as conn:
            cursor = conn.execute(
                "SELECT 1 FROM flight WHERE code = ?",
                (code,)
            )
            return cursor.fetchone() is not None


    def get_by_code(self, code: str) -> Flight | None:
        with get_connection() as conn:
            row = conn.execute(
                "SELECT * FROM flight WHERE code = ?",
                (code,)
            ).fetchone()
        
        if row is None:
            return None
        
        return Flight(
            row['code'],
            row['description'],
            row['plane']
        )
    

class SeatRepository:
    def add_many(self, flight_code: str, seats: list[Seat], conn):
        conn.executemany("""
            INSERT INTO seat (code, status, flight_code)
            VALUES (?, ?, ?)
        """, [(seat.code, seat.status.value, flight_code) 
                for seat in seats
                ])
            

    def list_by_flight(self, flight_code: str) -> list[Seat]:
        with get_connection() as conn:
            rows = conn.execute(
                "SELECT * FROM seat WHERE flight_code = ?",
                (flight_code,)
            ).fetchall()

        return [Seat(code=row['code'], status=StatusSeat(row['status'])) for row in rows]