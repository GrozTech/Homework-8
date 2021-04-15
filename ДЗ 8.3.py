#  Создайте собственный класс-исключение, который должен проверять содержимое списка
#  на наличие только чисел. Проверить работу исключения на реальном примере.
#  Необходимо запрашивать у пользователя данные и заполнять список.
#  Класс-исключение должен контролировать типы данных элементов списка


class Exception:
    def __init__(self, *args):
        self.list = []

    def input(self):

        while True:
            try:
                number = int(input('Введите число  - '))
                self.list.append(number)
                print(f'Текущий список - {self.list} \n ')
            except:
                print(f"Это не число")
                y_or_n = input(f'Попробовать еще раз? Y/N ')

                if y_or_n == 'Y' or y_or_n == 'y':
                    print(try_except.input())
                elif y_or_n == 'N' or y_or_n == 'n':
                    return f'Вы вышли'
                else:
                    return f'Вы вышли'

try_except = Exception(1)
print(try_except.input())