class Error(Exception):
    # Класс исключение
    def __init__(self, txt):
        self.txt = txt

lst = []
cnt = 1
val = input(f"Ведите число # {cnt}: ")

while val != "stop":
    try:
        if val.isdigit():
            val = int(val)
            lst.append(val)
            print(lst)
            cnt += 1
        else:
            raise Error("ввели не число: ")
    except Error as err:
        print(err)
    else:
        print("Все хорошо. вы ввели число!")

    val = input(f"Ведите число # {cnt}: ")
