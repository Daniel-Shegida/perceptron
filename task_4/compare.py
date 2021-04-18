import numpy as np


def compare(G1, X, R):
    if sum(G1) == 0:
        return np.dot(X,R)
    else:
        return np.dot(X,G1)