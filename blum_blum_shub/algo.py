import sympy
import numpy as np

class BBS:
    def __init__(self, seed):
        # x_i = x_(i-1) ** 2 % N
        self.seed = seed
        self.N = 832943 * 926819
        # compute N
        sympy.sieve.extend(1e6)
        primes = np.asarray(sympy.sieve._list)
        # check for prime and 3 congruency modulo 4
        primes = primes[primes % 4 == 3 % 4]
        primes = primes[int(primes.shape[0] * 0.75):]
        print(np.random.choice(primes, 2, replace=False))
        self.N = np.sum(np.random.choice(primes, 2, replace=False))
        x = self.N - 1
        while True:
            if np.gcd(x, self.N) == 1:
                break
            else:
                x -= 1
        print()
