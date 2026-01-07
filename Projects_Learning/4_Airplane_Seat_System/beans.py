from enum import Enum

class StatusSeat(Enum):
    FREE = "FREE"
    BUSY = "BUSY"


class Seat:
    def __init__(self, code: str, status: StatusSeat):
        self.code = code
        self.status = status


    @property
    def code(self):
        return self._code
    @code.setter
    def code(self, code: str):
        if isinstance(code, str) and code.strip():
            code = code.strip().upper()

            if len(code) == 2 and code[0].isalpha() and code[1].isdigit():
                self._code = code
            else:
                raise ValueError("ERROR: The seat code must be 2 characters, 1 letter and 1 number!")
        else:
            raise ValueError("ERROR: The code can't be a blank string!")   


    @property
    def status(self):
        return self._status
    @status.setter
    def status(self, status: StatusSeat):
        if isinstance(status, StatusSeat):
            self._status = status
        else:
            raise ValueError("ERROR: The status must be StatusSeat data!")
    

    def occupy(self):
        if self.status == StatusSeat.FREE:
            self.status = StatusSeat.BUSY
        else:
            raise ValueError("Seat already occupied")
    

    def free(self):
        if self.status == StatusSeat.FREE:
            return
        
        self.status = StatusSeat.FREE


class Flight:
    def __init__(self, code: str, description: str, plane: str):
        self.code = code
        self.description = description
        self.plane = plane
        self._seats: dict[str, Seat] = {}


    @property
    def code(self):
        return self._code
    @code.setter
    def code(self, code: str):
        if isinstance(code, str) and code.strip():
            code = code.strip().upper()
            if len(code) == 3 and code[0] == "#" and code[1].isalpha() and code[2].isdigit():
                self._code = code
            else:
                raise ValueError("ERROR: The flight code must be 3 characters with type '#A1' (hash, letter, digit)!")
        else:
            raise ValueError("ERROR: The flight code can't be a blank string!")
    

    @property
    def description(self):
        return self._description
    @description.setter
    def description(self, description: str):
        if isinstance(description, str) and description.strip():
            self._description = description.strip()
        else:
            raise ValueError("ERROR: The flight description can't be a blank string!")
    

    @property
    def plane(self):
        return self._plane
    @plane.setter
    def plane(self, plane: str):
        if isinstance(plane, str) and plane.strip():
            self._plane = plane.strip()
        else:
            raise ValueError("ERROR: The plane name can't be a blank string!")


    

    def add_seat(self, seat: Seat):
        if not isinstance(seat, Seat):
            raise TypeError("ERROR: Expected Seat instance!")
        
        if not seat.code in self._seats.keys():
            self._seats[seat.code] = seat
        else:
            raise ValueError("ERROR: This seat already exists!")
    

    def occupy_seat(self, seat_code: str):
        if seat_code in self._seats.keys():
            self._seats[seat_code].occupy()
        else:
            raise ValueError("ERROR: This seat doesn't exist!")
    

    def free_seat(self, seat_code: str):
        if seat_code in self._seats.keys():
            self._seats[seat_code].free()
        else:
            raise ValueError("ERROR: This seat doesn't exist!")
    
