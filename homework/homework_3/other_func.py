def nasterisk(n):
    """ A function that returns n asterisks """

    return (int(n) * '*')


def employee_serialize_msg(emp):
    s1 = f'  Employee {emp.first_name} serialization: '
    print('\n'+nasterisk(len(s1)+1)+'\n'+s1+'\n'+nasterisk(len(s1)+1))


def offer_serialize_msg(offer):
    s2 = f'  Offer {offer.position} from the company {offer.company.name} ' \
         f'to the employee {offer.employee.first_name} serialization: '

    print('\n'+nasterisk(len(s2)+1)+'\n'+s2+'\n'+nasterisk(len(s2)+1))


def company_serialize_msg(comp):
    s1 = f'  Company {comp.name} serialization: '
    print('\n'+nasterisk(len(s1)+1)+'\n'+s1+'\n'+nasterisk(len(s1)+1))
