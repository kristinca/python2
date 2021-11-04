# # # Lists
# # # Slicing
# #
# #
# # nums = [i for i in range(1, 110, 10)]
# # print(f'nums = {nums}\nnums[0:5] = {nums[0:5]}\nnums[0:5:2] = {nums[0:5:2]}\n')
# #
# #
# # # sets
# #
# # def print_set_ind(set1, indeks):
# #     j = 0
# #     for i in set1:
# #         if j == indeks:
# #             print(i)
# #         else:
# #             j += 1
# #
# #
# # def get_set_ind(set1, ind1):
# #     j = 0
# #     for i in set1:
# #         if j == ind1:
# #             return i
# #         else:
# #             j += 1
# #
# #
# # n = {'a', 'b', 'c', 'd', 'e'}
# #
# # print_set_ind(n, 4)
# #
# #
# # def msginfo():
# #     print('not a name and surname input')
# #
# #
# # def print_name(name, surname):
# #     if isinstance(name, str) and isinstance(surname, str):
# #         print(f"Name: {name.title()}, Surname: {surname.title()}")
# #     else:
# #         msginfo()
# #
# #
# # def print_name_from_set(set2):
# #     if len(set2) == 2:
# #         print(f"Name: {get_set_ind(set2,0).title()}, Surname: {get_set_ind(set2,1).title()}")
# #     else:
# #         msginfo()
# #
# #
# # lista1 = [['name1', 'surname1'], 4, ['name2', 4], 'name', ('name2', 'surname2'), {'name3', 'surNAME3'}, {3}, (3, 'name')]
# #
# #
# # def print_name_surname_from_list(list2):
# #     j = 0
# #     for el in list2:
# #         try:
# #             j += 1
# #             print(f'Element No.{j}:\t')
# #             if isinstance(el, list) or isinstance(el, tuple):
# #                 for i in range(len(el) - 1):
# #                     print_name(el[i], el[i + 1])
# #             elif isinstance(el, set):
# #                 print_name_from_set(el)
# #             else:
# #                 msginfo()
# #         except TypeError:
# #             msginfo()
# #
# #
# # print_name_surname_from_list(lista1)
#
# class Company:
#     def hire(self, employee, position, salary):
#         if employee.company:
#             raise Exception(f"{employee} can not be hired, is already working at {employee.company}")
#         print(f"{self.name} is hiring {employee}")
#         employee.company = self
#         employee.position = position
#         employee.salary = salary
#         self.employee_list.append(employee)
#
#     def fire(self, employee):
#         if not employee.company:
#             raise Exception(f"{employee} can't be fired, not employed in a company")
#         elif employee.company.company_id != self.company_id:
#             raise Exception(f"can't fire {employee} from {self.name}, employee is working at {employee.company}")
#         employee.company = None
#         employee.position = None
#         employee.salary = None
#         print(f"{employee} was fired from {self.name}")
#         self.employee_list.remove(employee)
#
#     def get_salary_costs(self):
#         total_salary_costs = 0
#         for emp in self.employee_list:
#             total_salary_costs += employee.salary
#         return total_salary_costs
#
#
# class Employee:
#     def full_name(self):
#         full_name = f"{self.first_name} - {self.last_name}"
#         return full_name
#
#     def __str__(self):
#         return self.full_name()
#
#
#
# semos = Company()
# seavus = Company()
#
# # print(semos)
# # print(type(semos))
# # print(isinstance(semos, Company))
#
# marija = Employee()
# viktor = Employee()
# jovan = Employee()
#
# semos.name = "Semos DOO"
# semos.address = "Kuzman Josifovski Pitu br.1000"
# semos.company_id = "1234"
# semos.employee_list = []
# #
# # print(semos.address)
# # print(semos.address)
# # print(semos.company_id)
#
# seavus.name = "Seavus AD"
# seavus.address = "Boris Trajkovski br.60"
# seavus.company_id = 5678
# seavus.employee_list = []
# #
# marija.first_name = "Marija"
# marija.last_name = "Krstevska"
# marija.email = None
# marija.position = None
# marija.company = None
# #
# # # print(marija.company.name)
# #
# # viktor.first_name = "Krisijan"
# # viktor.last_name = "kristijan@gmail.com"
# # viktor.salary = "50000"
# # viktor.position = "Software Developer"
# # viktor.company = semos
#
# jovan.first_name = "Jovan"
# jovan.last_name = "Jankov"
# jovan.salary = None
# jovan.position = None
# jovan.company = None
#
# # # print(semos.__dict__)
# # semos.hire(jovan, "HR", "40000")
# # print(jovan.company)
# #
# # print(jovan.__str__())
#
# # semos.hire(jovan, "Developer", '50000')
# semos.hire(marija, "dev", 50000)
# semos.hire(jovan, "dev", 30000)
#
# for employee in semos.employee_list:
#     print(employee)
#
# print(semos.get_salary_costs())

