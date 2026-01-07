from utils_module_u import title
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
            if not code.isalnum():
                raise ValueError("ERROR: Code must be alphanumeric!")
            
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




    def to_dict(self):
        return {
            'code': self.code,
            'name': self.name,
            'price': self.price,
            'qtd': self.qtd
        }
    



    @staticmethod
    def from_dict(data: dict):
        return Product(**data)



    def __str__(self):
        return f"{self.code:^6} | {self.name:<25} | {self.price:<9.2f} | {self.qtd:<7}"


# Database functions
def search_product(data: list[dict], code: str):
    products = [Product.from_dict(d) for d in data]

    for index, prod in enumerate(products):
        if prod.code == code:
            return index
        
    return -1

def add_product(arq: str, prod: Product):
    data = grab_data(arq)

    if search_product(data, prod.code) != -1:
        raise ValueError("ERROR: This code's product exists in system!")

    data.append(prod.to_dict())
    save_data(arq, data)


def delete_product(arq: str, prod_cod: str):
    data = grab_data(arq)
    index_prod = search_product(data, prod_cod)

    if index_prod != -1:
        data.pop(index_prod)
        save_data(arq, data)
    else:
        raise ValueError("ERROR: This product doesn't exist!")


def update_product(arq: str, prod_cod: str, option: int, new_value):
    data = grab_data(arq)
    index_prod = search_product(data, prod_cod)

    if index_prod != -1:
        prod = Product.from_dict(data[index_prod])
        match option:
            case 1:
                
                prod.code = new_value
            case 2:
                prod.name = new_value
            case 3:
                prod.price = new_value
            case 4:
                prod.qtd = new_value
        data[index_prod] = prod.to_dict()
        save_data(arq, data)
    else:
        raise ValueError("ERROR: This product doesn't exist!")

# Data Processing functions
def ensure_exists_file(arq: str):
    if not os.path.exists(arq):
        title(f"CRIANDO ARQUIVO {arq}")
        sleep(1)
        with open(arq, 'x', encoding="utf-8") as file:
            json.dump([], file, indent=4, ensure_ascii=False)


def grab_data(arq: str):
    try:
        with open(arq, "r", encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []


def save_data(arq: str, data: list[dict]):
    with open(arq, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def print_data(arq: str):
    data = grab_data(arq)
    products = [Product.from_dict(d) for d in data]

    title("LISTA DE PRODUTOS CADASTRADOS")
    print(f"{'CÓDIGO':^6} | {'NOME':<25} | {'PREÇO(R$)':<9} | {'QTD':<7}")
    print('-'*57)

    for prod in products:
        print(prod)