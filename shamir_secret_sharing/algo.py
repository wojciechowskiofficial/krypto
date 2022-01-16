import numpy as np
import sympy

class Encoder:
    def __init__(self, t, n, s):
        self.t = t
        self.n = n
        self.s = s
    def _randomize_constants(self):
        lower_bound_p = max(self.s, self.n) + 1
        self.p = sympy.randprime(lower_bound_p, sympy.nextprime(lower_bound_p, ith=5))
        self.a = [np.random.randint(0, lower_bound_p) for i in range(self.t - 1)]
        # a vector from now on contains s as a_0
        # at the end of the vector
        # [a_(t-1), a_(t-2), ..., a_0]
        self.a.append(self.s)
    def encode(self):
        self._randomize_constants()
        self.poly = np.poly1d(self.a)
        return ([(i, self.poly(i) % self.p) for i in range(1, self.n + 1, 1)], self.p)

class Decoder:
    def __init__(self, shares, p):
        self.shares = shares
        self.t = len(shares)
        self.p = p
    def _mod(self, a, b):
        if a < 0 and abs(a) > b:
            return np.fmod(a, b)
        else:
            return a % b
    def decode(self):
        self.basis_polynomials = list()
        for i in range(self.t):
            l_i = np.poly1d([1])
            for j in range(self.t):
                if i == j:
                    continue
                l_i *= np.poly1d([1, -self.shares[j][0]])
                l_i /= self.shares[i][0] - self.shares[j][0]
                # print(l_i)
            # print('new')
            l_i *= self.shares[i][1]
            # print('y', self.shares[i][1])
            # print(l_i)
            #l_i = np.poly1d([self._mod(coeff, self.p) for coeff in list(l_i)])
            # print(l_i)
            # print('end')
            self.basis_polynomials.append(l_i)
        return sum([list(l)[-1] for l in self.basis_polynomials]) % self.p
