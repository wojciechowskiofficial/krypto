import sympy
import numpy as np

class BBS:
    def __init__(self, seed):
        # x_i = x_(i-1) ** 2 % N
        self.seed = seed
        self.N = 832943 * 926819
        x = self.seed
        while True:
            if np.gcd(x, self.N) == 1:
                break
            else:
                print(np.gcd(x, self.N))
                x += 1
        self.x_0 = x ** 2 % self.N
        print(x, self.N, self.x_0)
    def __iter__(self):
        return self
    def __next__(self):
        self.x_0 = self.x_0 ** 2 % self.N
        return self.x_0
