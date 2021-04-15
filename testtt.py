import numpy as np
import os.path
import matplotlib.pyplot as plt
import math

from data_downloaders.mnist_data import get_mnist_data
from functions.sigmoid import sigmoid
from functions.utils import base, normal_list
from graphics.presentator import show


class Kohonen_perceptron:
    def __init__(self, inputs=1, name='blank'):
        """добавление в класс имя файла, в который будут сохранены веса"""
        self.fileName = name
        """ Инициализация весов, если веса есть, используем их, иначе рандомим"""
        if os.path.exists(self.fileName):
            self.weights = np.loadtxt(self.fileName)
        else:
            self.weights = np.random.rand(inputs)
            # randiv = []
            # for i in range(inputs):
            #     randiv.append( np.random.uniform((0.5 - 1 / (math.sqrt(inputs))), (0.5 + 1 / (math.sqrt(inputs)))))
            # self.weights =  np.asarray(randiv)
            np.savetxt(self.fileName, self.weights, fmt='%1.4f')

    def activation(self, x):
        distance = 0
        for i in range(len(x)):
            distance += (x[i] - self.weights[i]) ** 2
        return math.sqrt(distance)

    def test_train(self, input_data, rate):
        self.weights += (input_data - self.weights) * rate

    def save_weights(self):
        np.savetxt(self.fileName, self.weights, fmt='%1.4f')


class Kohonen_neironet():
    def __init__(self, X, size):
        self.net = []
        for i in range(size):
            self.net.append(Kohonen_perceptron(inputs=X, name= str(i)))

    def acceleration(self,X,education_rate):
        for j in range(3000):
            education_element = normal_list(X[j])
            for i in range(len(self.net)):
                self.net[i].test_train(education_element, education_rate)



    def train(self, education_data, education_rate, decrease_value, epochs=1):
        while education_rate > 0:
            for i in range(epochs):
                for j in range(len(education_data)):
                #for j in range(3000):
                    education_element = normal_list(education_data[j])
                    print("progress is {} in {}".format(j, len(education_data)))
                    id, min = self.predict(education_element)
                    self.net[id].test_train(education_element, education_rate)
            education_rate -= decrease_value
        self.save_net()

    def predict(self, X):
        min = 99999
        id = 0
        for k in range(len(self.net)):
            prediction = self.net[k].activation(X)
            if prediction < min:
                id = k
                min = prediction
        return id, min

    def save_net(self):
        for i in range(len(self.net)):
            self.net[i].save_weights()


X, Y = get_mnist_data()
neironet = Kohonen_neironet(len(X[0]), 10)
#neironet.acceleration(X,0.3)
#neironet.train(X, 0.1, 3)

list = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
size2 = 1000
for i in range(size2):
    data_set = normal_list(X[i])
    qq = neironet.predict(data_set)
    list[qq[0]][Y[i]] += 1
    print("progress is {} in {}".format(i, size2))

prost = [0,1,2,3,4,5,6,7,8,9]
for i in range(10):
    plt.bar(prost,list[i])
    plt.show()