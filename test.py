import os
from random import random

from mnist.loader import np

from functions.binar import binar


class Perceptron:
    def __init__(self, id, inputs=1,  name='blank', activ_fun=binar):
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
                self.weights.append(random.uniform(0, (2/(inputs+1))))
            np.savetxt(self.fileName, self.weights, fmt='%1.4f')

    def predict(self, x):
        """ Предсказание сети(пропускаем данные через функцию в self.activation) """
        y = self.activation(np.dot(x, self.weights))
        return y




class Kohonen_neironet():
    def __init__(self, X, size):
        self.net = []
        for i in range(size):
            self.net.append(Kohonen_perceptron(inputs=X, name=str(i)))

    def acceleration(self, X, education_rate):
        for j in range(3000):
            education_element = normal_list(X[j])
            for i in range(len(self.net)):
                self.net[i].test_train(education_element, education_rate)

    def train(self, education_data, education_rate, decrease_value, epochs=1):
        while education_rate > 0:
            for i in range(epochs):
                for j in range(len(education_data)):
                    # for j in range(3000):
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


class G2():
    def __init__(self, size):
        self.size = size

    def give(self, X):
        y = []
        if (sum(X) == 1):
            for i in range(self.size):
                y.append(1)
            return y
        else:
            for i in range(self.size):
                y.append(0)
            return y


class G1():
    def __init__(self, size):
        self.size = size

    def give(self, X, R):
        y = []
        if (sum(X) == 1 and sum(R) != 1):
            for i in range(self.size):
                y.append(1)
            return y
        else:
            for i in range(self.size):
                y.append(0)
            return y

class reseter():
    def __init__(self, limit):
        self.limit = limit

    def compare(self,X,C):
        if (sum(X)/sum(C) >= self.limit):
            return 0
        else:
            return 1


class compare_net():
    def __init__(self,size):
        self.id = 0
        self.net = []
        self.size - size
        for i in range(size):
            self.net.append(1)
    
    def compare(self,G1,X,R):
        test = G1 + X + R * self.net
        test2 = []
        for i in range(self.size):
            if(test[i] == 2):
                test2.append(1)
            else: test2.append(0)


class recognition_net():
    def __init__(self,size):
        self.id = 0
        self.size = size
        self.net = []
    def add_neiron(self):
        self.net.append(Perceptron(len(self.net),inputs=self.size))