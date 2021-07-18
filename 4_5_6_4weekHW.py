class Error(Exception):
    """Класс исключение"""
    def __init__(self, txt):
        self.txt = txt

class Storage:
    # Класс Склад
    def __init__(self, adress, size=0):
        self.adress = adress
        self.size = size
        self.pos = 1  # порядковый номер следующего добавляемого оборудования - сквозной не зависит от департамента
        self.dep = []
        self.dep.append('system')  # добавим системный департамент, на случай, чтобы легко было отказаться от использования департаментов, при этом логика программы остается под работу склада с департаментами
        self.store = {}

    def add_dep(self, depart):
        # проверить нет ли уже этого департамента
        self.dep.__add__(depart)

    def del_dep(self, depart):
        # проверить есть ли этот департамент
        self.dep.remove(depart)

    def input_eq(self, equipment, dep='system'):
        qty = input(f"Введите количество оргтехники {equipment.name}, {equipment.brand}, перемещаемой на склад -> ")
        try:
            if qty.isdigit():
                qty = int(qty)
                for i in range(qty):
                    kort = (self.pos, dep)
                    self.store[kort] = equipment
                    self.pos += 1
            else:
                raise Error("Вы ввели не число, повторите ввод!")
        except Error as err:
            print(err)
        else:
            print(f'Оборудование успешно добавлено на склад в департамент {dep}')

    def show(self):
        for el in self.store.items():
            print(el[0], el[1])
            # el[1].show()


class Equip:
    # Класс Оргтехники
    def __init__(self, name, brand, width, height, lenght, price):
        self.name = name
        self.brand = brand
        self.width = width
        self.height = height
        self.lenght = lenght
        self.price = price

    def show(self):
        print(f'Оргтехника {self.name}')
        print(f'Марка {self.brand}')
        print(f'Ширина: {self.width}')
        print(f'Высота: {self.height}')
        print(f'Глубина: {self.lenght}')
        print(f'Цена (руб): {self.price}')


class PrinterEquip(Equip):
    # Класс принтер
    def __init__(self, name, brand, width, height, lenght, price):
        super().__init__(name, brand, width, height, lenght, price)
        self.purpose = 'Printing'


class ScanerEquip(Equip):
    # Класс сканер
    def __init__(self, name, brand, width, height, lenght, price):
        super().__init__(name, brand, width, height, lenght, price)
        self.purpose = 'Scanning'


class XeroxEquip(Equip):
    # Класс копир
    def __init__(self, name, brand, width, height, lenght, price):
        super().__init__(name, brand, width, height, lenght, price)
        self.purpose = 'Coping'


printer = PrinterEquip('принтер', 'Epson', 250, 300, 450, 2500)
# print(printer.brand)
storage = Storage("ул. Семашек, 42")
storage.input_eq(printer)
scaner = ScanerEquip('сканер', 'Samsung', 250, 300, 450, 1500)
storage.input_eq(scaner)
xerox = XeroxEquip('ксерокс', 'Xerox', 250, 300, 450, 1500)
storage.input_eq(xerox)
storage.show()