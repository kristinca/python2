class Employee:
    minimum_pay = 15000

    def __init__(
            self,
            first_name,
            last_name,
            email,
            embg,
            salary=None,
            position=None,
            company=None
    ):
        # ._ => pseudo private attribute
        # self._first_name = first_name
        # self._last_name = last_name

        # .__ => private attribute
        self.__first_name = first_name
        self.__last_name = last_name
        self.salary = salary
        self.email = email
        self.position = position
        self.company = company
        self.embg = self.validate_embg(embg)

    # getter
    @property
    def first_name(self):
        return self.__first_name

    # setter
    @first_name.setter
    def first_name(self, value):
        print("IN SETTER "+value)
        if value not in ("Marija", "Milica"):
            raise Exception("Name not valid")
        else:
            self.__first_name = value

    @staticmethod
    def validate_embg(embg):
        if len(str(embg)) != 13:
            raise Exception(f'Invalid input of embg.')
        else:
            return embg

    def full_name(self):
        full_name = f"{self.__first_name} - {self.__last_name}"
        return full_name

    def __str__(self):
        return self.full_name()


marija = Employee("Marija","Krstevska",'marija@email.com', '1234567891011', None, None,None)
print(marija.first_name)

marija.first_name = 'Milica'

print(marija.first_name)