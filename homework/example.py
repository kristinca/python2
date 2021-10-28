from Company import Company
from Employee import Employee


marija = Employee("Marija", "Krstevska", "marija343", None, None, None)
semos = Company("semos","K.J.Pitu 1000",1234)

print(marija.salary)
semos.hire(marija,"HR","50000")
print(marija.salary)
semos.fire(marija,"HR")
print(marija.salary)