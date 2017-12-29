from numpy import sin, cos, pi

def main():
    print(sin(pi))
    print(differentiate(sin, pi))
    f = sin
    df = derivative(sin)
    print(df(pi))

    D = Derivative(sin) # Derivative는 Class, D는 Derivative의 Instance.
    print(D(pi))

# Differentiate
def differentiate(f, x):
    h = 1e-06
    return (f(x+h)-f(x)) / h

def derivative(f):
    def diff(x):
        return differentiate(f,x)
    return diff

class Derivative:
    def __init__(self, f):
        self.f = f
        self.h = 1e-06

    def differentiate(self, x):
        return (self.f(x+self.h) - self.f(x))/self.h

    def __call__(self, x): # Instance가 x를 받는 함수가 되게 만들어준다.
        return self.differentiate(x)


if __name__ == "__main__":
    main()
