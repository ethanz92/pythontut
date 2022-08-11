"""Class to take and store basic information of an employee"""

class Employee:

    def __init__(self, f_name, l_name, salary):
        """Initialise name and salary attributes."""
        self.f_name = f_name
        self.l_name = l_name
        self.salary = salary
        self.employee_info = [self.f_name, self.l_name, self.salary]
    
    def give_raise(self, raise_amount = 5000):
        """Give the employee a raise!"""
        self.employee_info[2] += raise_amount
        return self.employee_info