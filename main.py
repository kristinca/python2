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


n = {'a', 'b', 'c', 'd', 'e'}

print_set_ind(n, 4)


def msginfo():
    print('not a name and surname input')


def print_name(name, surname):
    try:
        if isinstance(name, str) and isinstance(surname, str):
            print(f"Name: {name.title()}, Surname: {surname.title()}")
        else:
            print('error')
    except TypeError:
        msginfo()


lista1 = [['name1', 'surname1'], 4, ['name2', 4], 'name']

for el in lista1:
    try:
        if isinstance(el, list):
            for i in range(len(el) - 1):
                print_name(el[i], el[i + 1])
        else:
            msginfo()
    except TypeError:
        msginfo()
