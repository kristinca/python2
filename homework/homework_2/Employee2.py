from other_func import nasterisk


class Employee2:
    minimum_pay = 15000

    def __init__(
            self,
            first_name,
            last_name,
            email,
            salary=None,
            position=None,
            company=None,
            job_offer_answer=None
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        if company and salary < Employee2.minimum_pay:
            raise Exception(f"Salary provided under minimum wage of {Employee2.minimum_pay}")
        self.salary = salary
        self.position = position
        self.company = company
        self.job_offer_answer = job_offer_answer

    def full_name(self):
        full_name = f"{self.first_name} - {self.last_name}"
        return full_name

    def __str__(self):
        return self.full_name()

    def quit(self):
        """Quit a job."""
        s1 = f"\n  Dear {self}, the company {self.company} you work in has " \
             f"{self.company.months_notice} months notice.\n"
        s2 = f"If you would like to quit now, enter 'NOW'...\t"
        self.company.ans_quit = str(input('\n'+nasterisk(len(s1)+2)+s1+nasterisk(len(s1)+2)+'\n'+s2))
        match self.company.ans_quit.lower():
            case 'now':
                self.company.employee_list.remove(self)
                self.company = None
                self.salary = 0
                self.position = None
                print(f'{self} has just quit.\n')
            case _:
                print(f"Thank you for giving the min {self.company.months_notice} months notice.\n")