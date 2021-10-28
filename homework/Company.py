from Employee import Employee


class Company:
    """A simple attempt to model a company."""

    def __init__(self, name, address, company_id):
        """"Initialize name, address and company id."""
        self.name = name
        self.address = address
        self.company_id = company_id

    def hire(self, employee, position, salary):
        """Hire an employee at some position and define the salary."""
        employee.company = self.name
        employee.position = position
        employee.salary = salary

    def fire(self, employee, position):
        """Fire an employee from some position."""
        if employee.company == self.name and employee.position == position:
            employee.company = None
            employee.position = None
            employee.salary = None
        else:
            print(f'The employee {employee.first_name} {employee.last_name} is'
                  f'not working at company {self.name} or is '
                  f'not working at the position {position}.')