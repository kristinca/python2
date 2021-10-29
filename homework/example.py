from Company import Company
from Employee import Employee


aname = Employee("Aname", "Alastname", "aname@email.com", None, None, None)
comp1 = Company("Company1", "Some address 1", 1234)
comp2 = Company("Company2", "Some address 2", 5678)


print(aname.company)
comp1.hire(aname, "dr", "500")
comp1.hire(aname, "dr", "700")
comp2.hire(aname, "dr", "600")
print(aname.company)
comp1.fire(aname, "fghcdhfrf")
print(aname.company)
