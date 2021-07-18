class MyComplex:
    """класс «Комплексное число»"""
    def __init__(self, real, imag=0):
        self.complex = complex(real, imag)

    def __add__(self, other):
        if isinstance(other, MyComplex):
            other = other.complex

        complex_ = self.complex + other
        return MyComplex(complex_.real, int(complex_.imag))

    def __mul__(self, other):
        if isinstance(other, MyComplex):
            other = other.complex

        complex_ = self.complex * other
        return MyComplex(complex_.real, int(complex_.imag))

    def __str__(self):
        return self.complex.__str__()


if __name__ == '__main__':
    c1 = MyComplex(2, -3)
    c2 = MyComplex(5)

    print(c1 + c2, complex(2, -3) + complex(5))
    print(c1 * c2, complex(2, -3) * complex(5))
