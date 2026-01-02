from datetime import date
from time import sleep
from utils import menu, title, read_option

class User:
    def __init__(self, name, year_age, weight, height):
        self.name = name
        self.year_age = year_age
        self.weight = weight
        self.height = height


    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if isinstance(name, str) and name.strip():
            self._name = name.strip()
        else:
            raise ValueError("ERROR!: The name can't be a blank string")


    @property
    def year_age(self):
        return self._year_age
    @year_age.setter
    def year_age(self, year_age):
        if isinstance(year_age, int) and year_age > 0:
            self._year_age = year_age
        else:
            raise ValueError("ERROR!: The year_age must be greater than 0")
    

    @property
    def weight(self):
        return self._weight
    @weight.setter
    def weight(self, weight):
        if isinstance(weight, (int, float)) and weight > 0:
            self._weight = float(weight)
        else:
            raise ValueError("ERROR!: The weight must be greater than 0")
    

    @property
    def height(self):
        return self._height
    @height.setter
    def height(self, height):
        if isinstance(height, (int, float)) and height > 0:
            self._height = float(height)
        else:
            raise ValueError("ERROR!: The height must be greater than 0")
    

    @property
    def calculate_age(self):
        return date.today().year - self.year_age


def main():
    while True:
        database = []
        menu()
        
        choice = read_option("Digite sua escolha: ", 5)
        sleep(1)
        print()


        if choice == 1:
            # Register Users
            pass
        elif choice == 2:
            # List Users
            pass
        elif choice == 3:
            # Delete Users
            pass
        elif choice == 4:
            # Update Users
            pass
        elif choice == 5:
            # Exit the program
            title("Saindo do Sistema")
            sleep(1)
            title("Até logo!")
            break
        

if __name__ == "__main__":
    main()