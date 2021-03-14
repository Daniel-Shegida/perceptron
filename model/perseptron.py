import numpy as np
import os.path
from functions.sigmoid import sigmoid
from functions.utils import base


class Perceptron:
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
        y = self.activation(np.dot(x, self.weights))
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

    def give_me_an_answer(self, x):  # just a joke function
        question = np.array(x)
        y = self.activation(np.dot(question, self.weights))
        # if y > 0.5:
        #     print("perception answer: ", y)
        #     return "assumption: it's 1"
        # else:
        #     print("perception answer: ", y)
        #     return "assumption: it's not one"
        # print(y,question)
        if y > 0.5:
            return 1
        else:
            return 0

