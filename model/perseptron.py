import numpy as np
import os.path
from functions.sigmoid import sigmoid
from functions.utils import base


class Perceptron:
    def __init__(self, inputs=1, name='blank', activ_fun=sigmoid, train_fun=base):
        self.fileName = name
        self.activation = activ_fun
        self.training = train_fun
        """ Инициализация весов, если веса есть, используем их, иначе рандомим"""
        if os.path.exists(self.fileName):
            self.weights = np.loadtxt(self.fileName)
        else:
            self.weights = 2 * np.random.rand(inputs).T - 1  # Веса, -1 > w < 1
            np.savetxt(self.fileName, self.weights, fmt='%1.4f')

    def predict(self, x):
        """ Предсказание сети(пропускаем данные через синусоиду) """
        y = self.activation(np.dot(x, self.weights))
        return y

    def train(self, x_list, y_list, epochs=1, lr=1):
        """ Обучаем наш перцептрон """
        print(self.weights)
        for i in range(epochs):
            for j in range(len(x_list)):
                x = np.array(x_list[j])
                y = y_list[j]

                y_predict = self.predict(x)
                y = self.training(y)
                err = (y - y_predict)

                self.weights += x * (err * lr)

                print("\rEpoch #{} - error: {}".format(i + 1, err, 3))
        np.savetxt(self.fileName, self.weights, fmt='%1.4f')
        print("Total - error: {} ".format(err, 3))

    def give_me_an_answer(self, x):  # just a joke function
        question = np.array(x)
        y = self.activation(np.dot(question, self.weights))
        if y > 0.9:
            print("perception answer: ", y)
            return "assumption: it's 1"
        else:
            print("perception answer: ", y)
            return "assumption: it's not one"
