from company3 import Company3
from employee3 import Employee3
from offer import Offer
from other_func import employee_serialize_msg, offer_serialize_msg, company_serialize_msg

comp1 = Company3("Company1", "Some address 1", 1234)
# comp2 = Company3("Company2", "Some address 2", 5678)

marija = Employee3("Marija", "Krstevska", "marija@gmail.com", "1234567891011")
kristijan = Employee3("Kristijan", "Gjorgiev", "kristijan@gmail.com", company=comp1,
                      position="HR", embg=1234567891012)
petko = Employee3("Petko", "Petkov", "petko@gmail.com", 1234567891012)

employees = [marija, petko, kristijan]
# print(comp1.__dict__)
# print(marija.__dict__)
# print(kristijan.__dict__)

for e in employees:
    employee_serialize_msg(e)
    e.serialize()

    offer1 = Offer(comp1, e, 50000, 'DR')

    offer_serialize_msg(offer1)
    offer1.serialize()

    employee_serialize_msg(e)
    e.serialize()

    offer1.accept_offer(e)

    company_serialize_msg(comp1)
    comp1.serialize()

    employee_serialize_msg(e)
    e.serialize()
