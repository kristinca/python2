# Lists
# Slicing


nums = [i for i in range(1, 110, 10)]
print(f'nums = {nums}\nnums[0:5] = {nums[0:5]}\nnums[0:5:2] = {nums[0:5:2]}\n')


# sets

def print_set_ind(set1, indeks):
    j = 0
    for i in set1:
        if j == indeks:
            print(i)
        else:
            j += 1


def get_set_ind(set1, ind1):
    j = 0
    for i in set1:
        if j == ind1:
            return i
        else:
            j += 1


n = {'a', 'b', 'c', 'd', 'e'}

print_set_ind(n, 4)


def msginfo():
    print('not a name and surname input')


def print_name(name, surname):
    if isinstance(name, str) and isinstance(surname, str):
        print(f"Name: {name.title()}, Surname: {surname.title()}")
    else:
        msginfo()


def print_name_from_set(set2):
    if len(set2) == 2:
        print(f"Name: {get_set_ind(set2,0).title()}, Surname: {get_set_ind(set2,1).title()}")
    else:
        msginfo()


lista1 = [['name1', 'surname1'], 4, ['name2', 4], 'name', ('name2', 'surname2'), {'name3', 'surNAME3'}, {3}, (3, 'name')]


def print_name_surname_from_list(list2):
    j = 0
    for el in list2:
        try:
            j += 1
            print(f'Element No.{j}:\t')
            if isinstance(el, list) or isinstance(el, tuple):
                for i in range(len(el) - 1):
                    print_name(el[i], el[i + 1])
            elif isinstance(el, set):
                print_name_from_set(el)
            else:
                msginfo()
        except TypeError:
            msginfo()


print_name_surname_from_list(lista1)