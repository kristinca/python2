class Company3:

    def __init__(self, name, address, company_id):
        self.name = name
        self.address = address
        self.company_id = company_id
        self.employee_list = []

    def serialize(self):
        print(self.__str__())

    def company_name(self):
        return self.name

    def fire(self, employee):
        # if not isinstance(employee, Employee3):
        #     raise Exception(f"{employee} is not instance of class Employee. Can't fire employee")

        if not employee.company:
            raise Exception(f"{employee} can't be fired, not employed in a company.")
        elif employee.company.company_id != self.company_id:
            raise Exception(f"Can't fire {employee} from {self.name}, employee already working at {employee.company}")

        employee.company = None
        employee.position = None
        employee.salary = None
        self.employee_list.remove(employee)
        print(f"{employee} was fired from {self.name}.")

    def get_salary_costs(self):
        total_salary_costs = 0

        for employee in self.employee_list:
            total_salary_costs += employee.salary

        return total_salary_costs

    # value returning
    def return_self(self):
        return self.name

    def __str__(self):
        info = dict()
        info['company name'] = Company3.return_self(self)
        info['address'] = self.address
        info['company_id'] = self.company_id
        info['employee_list'] = self.employee_list
        return info
