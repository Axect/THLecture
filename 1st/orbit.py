import numpy as np
from matplotlib import pyplot as plt

G = 6.67259e-11
m = 5.9736e+24
M = 1.9891e+30
AU = 1.49597870691e+11
t_step = 0.5 # 43200s
N = 3650*2
pos_1 = np.array([-9.851920196143998E-01*AU, 1.316466809434336E-01*AU, -4.877392224782687E-06*AU])
pos_2 = np.array([-9.864337701483683E-01*AU, 1.230799243164879E-01*AU, -4.374019384763304E-06*AU])

def main():
    (posArray, velArray) = genArray(N+1)
    totalArray = (posArray, velArray)
    vel1 = (pos_2 - pos_1) / t_step
    A = Position(pos_2, vel1)
    print(A)
    for i in range(0, N):
        insertValue(totalArray, A, i)
        A.integrate()
    insertValue(totalArray,A,N)
    print(A)
    plt.figure()
    plt.plot(np.linspace(0,N,N+1), posArray[:,0])
    plt.show()

class Position:
    def __init__(self, pos, vel):
        self.pos = pos
        self.vel = vel
        self.norm = np.sqrt(self.pos[0]**2 + self.pos[1]**2 + self.pos[2]**2)

    def calcAcc(self):
        return -(G*M/(self.norm**3)) * self.pos

    def __str__(self):
        return 'pos: {}\nvel: {}'.format(self.pos, self.vel)

    def integrate(self):
        a = self.calcAcc()
        self.vel += t_step * a
        self.pos += t_step * self.vel

def genArray(n):
    t1 = np.empty([n, 3])
    t2 = np.empty([n, 3])
    return (t1, t2)

def insertValue(tup, Pos, i):
    tup[0][i] = Pos.pos
    tup[1][i] = Pos.vel

if __name__ == "__main__":
    main()

