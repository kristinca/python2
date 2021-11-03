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
        if not employee.company:
            employee.company = self.name
            employee.position = position
            employee.salary = salary
        else:
            print(f"{employee.first_name} {employee.last_name} is already working"
                  f" at the company {employee.company}.")

    def fire(self, employee, position):
        """Fire an employee from some position."""
        match employee.company:
            case self.name:
                if employee.position == position:
                    employee.company = None
                    employee.position = None
                    employee.salary = None
                else:
                    print(f'The employee {employee.first_name} {employee.last_name} is'
                          f' working at the company {self.name} but is '
                          f'not working at the position {position}.')
            case _:
                print(f'The employee {employee.first_name} {employee.last_name} is'
                      f' not working at the company {self.name}.')
