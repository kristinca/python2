from company3 import Company3
from employee3 import Employee3
from offer import Offer


comp1 = Company3("Company1", "Some address 1", 1234)
# comp2 = Company3("Company2", "Some address 2", 5678)

marija = Employee3("Marija", "Krstevska", "marija@gmail.com", "1234567891011")
kristijan = Employee3("Kristijan", "Gjorgiev", "kristijan@gmail.com", company=comp1,
                      position="HR", embg=1234567891012)

employees = [marija, kristijan]

print(comp1.__dict__)
print(marija.__dict__)
print(kristijan.__dict__)


for e in employees:
    print(f'employee {e.first_name} serialization:')
    e.serialize()

    offer1 = Offer(comp1, e, 50000, 'dr')
    print(f'\noffer {offer1.position} from the company {offer1.company.name} '
          f'to the employee {offer1.employee.first_name} serialization:')
    offer1.serialize()

    e.serialize()

    offer1.receive_offer(e)

    offer1.accept_offer(e, comp1)

    e.serialize()
