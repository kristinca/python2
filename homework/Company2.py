from Employee2 import Employee2
from other_func import nasterisk


class Company2:

    months_notice = 2

    def __init__(self, name, address, company_id, answer_quit=None):
        self.name = name
        self.address = address
        self.company_id = company_id
        self.employee_list = []
        self.answer_quit = answer_quit

    def hire(self, employee, position, salary):
        if salary < employee.minimum_pay:
            raise Exception(f"Salary provided under minimum wage of {employee.minimum_pay}")

        if employee.company:
            raise Exception(f"{employee} can not be hired. Already employed in {employee.company}")

        s1 = f'  Dear {employee}, the company {self} would like to hire you at the position {position}' \
             f'for a salary of {salary}.\n'
        s2 = f'If you accept this offer, enter Y, otherwise enter N ...\t'

        employee.job_offer_answer = str(input(
            nasterisk(len(s1)+2)+'\n'+s1+nasterisk(len(s1)+2)+'\n'+s2))
        match employee.job_offer_answer.lower():
            case 'y':
                employee.company = self
                employee.position = position
                employee.salary = salary
                self.employee_list.append(employee)
                print(f"{self.name} is hiring {employee}")
            case 'n':
                print(f'{employee} has declined the job offer.')
            case _:
                print(f'The answer {employee.job_offer_answer} is not "y" or "n".\n')
                self.hire(employee, position, salary)

    def fire(self, employee):
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

    def __str__(self):
        return self.name
