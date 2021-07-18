
class Error(Exception):
    # Класс исключения
    def __init__(self, txt):
        self.txt = txt
    pass
try:
    inp_data_1 = int(input("Введите число делимое: "))
    inp_data_2 = int(input("Введите число делитель: "))
    if inp_data_2 == 0:
        raise Error("деление на 0 запрещено!")
except ValueError:
    print("проверьте ввод числа")
except Error as err:
    print(err)
else:
    print(f'результат: {inp_data_1 // inp_data_2}')
