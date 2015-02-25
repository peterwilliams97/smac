from __future__ import division, print_function
import random

N = 15
L = 10.0
sigma = 0.1
n_configs = 100

for _ in xrange(n_configs):
    x = []
    while len(x) < N:
        x.append(random.uniform(sigma, L - sigma))
        if any(abs(t - x[-1]) < 2.0 * sigma for t in x[:-1]):
            x = []
    print(x)
