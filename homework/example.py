from Company2 import Company2
from Employee2 import Employee2


aname = Employee2("Aname", "Alastname", "aname@email.com", 0, None, None)
comp1 = Company2("Company1", "Some address 1", 1234)
comp2 = Company2("Company2", "Some address 2", 5678)


print(aname.company)
comp1.hire(aname, "dr", 50000)
# comp1.hire(aname, "dr", 70000)
# comp2.hire(aname, "dr", 60000)
# print(aname.company)
# comp1.fire(aname)
# print(aname.company)
# print(aname.company.months_notice)
aname.quit()
print(aname.company, aname.salary, aname.position)