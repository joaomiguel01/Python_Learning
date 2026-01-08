from beans import Flight, Seat, StatusSeat
from setup_db import FlightRepository, SeatRepository, get_connection
from string import ascii_uppercase

class SeatFactory:
    def __init__(self, flight_repo: FlightRepository, seat_repo: SeatRepository):
        self._flight_repo = flight_repo
        self._seat_repo = seat_repo

    
    def create_seats(self,
                     flight: Flight,
                     num_cols: int, 
                     num_rows: int):
        
        if num_cols < 1 or num_cols > 26:
            raise ValueError("ERROR: num_cols must be between 1 and 26")
        
        if num_rows < 1:
            raise ValueError("ERROR: num_rows must be >= 1")
        

        if self._flight_repo.exists(flight.code):
            raise ValueError("Flight already exists")
        

        letters = ascii_uppercase[:num_cols]
        seats = []

        for char in letters:
            for num in range(1, num_rows+1):
                seats.append(Seat(f"{char}{num}", StatusSeat.FREE))
        

        # Transação
        with get_connection() as conn:
            self._flight_repo.save(flight, conn)
            self._seat_repo.add_many(flight.code, seats, conn)

