def nasterisk(n):
    """ A function that returns n asterisks """
    return (int(n) * '*')


def print_str_w_nasterisk(string1):
    print('\n'+nasterisk(len(string1)+1)+'\n'+string1+'\n'+nasterisk(len(string1)+1))


def employee_serialize_msg(emp):
    s1 = f'  Employee {emp.first_name} serialization: '
    print_str_w_nasterisk(s1)


def offer_serialize_msg(offer):
    s2 = f'  Offer {offer.position} from the company {offer.company.name} ' \
         f'to the employee {offer.employee.first_name} serialization: '
    print_str_w_nasterisk(s2)


def company_serialize_msg(comp):
    s1 = f'  Company {comp.name} serialization: '
    print_str_w_nasterisk(s1)
