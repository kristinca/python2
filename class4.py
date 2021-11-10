import json


class Company:

    def __init__(self, name, address, company_id):
        self.name = name
        self.address = address
        self.company_id = company_id
        self.employee_list = []
        self.assets = []

    def make_offer(self, employee, salary, position):
        if not isinstance(employee, Employee):
            raise Exception(f"{employee} is not instance of class Employee. Can't make offer.")

        offer = Offer(self, employee, salary, position)
        print(offer)

    def fire(self, employee):
        if not isinstance(employee, Employee):
            raise Exception(f"{employee} is not instance of class Employee.")

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

    def __repr__(self):
        return str(self)


class Employee:
    position = None

    def __init__(
            self,
            first_name,
            last_name,
            email,
            embg,
            salary=None,
            company=None
    ):
        try:
            print(self.asset)
        except:
            raise Exception("You must implement asset attribute")
        self.first_name = first_name
        self.last_name = last_name
        self.email = email

        self.embg = self.validate_embg(embg)
        self.salary = salary
        self.company = company
        self.offers = dict()

    @staticmethod
    def validate_embg(embg):
        if len(embg) != 13:
            raise Exception(f"Not a valid embg.")
        return embg

    # instance methods
    def full_name(self):
        full_name = f"{self.first_name} - {self.last_name}"
        return full_name

    def receive_offer(self, offer):
        if not isinstance(offer, Offer):
            raise Exception(f"{offer} is not instance of Offer class. Can't receive the offer.")

        self.offers[offer.company.company_id] = offer

    def accept_offer(self, company):
        if not isinstance(company, Company):
            raise Exception(f"{company} must be instance of class Company")
        elif self.company:
            raise Exception(f"{self} is already employed in {self.company}")

        offer = self.offers.get(company.company_id)
        if not offer:
            raise Exception(f"No offer received from {company}")

        self.company = offer.company
        self.salary = offer.salary
        self.position = offer.position
        offer.company.employee_list.append(self)

        print(f"{self} accepted the offer from company {self.company}")

        del self.offers[offer.company.company_id]

    def quit(self):
        if self.company is None:
            raise Exception(f"{self} is not employed. Can't quit.")

        print(f"{self} is quitting from {self.company}")
        self.company.employee_list.remove(self)
        self.company = None
        self.salary = None
        self.position = None

    def __repr__(self):
        return str(self)

    def __str__(self):
        return self.full_name()

    def do_work(self):
        if self.company:
            self.company.assets.append(self.asset)

    # def serialize(self):
    #     return self.__dict__

    def serialize(self):
        new_attributes = dict()

        for key, value in self.__dict__.items():
            new_key = key.replace("_", " ").title()
            new_attributes[new_key] = value

        return new_attributes


class Offer:
    minimum_pay = 15000

    def __init__(self, company, employee, salary, position):
        if not isinstance(company, Company):
            raise Exception(f"{company} is not instance of class Company. Can't make offer.")

        if not isinstance(employee, Employee):
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

        employee.receive_offer(self)

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"Offer from {self.company} to {self.employee}"


# Create class Developer and class Accountant, should inherit from Employee
# two class attributes -> 1st. position, 2nd. asset -> "coding", "calculation"
class Developer(Employee):
    position = "Developer"
    asset = "coding"


class Accountant(Employee):
    position = "Accountant"
    asset = "calculating"


# print(toshe.position)

semos = Company("Semos", "Kuzman Josifovski Pitu br. 1000", "1234")
seavus = Company("Seavus AD", "Boris Trajkovski br 60", "9876")

toshe = Developer("Toshe", "Petrovski", "toshe@gmail.com", "1234567891011")
semos.make_offer(toshe, 50000, "Developer")
toshe.accept_offer(semos)
toshe.do_work()

print(semos.assets)

# A class attribute changes -> all instances created afterwards change
# Employee.minimum_pay = 25000

# marija = Employee("Marija", "Krstevska", "marija@gmail.com", "1234567891011")
# kristijan = Employee("Kristijan", "Gjorgiev", "kristijan@gmail.com", company=semos, embg="1234567891012")
# jovan = Employee("Jovan", "Jankov", "jovan@gmail.com", "1234567891013")

# semos.make_offer(marija, 50000, "HR")
# semos.make_offer(jovan, 50000, "HR")
# seavus.make_offer(jovan, 50000, "HR")

# Represent objects visually when part of structure
# print(marija.offers)

# obj_serialized = jovan.serialize()

# f = open("test.txt", "w")
# f.write(json.dumps(obj_serialized))
# f.close()
# print([jovan, marija])
# print([semos)

# test = 'first_name'

# test = test.replace("_", " ")
# print(test.title())
# t = ""
# prev = ""
# test = 'first_name'
# for char in test:
#     if char == "i":
#         t += "h"
#     else:
#         t += char
#
# test = t
# print(test)


# deserialization from file

# f = open("test.txt", "r")
# data = f.read()
# data_dictionary = json.loads(data)
#
# print(type(data_dictionary))
# print(data_dictionary)
#
# jovan = Employee(data_dictionary["first_name"],
#     data_dictionary["last_name"],
#     data_dictionary["email"],
#     data_dictionary["embg"])
#
# print(jovan)
#
# f.close()

# alkaloid = Company()
# alkaloid.make_offer()
