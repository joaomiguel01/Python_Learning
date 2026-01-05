from datetime import date
import json

# Classes
class Student:

    number_of_studs = 0

    def __init__(self, id: int, name: str, birth_year: int, grades: list):
        self.id = id
        self.name = name
        self.birth_year = birth_year
        self.grades = grades
        Student.number_of_studs += 1


    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, id):
        if isinstance(id, int) and id > 0:
            self._id = id
        else:
            raise ValueError("ERROR: The ID must be greater than 0")

    
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
        current_year = date.today().year
        if isinstance(birth_year, int) and 1900 <= birth_year <= current_year:
            self._birth_year = birth_year
        else:
            raise ValueError(f"ERROR: The birth_year must be between 1900 and {current_year}")
    

    @property
    def grades(self):
        return self._grades
    @grades.setter
    def grades(self, grades: list):
        if isinstance(grades, list) and len(grades) > 0:
            self._grades = grades
        else:
            raise ValueError("ERROR: The length's grades list must be greater than 0")
    

    
    
    @property
    def media(self):
        return sum(self.grades) / len(self.grades)
    

    @property
    def age(self):
        return date.today().year - self.birth_year
    

    @property
    def std(self):
        media = self.media
        var = sum((n-media)**2 for n in self.grades) / len(self.grades)
        return var**(1/2)


    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'birth_year': self.birth_year,
            'age': self.age,
            'grades': self.grades,
            'media': self.media,
            'std': self.std
        } 


# Database Functions
def add_student(arq: str, student: Student):
    with open(arq, "r", encoding="utf-8") as file:
        data = json.load(file)
    
    new_student = student.to_dict()


    data.append(new_student)

    with open(arq, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
