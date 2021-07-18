
class MyDate:
    # Класс Дата
    # дата поступает из внешнего источника  в виде строки в формате 'dd-mm-yyyy'

    DATE = '0-0-0000'
    # DAY, MONTH, YEAR = map(int, DATE.split('-'))

    def __init__(self, d_str):
        # self.date = str_date # атрибут экземляра
        MyDate.DATE = d_str # не знаю использовать ли атрибут класса или атрибут экзмпеляра

    @classmethod
    # Метод класса
    def extract_date(cls):
        day, month, year = map(int, cls.DATE.split('-'))
        # получить день, месяц и год в виде целочисленное значение
        return f'{day}.{month}.{year}'

    @staticmethod
    # Метод статик
    def date_valid(date):
        day, month, year = map(int, date.split('-'))
        if day < 1:
            print("Календарь не может быть меньше 0")
        elif day > 31:
            print("Календарный день не может быть больше 31")
        if year < 0:
            print("Год не может быть меньше 0")


date2 = MyDate('11-09-2012')
d = MyDate.extract_date()
print(d)
MyDate.date_valid('11-09-2012')






#def display(self):
#    return "{0}-{1}-{2}".format(self.month, self.day, self.year)
# в явном виде return day, month, year




