# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.


class Sklad:
    def __init__(self):
        self._dict = {}


class Equipment:
    def __init__(self, name, make, year):
        self.name = name
        self.make = make
        self.year = year
        self.group = self.__class__.__name__


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
xerox = Xerox('Xerox', 'B205', 2019)
printer = Printer('e-320', 'sony', 126, 2018)

