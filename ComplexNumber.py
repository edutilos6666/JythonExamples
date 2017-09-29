import math

class ComplexNumber:
    def __init__(self, re=0 , im = 0):
        self.re = re
        self.im = im


    def __add__(self, other):
        ret = ComplexNumber()
        ret.re = self.re + other.re
        ret.im = self.im + other.im
        return ret


    def __sub__(self, other):
        ret = ComplexNumber()
        ret.re = self.re - other.re
        ret.im = self.im - other.im
        return ret

    def __mul__(self, other):
        ret = ComplexNumber()
        ret.re = self.re*other.re - self.im*other.im
        ret.im = self.re*other.im + self.im*other.re
        return ret

    def multiply_by_factor(self, factor= 1.0):
        ret = ComplexNumber()
        ret.re = self.re * factor
        ret.im = self.im * factor
        return ret

    def divide_by_factor(self, factor = 1.0):
        ret = ComplexNumber()
        ret.re = self.re / factor
        ret.im = self.im / factor
        return ret

    # that is not ok for python 2.7 , but ok for python 3.5 
    # def __rtruediv__(self, other):
    #     factor = math.pow(other.re , 2) + math.pow(other.im , 2)
    #     temp1 = ComplexNumber(other.re , -other.im)
    #     ret = self*temp1
    #     ret = ret.divide_by_factor(factor)
    #     return ret

    def __div__(self, other):
        factor = math.pow(other.re , 2) + math.pow(other.im , 2)
        temp1 = ComplexNumber(other.re , -other.im)
        ret = self*temp1
        ret = ret.divide_by_factor(factor)
        return ret

    def __repr__(self):
        str = "{0} + i*({1})".format(self.re, self.im)
        return str
