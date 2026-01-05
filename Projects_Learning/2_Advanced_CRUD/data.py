from datetime import date
from gui_utils import read_int, title, read_name, read_float
from time import sleep
import os
import json

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
    

    
    
    @staticmethod
    def media(grades: list):
        return sum(grades) / len(grades)
    

    @staticmethod
    def age(birth_year):
        return date.today().year - birth_year
    

    @staticmethod
    def std(media: float, grades: list):
        media = media
        var = sum((n-media)**2 for n in grades) / len(grades)
        return var**(1/2)


    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'birth_year': self.birth_year,
            'grades': self.grades,
        } 


    @staticmethod
    def from_dict(stud_dict: dict):
        return Student(
            stud_dict['id'],
            stud_dict['name'],
            stud_dict['birth_year'],
            stud_dict['grades']
        )
    

# Database Functions
def add_student(arq: str, student: Student):
    data = grab_data(arq)
    
    if search_student(data, student.id) != -1:
        raise ValueError("ERROR: ID already exists!")
    
    data.append(student.to_dict())

    save_data(arq, data)


def print_data(arq: str):
    data = grab_data(arq)
    
    title("LISTA DE ESTUDANTES CADASTRADOS")
    print(f"{'ID':^5} | {'NOME':<20} | {'IDADE':<3} | {'NOTAS':<20} | {'MÉDIA':<7} | {'DESVIO P.':<7}")
    print("-"*85)
    for stud in data:
        age = Student.age(stud['birth_year'])
        media = Student.media(stud['grades'])
        std = Student.std(media, stud['grades'])

        print(f"{stud['id']:^5} | {stud['name']:<20} | {str(age):^5} | ", end="")
        print(f"{str(stud['grades']):<20} | {media:<7.2f} | {std:<7.2f}")


def search_student(repository: list[dict], id_stud: int) -> int:
    for ind, stud in enumerate(repository):
        if stud['id'] == id_stud:
            return ind

    return -1


def delete_student(id_stud: int, arq: str):
    data = grab_data(arq)
    index_stud = search_student(data, id_stud)

    if index_stud != -1:
        data.pop(index_stud)
        save_data(arq, data)
        title("ALUNO DELETADO COM SUCESSO!")
    else:
        raise ValueError("ERROR: This student doesn't exist!")


def update_student(id_stud: int, option: int, arq: str):
    data = grab_data(arq)
    index_stud = search_student(data, id_stud)

    if index_stud != -1:
        match option:
            case 1:
                new_id = read_int("Novo ID: ")

                if search_student(data, new_id) != -1:
                    raise ValueError("ERROR: ID already exists!")

                data[index_stud]['id'] = new_id
            case 2:
                new_name = read_name("Novo Nome: ")
                data[index_stud]['name'] = new_name
            case 3:
                new_birth_year = read_int("Novo Ano de Nascimento: ")
                data[index_stud]['birth_year'] = new_birth_year
            case 4:
                note1 = read_float("Nova Nota1: ")
                note2 = read_float("Nova Nota2: ")

                data[index_stud]['grades'] = [note1, note2]
        save_data(arq, data)
        title("ALUNO ATUALIZADO COM SUCESSO!")
    else:
        raise ValueError("ERROR: This student doesn't exist!")


def is_database_exists(arq: str):
    if not os.path.exists(arq):
        try:
            title(f"CRIANDO ARQUIVO {arq}")
            with open(arq, "w", encoding="utf-8") as file:
                json.dump([], file, indent=4)
            sleep(1)
        except Exception as e:
            title("ERRO AO TENTAR CRIAR O ARQUIVO")
            print(f"ERRO: {e}")

    title(f"ARQUIVO {arq} CARREGADO COM SUCESSO!")


def grab_data(arq: str):
    try:
        with open(arq, "r", encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []


def save_data(arq: str, data: list):
    with open(arq, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)