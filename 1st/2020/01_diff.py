def main():
    from math import sin, cos, pi
    #print(abs((diff(sin, pi) - cos(pi)) / cos(pi)) * 100)
    #dsin = derivative(sin)
    #print([dsin(2*pi*i/100) for i in range(0, 101)])
    #Dsin = Derivative(sin)
    #print(Dsin.calc(pi))
    #Dsin.set_precision(1e-7)
    #print(Dsin(pi))
    #Dsin = Derivative(sin)
    #Dcos = Derivative(cos)
    #Dsincos = Dsin * Dcos
    #Dsin2 = 2 * Dsin
    #print(Dsincos(pi))
    #print(Dsin2(pi))
    a = Taehyun()
    b = Taegeun()
    quack(a)
    quack(b)

def diff(f, x, h=1e-6):
    return (f(x+h) - f(x)) / h

# Higher Order Function
def derivative(f):
    return lambda x: diff(f,x)

class Taehyun:
    def __init__(self):
        pass
    def quack(self):
        print("quack")

class Taegeun:
    def __init__(self):
        pass
    def quack(self):
        print("quark")

def quack(x):
    x.quack()

# Object Oriented
class Derivative:
    def __init__(self, f):
        self.f = f
        self.h = 1e-6

    def calc(self, x):
        return diff(self.f, x, self.h)

    def set_precision(self, h):
        self.h = h

    def __call__(self, x):
        return self.calc(x)

    def __add__(self, other):
        return Derivative(lambda x: self.f(x) + other.f(x))

    def __mul__(self, other):
        return Derivative(lambda x: self.f(x) * other.f(x))

    def __rmul__(self, number):
        return Derivative(lambda x: number * self.f(x))

if __name__ == "__main__":
    main()
