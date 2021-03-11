import numpy as np

def sigmoid(x): # сигмоид функция, используется как стандартная для персептрона
    return 1 / (1 + np.exp(-x))