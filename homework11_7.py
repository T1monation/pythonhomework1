class ComplexNumber:
    def __init__(self, real_num, imag_num):
        self.complex_num = complex(real_num, imag_num)

    def __add__(self, other):
        return self.complex_num + other.complex_num

    def __mul__(self, other):
        return self.complex_num * other.complex_num


a = 2 + 3j
b = 3 - 1j
print(a + b)
print(a * b)
c = ComplexNumber(2, 3)
d = ComplexNumber(3, -1)
print(c.complex_num)
print(d.complex_num)
print(c + d)
print(c * d)
