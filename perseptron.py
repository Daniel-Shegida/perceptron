import numpy as np
import time
import os.path

file = 'file.txt'


class Perceptron():
    def __init__(self, inputs=1, name='blank'):
        self.fileName = name
        """ Инициализация весов, если веса есть, используем их, иначе рандомим"""
        if (os.path.exists(self.fileName)):
            self.weights = np.loadtxt(self.fileName)
        else:
            self.weights = 2 * np.random.rand(inputs).T - 1  # Веса, -1 > w < 1
            np.savetxt(self.fileName, self.weights, fmt='%1.4f')

    def predict(self, x):
        """ Предсказание сети(пропускаем данные через синусоиду) """
        y = self.activation(np.dot(x, self.weights))
        return y

    def train(self, X, Y, epochs=1, lr=1):
        """ Обучаем наш перцептрон """
        T0 = time.time()
        print(self.weights)
        for i in range(epochs):
            t0 = time.time()
            for j in range(len(X)):
                x = X[j]
                y = Y[j]

                y_predict = self.predict(x)

                err = (y - y_predict)
                delta_weight = err * self.activation(y_predict, True)
                print("summ", x * (delta_weight * lr))
                #self.weights += err

                self.weights += x * (delta_weight * lr)

                print(self.weights,'sdo')
                [weight + 1 for weight in self.weights]
                print(self.weights,'after')

                print("\rEpoch #{} - error: {} - time {}sec.".format(i + 1, err, round(t0 - time.time(), 3)))
        np.savetxt(self.fileName, self.weights, fmt='%1.4f')
        print("Total - error: {} - time {}sec.".format(err, round(T0 - time.time(), 3)))

    def activation(self, x, deriv=False):
        """ Функция активации (сигмоида) """
        if deriv:
            return self.activation(x) * (1 - self.activation(x))
        return 1 / (1 + np.exp(-x))

    def give_me_an_answer(self, x):
        question = np.array(x)
        y = self.activation(np.dot(question, self.weights))
        if (y > 0.9):
            return ("it's 1")
        else:
            return ("it's not one")


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

    perceptron = Perceptron(inputs=35, name=file)

    perceptron.train(X, answers, epochs=1, lr=.01)

    """ for debugging"""
    # [print(perceptron.predict(np.array(x))) for x in X]
    [print(perceptron.give_me_an_answer(x)) for x in X]
