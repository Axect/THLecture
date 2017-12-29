import numpy as np

def main():
    (a,b) = genVector()
    print(innerProduct(a,b))

def innerProduct(X, Y):
    return X.dot(Y)

def genVector():
    X = np.empty(3)
    Y = np.empty(3)
    for i in range(0, len(X)):
        X[i] = 2*(i+1) - 1
        Y[i] = 2*(i+1)
    return (X,Y)

if __name__ == "__main__":
    main()
