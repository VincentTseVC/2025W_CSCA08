"""CSC 108 Summer 2021 Final Test: MarkUs Part, Question 4 (6 marks)

This code is provided solely for the personal and private use of students
taking the CSC108 course at the University of Toronto. Copying for purposes
other than this use is expressly prohibited. All forms of distribution of
this code, whether as given or with any changes, are expressly prohibited.

This file is:
Copyright (c) 2021 Angela Zavaleta Bernuy and Laura (Di) Chen.
"""

class Date:
    """A calendar date."""

    def __init__(self, day: int = 1, month: str = 'January',
                 year: int = 2000) -> None:
        """Initialize a calendar date with day, month and year.

        >>> d = Date(29, 'May', 2021)
        >>> d.day
        29
        >>> d.month
        'May'
        >>> d.year
        2021
        """
        self.day = day
        self.month = month
        self.year = year


    def __str__(self) -> str:
        """Return a string representation of this date.

        >>> d = Date(3, 'August', 2021)
        >>> print(d)
        3 August 2021
        """
        return '{0} {1} {2}'.format(self.day, self.month, self.year)


class Vaccine:
    """A vaccine appointment."""

    def __init__(self, product: str, date: "Date") -> None:
        """Initialize a vaccine appointment with the vaccine product name and
        the Date when it took place.

        >>> d = Date(3, 'May', 2021)
        >>> v = Vaccine('Pfizer', d)
        >>> v.product
        'Pfizer'
        >>> str(v.date)
        '3 May 2021'
        """
        self.product = product
        self.date = date

    def __str__(self) -> str:
        """Return a string representation of this vaccine appointment.

        >>> d = Date(3, 'May', 2021)
        >>> v = Vaccine('Pfizer', d)
        >>> print(v)
        Pfizer on 3 May 2021
        """
        return self.product + ' on ' + str(self.date)


# (1) Complete the following methods according to their docstrings.
#     There are 4 methods to be completed in total in this file.
#     You can earn part marks for a partial solution, even if it doesn't run.
# (2) Submit your modified file to MarkUs. Use the specified filename.
# (3) Verify you have submitted the right file to MarkUs by downloading it
#     again and checking it is the one you meant to submit.

# Note that the Date class is provided in the module date.py, and the
# Vaccine class is provided the module vaccine.py

class Vaccine_Passport:
    """A vaccine passport."""

    def __init__(self, patient_name: str) -> None:
        """Initialize a vaccine passport with the patient's name and
        an empty list of vaccines.

        >>> vs = Vaccine_Passport('Angela')
        >>> vs.patient
        'Angela'
        >>> vs.vaccines
        []
        """
        self.patient = patient_name
        self.vaccines = []


    def add_vaccine(self, vaccine: "Vaccine") -> bool:
        """Add a vaccine to the passport for the patient, only if they have
        less than two vaccines. Return True iff the vaccine was successfuly
        added to the passport, False otherwise.

        >>> vs = Vaccine_Passport('Angela')
        >>> d1 = Date(3, 'May', 2021)
        >>> v1 = Vaccine('Pfizer', d1)
        >>> vs.add_vaccine(v1)
        True
        >>> d2 = Date(3, 'July', 2021)
        >>> v2 = Vaccine('Pfizer', d2)
        >>> vs.add_vaccine(v2)
        True
        >>> vs.add_vaccine(v1)
        False
        """
        if len(self.vaccines) >= 2:
            return False

        self.vaccines.append(vaccine)
        return True


    def is_fully_vaccinated(self) -> bool:
        """Return True if and only if the patient is fully vaccinated. A patient
        is fully vaccinated if they have received exactly two vaccines.

        >>> vs = Vaccine_Passport('Angela')
        >>> d1 = Date(3, 'May', 2021)
        >>> v1 = Vaccine('Pfizer', d1)
        >>> vs.is_fully_vaccinated()
        False
        >>> vs.add_vaccine(v1)
        True
        >>> vs.is_fully_vaccinated()
        False
        >>> d2 = Date(3, 'July', 2021)
        >>> v2 = Vaccine('Pfizer', d2)
        >>> vs.add_vaccine(v2)
        True
        >>> vs.is_fully_vaccinated()
        True
        """
        return len(self.vaccines) == 2


    def __str__(self) -> str:
        """Return a string representation of a Vaccine Passport.
        (Note: You must use the method is_fully_vaccinated in your solution)

        >>> vs = Vaccine_Passport('Angela')
        >>> print(vs)
        The patient Angela has received the following vaccine(s):
        >>> d1 = Date(3, 'May', 2021)
        >>> v1 = Vaccine('Pfizer', d1)
        >>> vs.add_vaccine(v1)
        True
        >>> print(vs)
        The patient Angela has received the following vaccine(s):
        - Pfizer on 3 May 2021
        >>> d2 = Date(3, 'July', 2021)
        >>> v2 = Vaccine('Pfizer', d2)
        >>> vs.add_vaccine(v2)
        True
        >>> print(vs)
        Congratulations! You are fully vaccinated!
        The patient Angela has received the following vaccine(s):
        - Pfizer on 3 May 2021
        - Pfizer on 3 July 2021
        """

        res = ''
        if self.is_fully_vaccinated():
            res += 'Congratulations! You are fully vaccinated!'

        res += f'The patient {self.patient} has received the following vaccine(s):'

        for vc in self.vaccines:
            res += '- ' + str(vc)    # str(vc) OR Vaccine.__str__(vc)

        return res
