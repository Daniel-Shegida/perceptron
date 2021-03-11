import numpy as np

def binar(x): # простая пороговая функция, если х превышает некоторое значение(35), выдает единицу
    if np.sum(x) > 35:
        return 1
    else:
        return 0