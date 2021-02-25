import numpy as np
import time
import os.path

class Perceptron:
    def __init__(self, inputs=1, name='blank'):
        self.fileName = name
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
                x = x_list[j]
                y = y_list[j]

                y_predict = self.predict(x)

                err = (y - y_predict)

                self.weights += x * (err * lr)

                print("\rEpoch #{} - error: {}".format(i + 1, err, 3))
        np.savetxt(self.fileName, self.weights, fmt='%1.4f')
        print("Total - error: {} ".format(err, 3))

    def activation(self,x):
        """ Функция активации (сигмоида) """
        if np.sum(x) > 35:
            return 1
        else:
            return 0

    def give_me_an_answer(self, x):
        question = np.array(x)
        y = self.activation(np.dot(question, self.weights))
        if y > 0.9:
            return "it's 1"
        else:
            return "it's not one"


if __name__ == '__main__':
    """our data samples"""
    X = np.array([[0, 0, 1, 0, 0,
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

    answers = np.array([[1],
                        [1],
                        [0],
                        [0],
                        [0]])
    file = 'binar.txt'

    perceptron = Perceptron(inputs=35, name=file)

    perceptron.train(X, answers, epochs=1111, lr=.01)

    """ for debugging"""
    # [print(perceptron.predict(np.array(x))) for x in X]
    [print(perceptron.give_me_an_answer(x)) for x in X]
