from __future__ import annotations
from typing import Optional, Union
from random import randint


class Person:
    """A Class that represent a Person

    === Attribute ===
    name: the name of the person
    age: the age of the person
    gender: the gender of the person

    === Representation Invariant ===
    - age > 0
    - gender in ('M', 'F')

    === Sample Usage ===
    >>> vc = Person('Vincent', 18, 'M')
    >>> vc.name
    'Vincent'
    """

    name: str
    age: int
    gender: str

    def __init__(self, name: str, age: int, gender: str) -> None:
        """Initialize the person with the given name, age and gender
        Percondition:
            age > 0
            gender in ('M', 'F')
        """
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self) -> str:
        """Return a string representation of a Person.
        """
        return f'{self.name}, {self.age}'

    def __gt__(self, other: Person) -> bool:
        """Return True iff this Person is older than the other person.
        """
        return self.age > other.age

    def eat(self, food: str) -> str:
        return f'{self.name} is eating {food}'

    def give_birth(self, husband: Person, child_name: str) -> Person:
        """
        Precondition:
         - ...
        """

        assert self.age > 18
        assert husband.age > 18
        assert self.gender == 'F'
        assert husband.gender == 'M'

        return Person(child_name, 1, 'F' if randint(0, 1) == 0 else 'M')


# Child(Parent)
# Derived(Base)
# Sup(Supper)

class Student(Person):
    """A Class that represents a Student

    === Public Attribute ===
    utorid: the utorid of the student

    === Private Attribute ===
    _password: the password of the student
    """

    utorid: str
    _password: str
    courses: dict[str, Grade]

    # {'CSC148': NumericGrade(95.0),
    #  'CSC165': None
    #  'ECO101': LetterGrade('A+')}

    def __init__(self, name: str, age: int, gender: str, utorid: str) -> None:
        """Initialize the person with the given name, age and gender
        Percondition:
            age > 0
            gender in ('M', 'F')
        """
        # Person.__init__(self, name, age, gender)
        super().__init__(name, age, gender)
        self.utorid = utorid
        self._password = '1234'
        self.courses = {}


    def change_password(self, new_password: str) -> None:
        """..."""
        self._password = new_password

    def enroll(self, course: Course) -> bool:
        # if len(course.students) >= course.capacity:
        #     return False
        # course.students.append(self)
        # return True
        self.courses[course.code] = None
        return course.enroll(self)

    def set_grade(self, course: Course, mark: Union[str, float]) -> None:
        if course.code not in self.courses:
            return

        if isinstance(mark, float):
            self.courses[course.code] = NumericGrade(mark)
        else:
            self.courses[course.code] = LetterGrade(mark)

    def cgpa(self) -> float:

        total = 0
        num = 0
        for grade in self.courses.values():
            total += grade.gpa()
            num += 1

        return total / num

    # Method Override
    def __str__(self) -> str:
        """Return a string representation of a Person.
        """
        # return f'{Person.__str__(self)} {self.utorid}'
        return f'{super().__str__()} {self.utorid}'


# Abstract Class (Cannot be instantiated)
class Grade:
    ...
    # Abstract Method (Any Child Class MUST complete Override this method)
    def gpa(self) -> float:
        raise NotImplementedError

class LetterGrade(Grade):

    def __init__(self, mark: str) -> None:
        self.mark = mark

    # Method Override
    def gpa(self) -> float:
        if self.mark in ('A', 'A+'):
            return 4.0
        elif self.mark == 'A-':
            return 3.7
        elif self.mark == 'B+':
            return 3.3
        # ...
        else:
            return 0.0


class NumericGrade(Grade):

    def __init__(self, mark: float) -> None:
        self.mark = mark

    # Method Override
    def gpa(self) -> float:
        if self.mark >= 85:
            return 4.0
        elif self.mark >= 80:
            return 3.7
        elif self.mark >= 78:
            return 3.3
        # ....
        else:
            return 0.0


class Course:

    code: str
    capacity: int
    students: list[Student]
    instructor: Professor

    def __init__(self, code: str, capacity: int, instructor: Professor) -> None:
        self.code = code
        self.capacity = capacity
        self.students = []
        self.instructor = instructor
        instructor.teach(self)

    def enroll(self, student: Student) -> bool:
        if len(self.students) >= self.capacity:
            return False
        self.students.append(student)
        return True


# Abstract
class Faculty(Person):

    empID: int

    def __init__(self, name: str, age: int, gender: str, empID: int) -> None:
        """Initialize the person with the given name, age and gender
        Percondition:
            age > 0
            gender in ('M', 'F')
        """
        # Person.__init__(self, name, age, gender)
        super().__init__(name, age, gender)
        self.empID = empID


    def get_salary(self) -> float:
        raise NotImplementedError


class Professor(Faculty):

    teaching_courses: list[Course]

    def __init__(self, name: str, age: int, gender: str, empID: int) -> None:
        """Initialize the person with the given name, age and gender
        Percondition:
            age > 0
            gender in ('M', 'F')
        """
        # Faculty.__init__(self, name, age, gender, empID)
        super().__init__(name, age, gender, empID)
        self.teaching_courses = []

    def teach(self, course: Course) -> None:
        self.teaching_courses.append(course)


    def get_salary(self) -> float:
        return len(self.teaching_courses) * 5000


class StudentTA(Student, Faculty):

    hours: int

    def __init__(self, name: str, age: int, gender: str, utorid: str, empID: int) -> None:
        """Initialize the person with the given name, age and gender
        Percondition:
            age > 0
            gender in ('M', 'F')
        """
        Student.__init__(self, name, age, gender, utorid)
        Faculty.__init__(self, name, age, gender, empID)
        self.hours = 0

    def add_contract(self, hour: int) -> None:
        self.hours += hour

    def get_salary(self) -> float:
        return self.hours * 46.5

class Cleaner(Faculty):

    def __init__(self, name: str, age: int, gender: str, empID: int) -> None:
        """Initialize the person with the given name, age and gender
        Percondition:
            age > 0
            gender in ('M', 'F')
        """
        # Faculty.__init__(self, name, age, gender, empID)
        super().__init__(name, age, gender, empID)

    def get_salary(self) -> float:
        return 40000

if __name__ == "__main__":
    a = Person("Vincent", 18, "M")
    print(a)

    alice = Student('Alice', 18, 'F', 'alice123')
    # print(alice._password)
    print(alice.eat('🍠'))
    print(alice)

    vc = Professor('Vincnet', 19, 'M', 101)


    csc148 = Course('CSC148', 3, vc)
    csc165 = Course('CSC165', 4, vc)
    eco101 = Course('ECO101', 10, vc)

    csc148.enroll(alice)

    alice.enroll(csc148)

    alice.set_grade(csc148, 'A+')

    print(alice.cgpa())

    bob = Cleaner('洗馬桶的', 70, 'M', 102)



    print(bob.get_salary())
    print(vc.get_salary())

