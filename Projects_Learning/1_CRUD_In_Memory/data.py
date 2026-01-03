from datetime import date

# Classes
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


# Database commands
def add_user(repository: list, user: User):
    if not isinstance(user, User):
        raise ValueError("ERROR! The user must be a User data")
    
    if any(u.name.lower() == user.name.lower() for u in repository):
        raise ValueError("ERROR! User already exists")
    
    repository.append(user)


def read_user(repository: list, name: str):
    if not (isinstance(name, str) and name.strip()):
        raise ValueError("ERROR! Invalid Name!")
    
    for user in repository:
        if name.lower() == user.name.lower():
            return user

    raise LookupError("User not found")


def print_data(repository: list):
    print(f"{' ID':^3} | {'NOME':<20} | {'PESO':<7} | {'ALTURA':<7} | {'IDADE':<3}")
    print("-"*57)
    for index, user in enumerate(repository, start=1):
        print(f"{index:^3} | {user.name:<20} | {user.weight:<7.2f} | {user.height:<7.2f} | {str(user.calculate_age):<3} anos")
