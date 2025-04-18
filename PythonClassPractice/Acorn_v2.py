"""CSC110 Fall 2021: Term Test 2, Question 3 (Object Oriented Design)

Module Description
==================
This module contains instructions for this question. There are TWO
parts of this question, labelled "Part (a)", "Part (b)", etc.
The comments in this file contain instructions on how to complete each part,
so please read those comments carefully.

SUBMIT THIS FILE FOR GRADING!

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC110 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2021 Mario Badr and Tom Fairgrieve.
"""


###################################################################################################
# Modelling a Problem Domain
###################################################################################################
# In this question, you will model a new problem domain by designing classes in a similar style to
# the food delivery system we studied in lecture.

###################################################################################################
# Description of the Problem Domain
###################################################################################################
# Your client is the University of Toronto. They want new software to manage the grades of their
# students. The grade system will store:
#   1. GRADES that each have the course id (e.g., 'CSC110Y'), term id (e.g., '20219'), and score in
#   the course (i.e., an integer ranging from 0 to 100, inclusive).
#   2. STUDENTS that each have a utorid (e.g., 'astudent') and a collection of grades.

###################################################################################################
# Part (a) - Entity data classes
###################################################################################################
# Your first task is to complete the two data classes below, which represent  the two main entities
# in our computational model.  Read the provided docstrings and use them to complete each data class
# body.
#
# Do NOT add any additional instance attributes or change the class docstring.
# You do NOT need to add any representation invariants or doctest examples.

class Grade:
    """A grade on Acorn.

    Instance Attributes:
       - course: the course (e.g., 'CSC110Y1') this grade was achieved in.
       - term: the term (e.g., '20219') this grade was achieved in.
       - score: an integer representing the grade achieved.
    """

    def __init__(self, c: str, t: str, s: int) -> None:
        ...


class Student:
    """A student who can have courses grades on acorn.

    Instance Attributes:
        - utorid: the utorid of this student
        - grades: a dictionary mapping a course (e.g., 'CSC110Y1') to the student's Grade in that
            course.
    """

    def __init__(self, uid: str) -> None:
        ...


###############################################################################
# Part (b) - Manager class
###############################################################################
# The class below is responsible for keeping track of all instances of the entities in our
# model and performing mutating operations on them.
#
# Read through the class and implement the methods that have empty bodies.
# Do NOT change anything else in the class (attributes, methods that we have implemented).


class AcornSystem:
    """A class that tracks students and their grades."""
    # Private Instance Attributes:
    #   - _students: a dictionary mapping utorids to Students
    _students: dict[str, Student]

    def __init__(self, initial_students: list[Student]) -> None:
        """Initialize a new AcornSystem, adding every student in initial_students to this system.

        Precondition:
            - Every student in initial_students has a unique utorid

        >>> acorn_system = AcornSystem([])
        >>> acorn_system.student_count()
        0
        """
        self._students = {}
        for student in initial_students:
            self._students[student.utorid] = student

    def student_count(self) -> int:
        """Return the number of students in this system."""
        return len(self._students)

    def add_grade(self, utorid: str, grade: Grade) -> bool:
        """Add grade to the student with utorid and return whether the grade was added successfully.

        Do not add grade if the student with utorid already has a grade assigned for that course.

        Preconditions:
            - A student with utorid exists in this system
        """
        student = self._students[utorid]

        if grade.course in student.grades:
            return False
        else:
            student.grades[grade.course] = grade
            return True

    def get_grade(self, utorid: str, course: str) -> tuple[str, int]:
        """Return a tuple of the term and score that the student with utorid achieved in course.

        Preconditions:
            - A student with utorid exists in this system
            - The student in this system with utorid has a grade for course

        >>> acorn_system = AcornSystem([Student('astudent', {})])
        >>> acorn_system.add_grade('astudent', Grade('CLA204H1', '20209', 76))
        True
        >>> acorn_system.get_grade('astudent', 'CLA204H1')
        ('20209', 76)
        """
        # TODO: implement this function body and remove this todo

    def amend_grades(self, course: str, amendments: dict[str, int]) -> int:
        """Update the grades for course based on the amendments, which maps student utorids to
        the amended score. Only students in amendments should have their grade amended.

        Return the number of successful amendments made. An amendment is not successful if the
        student has no grade on record for the course. No mutation should occur for students who
        have no grade on record for course.

        Preconditions:
            - Every utorid in amendments is a student in this system

        >>> acorn_system = AcornSystem([Student('astudent', {})])
        >>> acorn_system.add_grade('astudent', Grade('CLA204H1', '20209', 76))
        True
        >>> acorn_system.amend_grades('CLA204H1', {'astudent': 80})
        1
        >>> acorn_system.get_grade('astudent', 'CLA204H1')
        ('20209', 80)
        """
        # TODO: implement this function body and remove this todo


    def calculate_averages(self, utorid: str) -> dict[str, float]:
        """Return a dictionary mapping each term to the average grade achieved in that term for the
        student with utorid. The dictionary only includes terms where the student has taken courses.

        Preconditions:
            - A student with utorid exists in this system

        >>> acorn_system = AcornSystem([Student('astudent', {})])
        >>> acorn_system.add_grade('astudent', Grade('CLA204H1', '20209', 76))
        True
        >>> acorn_system.calculate_averages('astudent')
        {'20209': 76.0}
        """
        # TODO: implement this function body and remove this todo

        
if __name__ == '__main__':
    import doctest
    doctest.testmod()