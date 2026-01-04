from datetime import date

# Classes
class Student:
    def __init__(self, id: int, name: str, birth_year: int, grades: list):
        self.id = id
        self.name = name
        self.birth_year = birth_year
        self.grades = grades


    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, id):
        if isinstance(id, int) and id > 0:
            self._id = id
        else:
            raise ValueError("ERROR: The ID must be a valid integer greater than 0")
        
    
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if isinstance(name, str) and name.strip():
            self._name = name.strip()
        else:
            raise ValueError("ERROR: The name can't a blank string")
        

    @property
    def birth_year(self):
        return self._birth_year
    @birth_year.setter
    def birth_year(self, birth_year):
        if isinstance(birth_year, int) and birth_year > 0:
            self._birth_year = birth_year
        else:
            raise ValueError("ERROR: The birth_year must be greater than 0")
    

    @property
    def grades(self):
        return self._grades
    grades.setter
    def grades(self, grades: list):
        if isinstance(grades, list) and len(grades) > 0:
            self._grades = grades
        else:
            raise ValueError("ERROR: The lenght's grades list must be greater than 0")
    

    
    
    @property
    def calculate_media(self):
        return sum(self.grades) / len(self.grades)
    

    @property
    def calculate_age(self):
        return date.today().year - self.birth_year
    

    @property
    def calculate_std(self):
        media = self.calculate_media
        var = sum((n-media)**2 for n in self.grades) / len(self.grades)
        return var(**(1/2)) 
        