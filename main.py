# # Lists
# # Slicing
#
#
# nums = [i for i in range(1, 110, 10)]
# print(f'nums = {nums}\nnums[0:5] = {nums[0:5]}\nnums[0:5:2] = {nums[0:5:2]}\n')
#
#
# # sets
#
# def print_set_ind(set1, indeks):
#     j = 0
#     for i in set1:
#         if j == indeks:
#             print(i)
#         else:
#             j += 1
#
#
# def get_set_ind(set1, ind1):
#     j = 0
#     for i in set1:
#         if j == ind1:
#             return i
#         else:
#             j += 1
#
#
# n = {'a', 'b', 'c', 'd', 'e'}
#
# print_set_ind(n, 4)
#
#
# def msginfo():
#     print('not a name and surname input')
#
#
# def print_name(name, surname):
#     if isinstance(name, str) and isinstance(surname, str):
#         print(f"Name: {name.title()}, Surname: {surname.title()}")
#     else:
#         msginfo()
#
#
# def print_name_from_set(set2):
#     if len(set2) == 2:
#         print(f"Name: {get_set_ind(set2,0).title()}, Surname: {get_set_ind(set2,1).title()}")
#     else:
#         msginfo()
#
#
# lista1 = [['name1', 'surname1'], 4, ['name2', 4], 'name', ('name2', 'surname2'), {'name3', 'surNAME3'}, {3}, (3, 'name')]
#
#
# def print_name_surname_from_list(list2):
#     j = 0
#     for el in list2:
#         try:
#             j += 1
#             print(f'Element No.{j}:\t')
#             if isinstance(el, list) or isinstance(el, tuple):
#                 for i in range(len(el) - 1):
#                     print_name(el[i], el[i + 1])
#             elif isinstance(el, set):
#                 print_name_from_set(el)
#             else:
#                 msginfo()
#         except TypeError:
#             msginfo()
#
#
# print_name_surname_from_list(lista1)

class Company:
    def hire(self, employee, position, salary):
        employee.company = self
        employee.position = position
        employee.salary = salary


class Employee:
    def full_name(self):
        full_name = f"{self.first_name} - {self.last_name}"
        return full_name

    def __str__(self):
        return self.full_name()



semos = Company()
seavus = Company()

# print(semos)
# print(type(semos))
# print(isinstance(semos, Company))

marija = Employee()
viktor = Employee()
jovan = Employee()

semos.name = "Semos DOO"
semos.address = "Kuzman Josifovski Pitu br.1000"
semos.company_id = "1234"
#
# print(semos.address)
# print(semos.address)
# print(semos.company_id)

seavus.name = "Seavus AD"
seavus.address = "Boris Trajkovski br.60"
seavus.company_id = 5678

marija.first_name = "Marija"
marija.last_name = "Krstevska"
marija.email = "marija@gmail.com"
marija.position = "Software Tester"
marija.company = semos

# print(marija.company.name)

viktor.first_name = "Krisijan"
viktor.last_name = "kristijan@gmail.com"
viktor.salary = "50000"
viktor.position = "Software Developer"
viktor.company = semos

jovan.first_name = "Jovan"
jovan.last_name = "Jankov"
jovan.salary = None
jovan.position = None
jovan.company = None

# print(semos.__dict__)
semos.hire(jovan, "HR", "40000")
print(jovan.company)

print(jovan.__str__())