from company3 import Company3
from employee3 import Employee3


class Offer:
    minimum_pay = 15000

    def __init__(self, company, employee, salary, position):
        if not isinstance(company, Company3):
            raise Exception(f"{company} is not instance of class Company. Can't make offer.")

        if not isinstance(employee, Employee3):
            raise Exception(f"{employee} is not instance of class Employee. Can't make offer.")

        if not isinstance(salary, int):
            raise Exception(f"{salary} is not instance of Integer. Can't make offer.")

        if not isinstance(position, str):
            raise Exception(f"{position} is not instance of String. Can't make offer.")

        if salary < self.minimum_pay:
            raise Exception(f"Salary provided under minimum wage of {Offer.minimum_pay}")

        self.company = company
        self.employee = employee
        self.salary = salary
        self.position = position

        self.receive_offer(employee)

    @staticmethod
    def make_offer(company, employee, salary, position):
        if not isinstance(employee, Employee3):
            raise Exception(f"{employee} is not instance of class Employee. Can't make offer.")

        offer = Offer(company, employee, salary, position)
        print(offer)

    def receive_offer(self, employee):
        employee.offers[self.company.company_id] = self

    @staticmethod
    def accept_offer(employee, company):
        if not isinstance(company, Company3):
            raise Exception(f"{company} must be instance of class Company")
        elif employee.company:
            raise Exception(f"{Employee3.full_name(employee)} is already employed.")
                            # in f" {employee.company}" ???)

        offer = employee.offers.get(company.company_id)
        if not offer:
            raise Exception(f"No offer received from {company}")

        employee.company = offer.company
        employee.salary = offer.salary
        employee.position = offer.position
        offer.company.employee_list.append(employee)

        print(f"{Employee3.full_name(employee)} accepted the offer from company {Company3.company_name(company)}")

        del employee.offers[offer.company.company_id]

    def serialize(self):
        print(self.__str__())

    def __str__(self):
        # return f"Offer from {self.company} to {self.employee}"
        info = dict()
        comp_id = self.company.company_id
        info[comp_id] = self.position
        return info
