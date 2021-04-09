import numpy as np
import os.path

from data_downloaders.mnist_data import get_mnist_data
from functions.sigmoid import sigmoid
from functions.utils import base


class Perceptron2:
    def __init__(self, inputs=1, name='blank', activ_fun=sigmoid, train_fun=base):
        """добавление в класс имя файла, в который будут сохранены веса"""
        self.fileName = name
        """добавление в класс функции, с помощью которой будет анализироватсья входные данные(по умолчаню сигноид)"""
        self.activation = activ_fun
        """добавление вспомогательной функции,которая регулирует  входные результатов(по умолчанию без изменений)"""
        self.training = train_fun
        """ Инициализация весов, если веса есть, используем их, иначе рандомим"""
        if os.path.exists(self.fileName):
            self.weights = np.loadtxt(self.fileName)
        else:
            self.weights = 2 * np.random.rand(inputs).T - 1  # Веса, -1 > w < 1
            np.savetxt(self.fileName, self.weights, fmt='%1.4f')

    def predict(self, x):
        """ Предсказание сети(пропускаем данные через функцию в self.activation) """
        # y = self.activation(np.dot(x, self.weights))
        y = sum(self.weights * x)

        return y

    def train(self, x_list, y_list, epochs=1, lr=1):
        """ Обучаем наш перцептрон """
        for i in range(epochs):
            for j in range(len(x_list)):#каждой эпохе обучение идет по всем обучающим данным
                x = np.array(x_list[j])
                y = y_list[j]# и для каждого входного значения есть подготовленный ответ

                y_predict = self.predict(x)
                y = self.training(y)# регулируются входные данные
                err = (y - y_predict) # сравниваются значения между предсказанием и подготовленным ответом

                self.weights += x * (err * lr) #если ошибка ненулевая, проихводятся изменения в весах

                print("\rEpoch #{} - error: {}".format(i + 1, err, 3))
        np.savetxt(self.fileName, self.weights, fmt='%1.4f')# после обучения, веса сохраняются в текстовом файле
        print("Total - error: {} ".format(err, 3))

    def test_train(self, input_data, predict,rate):
        self.weights = (input_data - self.weights) * predict * rate



class neironet():
    def __init__(self,X):
        self.education_rate = 5
        perceptron0 = Perceptron2(inputs=X)
        perceptron1 = Perceptron2(inputs=X)
        perceptron2  = Perceptron2(inputs=X)
        perceptron3 = Perceptron2(inputs=X)
        perceptron4 = Perceptron2(inputs=X)
        perceptron5 = Perceptron2(inputs=X)
        perceptron6 = Perceptron2(inputs=X)
        perceptron7 = Perceptron2(inputs=X)
        perceptron8 = Perceptron2(inputs=X)
        perceptron9 = Perceptron2(inputs=X)
        self.net = [perceptron0,perceptron1,perceptron2,perceptron3,perceptron4,perceptron5,perceptron6,perceptron7,
                   perceptron8,perceptron9]

    def train(self,education_data,epochs):
        for i in range(epochs):
            for j in education_data:
                print("working")
                max = 0
                maxk = 0
                for k in range(len(self.net)):
                    if self.net[k].predict(j) > max:
                        maxk = k
                self.net[maxk].test_train(j,max,self.education_rate)


X,Y = get_mnist_data()
neironet1 = neironet(len(X[0]))
neironet1.train(X,1)