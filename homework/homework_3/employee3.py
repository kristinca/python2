class Employee3:

    def __init__(
            self,
            first_name,
            last_name,
            email,
            embg,
            salary=None,
            position=None,
            company=None
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

        self.embg = self.validate_embg(embg)

        self.salary = salary
        self.position = position
        self.company = company
        Employee3.add_to_employee_list(self)
        self.offers = dict()

    def add_to_employee_list(self):
        if self.company:
            self.company.employee_list.append(self.full_name())
        else:
            self.company = None

    def delete_offers(self):
        self.offers.clear()

    @staticmethod
    def validate_embg(embg):
        if len(str(embg)) != 13:
            raise Exception(f"Invalid EMBG: {embg}. Must be 13 digits.")

        return embg

    def serialize(self):
        print(self.__str__())

    # instance methods
    def full_name(self):
        full_name = f"{self.first_name} - {self.last_name}"
        return full_name

    def emp_company(self):
        return self.company

    def quit(self):
        if self.company is None:
            raise Exception(f"{self} is not employed. Can't quit.")

        print(f"{Employee3.full_name(self)} is quitting from {self.company.return_self()}")
        self.company.employee_list.remove(Employee3.full_name(self))
        self.company = None
        self.salary = None
        self.position = None

    def __str__(self):
        info = dict()
        info['first_name'] = self.first_name
        info['last_name'] = self.last_name
        info['email'] = self.email
        info['EMBG'] = self.embg
        info['salary'] = self.salary
        info['position'] = self.position
        if self.company:
            info['company'] = self.company.return_self()
        else:
            info['company'] = None
        info['job_offers'] = self.offers
        return info
