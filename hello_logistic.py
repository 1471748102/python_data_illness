# import math
import numpy as np
K = 10000
P0 = 1000
r = 0.2


def logistic(t):
    exp_r = np.exp(r * t)
    return K * P0 * exp_r / (K + P0 * (exp_r - 1))


t1 = np.array([1, 2, 3])
p1 = logistic(t1)
print(p1)