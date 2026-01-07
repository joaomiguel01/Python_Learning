from database import get_connection
from beans import Flight, Seat, StatusSeat

def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS flight (
        code TEXT PRIMARY KEY,
        description TEXT NOT NULL,
        plane TEXT NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS seat(
        code TEXT,
        status TEXT NOT NULL,
        flight_code TEXT NOT NULL,
        PRIMARY KEY (code, flight_code),
        FOREIGN KEY (flight_code) REFERENCES flight(code)           
    )
    """)

    conn.commit()
    conn.close()


class FlightRepository:
    def save(self, flight: Flight):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO flight (code, description, plane)
        VALUES(?, ?, ?)
        """, (flight.code, flight.description, flight.plane))

        conn.commit()
        conn.close()
    

    def get_by_code(self, code: str) -> Flight | None:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM flight WHERE code = ?", (code,)
        )

        row = cursor.fetchone()
        conn.close()

        if row is None:
            return None
        
        return Flight(
            row['code'],
            row['description'],
            row['plane']
        )
    

class SeatReposiotory:
    def add_seat(self, flight_code: str, seat: Seat):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO seat (code, status, flight_code)
        VALUES (?, ?, ?)
        """, (seat.code, seat.status.value, flight_code))


        conn.commit()
        conn.close()
    

    def list_by_flight(self, flight_code: str) -> list[Seat]:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM seat WHERE flight_code = ?", (flight_code,)
        )

        seats = []

        for row in cursor.fetchall():
            seats.append(Seat(code=row['code'], status=StatusSeat(row['status'])))
        
        conn.close()
        return seats