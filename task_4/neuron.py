import os
from random import random

import numpy as np

class Perceptron:
    def __init__(self, id, inputs=1, name='blank', activ_fun=binar):
        self.id = id
        """добавление в класс имя файла, в который будут сохранены веса"""
        self.fileName = name
        """добавление в класс функции, с помощью которой будет анализироватсья входные данные(по умолчаню сигноид)"""
        self.activation = activ_fun
        """ Инициализация весов, если веса есть, используем их, иначе рандомим"""
        if os.path.exists(self.fileName):
            self.weights = np.loadtxt(self.fileName)
        else:
            self.weights = []
            for i in range(inputs):
                self.weights.append(random.uniform(0, (2 / (inputs + 1))))
            np.savetxt(self.fileName, self.weights, fmt='%1.4f')

        self.t_weights = [0 for i in range(8 ** 2)]
        self.b_weights = [0 for i in range(8 ** 2)]

    def get_t(self):
        return self.t

    def calculate_r(self, input_c):
        net = np.dot(self.b, input_c)
        return net

    def learn(self, input_c):
        sum_c = sum(input_c)
        # Обучаем вектор весов T
        self.t_weights = input_c
        for i in range(len(input_c)):
            # Обучаем вектор весов B
            self.b_weights[i] = (2 * input_c[i]) / (2 - 1 + sum_c)
