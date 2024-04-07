import pickle
from dataclasses import dataclass
from datetime import datetime


@dataclass
class Specialty:
    name: str
    number: int


@dataclass
class Student:
    first_name: str
    last_name: str
    birth_date: datetime
    average_mark: float
    has_scholarship: bool
    phone_number: str
    address: str


@dataclass
class Group:
    specialty: Specialty
    course: int
    students: list[Student]


def write_groups_information(groups: list[Group]) -> int:
    with open("groups.pickle", "wb") as pickle_file:
        pickle.dump(groups, pickle_file)
    return max([len(group.students) for group in groups]) if groups else 0


def write_students_information(students: list[Student]) -> int:
    with open("students.pickle", "wb") as pickle_file:
        pickle.dump(students, pickle_file)
    return len(students)


def read_groups_information() -> set[str]:
    with open("groups.pickle", "rb") as pickle_file:
        return set([i.specialty.name for i in pickle.load(pickle_file)])


def read_students_information() -> list[Student]:
    with open("students.pickle", "rb") as pickle_file:
        return pickle.load(pickle_file)
