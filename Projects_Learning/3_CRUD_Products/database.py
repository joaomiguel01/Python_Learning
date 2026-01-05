from gui_utils import title
from time import sleep
import os
import json

# Classes
class Product:
    def __init__(self, code: str, name: str, price: float, qtd: int):
        self.code = code
        self.name = name
        self.price = price
        self.qtd = qtd


    @property
    def code(self):
        return self._code
    @code.setter
    def code(self, code: str):
        if isinstance(code, str) and code.strip():
            if len(code) == 6:
                self._code = code.strip()
            else:
                raise ValueError("ERROR: The code must have 6 chars!")
        else:
            raise ValueError("ERROR: Enter a valid code!")
    

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name: str):
        if isinstance(name, str) and name.strip():
            self._name = name.strip().upper()
        else:
            raise ValueError("ERROR: Enter a valid name!")
    

    @property
    def price(self):
        return self._price
    @price.setter
    def price(self, price: float):
        if isinstance(price, (int, float)) and price > 0:
            self._price = float(price)
        else:
            raise ValueError("ERROR: Price must be a positive number!")
    

    @property
    def qtd(self):
        return self._qtd
    @qtd.setter
    def qtd(self, qtd: int):
        if isinstance(qtd, int) and qtd >= 0:
            self._qtd = qtd
        else:
            raise ValueError("ERROR: Quantity must be greater than or equal to 0!")
    

    @property
    def total_value(self):
        return self.price * self.qtd





    def __str__(self):
        return f"{self.code:^6} | {self.name:<25} | R${self.price:<7.2f} | {self.qtd:<7}"


# Database functions


# Data Processing functions
def ensure_exists_file(arq: str):
    if not os.path.exists(arq):
        title(f"CRIANDO ARQUIVO {arq}")
        sleep(1)
        with open(arq, 'x', encoding="utf-8") as file:
            json.dump([], file, indent=4, ensure_ascii=False)
     