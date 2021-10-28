class Employee:
    """A simple attempt to model an employee"""
    def __init__(self, first_name, last_name, email, salary, position, company):
        """Initialize first name, last name, email, position and the company"""
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.email = email
        self.position = position
        self.company = company
