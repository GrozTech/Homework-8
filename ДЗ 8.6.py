#Продолжить работу над вторым заданием.
# Реализуйте механизм валидации вводимых пользователем данных. Например,
# для указания количества принтеров, отправленных на склад, нельзя
# использовать строковый тип данных.


class Sklad:
    def __init__(self):
        self._dict = {}

    def add_to(self, equipment):
        ''' добавляем в словарь обьект по его названию, в значении
        будет список экземпляров этого оборудования'''
        self._dict.setdefault(equipment.group_name(), []).append(equipment)

    def extract(self, name):
        ''' извлекаем из значения обьект по названию группы.
        дальше можно расширить поиск по серии, марки или еще чему либо'''
        if self._dict[name]:
            self._dict.setdefault(name).pop(0)


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

    def action(self):
        return 'Печатает'


class Scaner(Equipment):
    def __init__(self, name, make, year):
        super().__init__(name, make, year)

    def action(self):
        return 'Сканирует'


class Xerox(Equipment):
    def __init__(self, name, make, year):
        super().__init__(name, make, year)

    def action(self):
        return 'Копирует'


sklad = Sklad()
scaner = Scaner('hp', '2400', 2019)
sklad.add_to(scaner)
xerox = Xerox('Xerox', 'B205', 2019)
sklad.add_to(xerox)
printer = Printer('e-320', 'sony', 126, 2018)
sklad.add_to(printer)
print(sklad._dict)
# забираем со склада и выводим склад
sklad.extract('Printer')
print(sklad._dict)