# Продолжить работу над первым заданием. Разработать методы,
# отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники, а также других данных,
# можно использовать любую подходящую структуру, например словарь.


class Sklad:
    def __init__(self):
        self._dict = {}

    def add_to(self, equipment):
        ''' добавляем в словарь обьект по его названию, в значении
        будет список экземпляров этого оборудования'''
        self._dict.setdefault(equipment.group_name(), []).append(equipment)


class Equipment:
    def __init__(self, name, make, year):
        self.name = name
        self.make = make
        self.year = year
        self.group = self.__class__.__name__

    def group_name(self):
        return f'{self.group}'


    def __repr__(self):
        return f'{self.name} {self.make} {self.year}'


class Printer(Equipment):
    def __init__(self, series, name, make, year):
        super().__init__(name, make, year)
        self.series = series

    def __repr__(self):
        return f'{self.name} {self.series} {self.make} {self.year}'



class Scaner(Equipment):
    def __init__(self, name, make, year):
        super().__init__(name, make, year)



class Xerox(Equipment):
    def __init__(self, name, make, year):
        super().__init__(name, make, year)



sklad = Sklad()
scaner = Scaner('hp', '2400', 2019)
sklad.add_to(scaner)
xerox = Xerox('Xerox', 'B205', 2019)
sklad.add_to(xerox)
printer = Printer('e-320', 'sony', 126, 2018)
sklad.add_to(printer)
print(sklad._dict)