# Custum Types/Classes by default create mutable objects
class Company:
    pass

company_1 = Company()
company_2 = company_1
company_1.name = 'semos'
print(company_1.name)
print(company_2.name)

# every object instantiated from a class is a DISTINCT OBJECT

# id (<object>) returns the memory address alocated for the object

a = 2
b = a

b = 10
# when immutable objects are in question, changing the value allocates new memory address

print(a,b)
print(id(a),id(b))

print(id(company_1))
print(id(company_2))


class Employee:
    minimum_pay = 15000

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
        self.salary = salary
        self.email = email
        self.position = position
        self.company = company
        self.embg = self.validate_embg(embg)

    @staticmethod
    def validate_embg(embg):
        if len(str(embg)) != 13:
            raise Exception(f'Invalid input of embg.')
        else:
            return embg

    def full_name(self):
        full_name = f"{self.first_name} - {self.last_name}"
        return full_name

    def __str__(self):
        return self.full_name()


class Company:

    def __init__(self, name, address, company_id):
        self.name = name
        self.address = address
        self.company_id = company_id
        self.employee_list = []

    def hire(self, employee, position, salary):
        if salary < Employee.minimum_pay:
            raise Exception(f"Salary provided under min wage of {Employee.minimum_pay}")

        if employee.company:
            raise Exception(f"{employee} can not be hired, is already working at {employee.company}")
        print(f"{self.name} is hiring {employee}")
        employee.company = self
        employee.position = position
        employee.salary = salary
        self.employee_list.append(employee)

    def fire(self, employee):
        if not employee.company:
            raise Exception(f"{employee} can't be fired, not employed in a company")
        elif employee.company.company_id != self.company_id:
            raise Exception(f"can't fire {employee} from {self.name}, employee is working at {employee.company}")
        employee.company = None
        employee.position = None
        employee.salary = None
        print(f"{employee} was fired from {self.name}")
        self.employee_list.remove(employee)

    def get_salary_costs(self):
        total_salary_costs = 0
        for emp in self.employee_list:
            total_salary_costs += emp.salary
        return total_salary_costs



semos = Company("Semos DOO", "Kuzman Josifovski Pitu br.1000", "1234")


# print(semos)
# print(type(semos))
# print(isinstance(semos, Company))

print(semos.name,semos.address,semos.company_id)

marija = Employee("Marija","Krstevska",'marija@email.com', '1234567891011', None, None,None)
viktor = Employee("Viktor", 'Gjorgiev', "viktor@gmail.com", 1234567891012, None, None,None)
jovan = Employee("Jovan", "Jankov", "jovan@email.com", 1234567891013, None, None, None)

seavus = Company("Seavus AD", "Boris Trajkovski br.60", 5678)

print(marija)

# to delete an obj we use the del obj_name
# del semos
Employee.minimum_pay=25000
print(marija.minimum_pay)

# Tight Coupling between components -> DO NOT DO IT!!!

# constants are written with CAPS_LOCK !!!!
# -> PASSWORD, USER, ....