import numpy as np

def get_test_data():
    x = np.array([[0, 0, 1, 0, 0,
                   0, 1, 1, 0, 0,
                   1, 0, 1, 0, 0,
                   0, 0, 1, 0, 0,
                   0, 0, 1, 0, 0,
                   0, 0, 1, 0, 0,
                   1, 1, 1, 1, 1],

                  [0, 0, 0, 1, 0,
                   0, 0, 1, 1, 0,
                   0, 1, 0, 1, 0,
                   0, 0, 0, 1, 0,
                   0, 0, 0, 1, 0,
                   0, 0, 0, 1, 0,
                   1, 1, 1, 1, 1],

                  [1, 1, 1, 1, 1,
                   1, 0, 0, 0, 0,
                   1, 0, 0, 0, 0,
                   1, 1, 1, 1, 1,
                   0, 0, 0, 0, 1,
                   0, 0, 0, 0, 1,
                   1, 1, 1, 1, 1],

                  [1, 1, 1, 1, 1,
                   1, 0, 0, 0, 1,
                   1, 0, 0, 0, 1,
                   1, 1, 1, 1, 1,
                   1, 0, 0, 0, 1,
                   1, 0, 0, 0, 1,
                   1, 1, 1, 1, 1],

                  [1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1,
                   1, 1, 1, 1, 1]])

    y = np.array([[1],
                        [1],
                        [0],
                        [0],
                        [0]])
    return x,y