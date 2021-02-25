
import numpy as np
import os.path
import mnist


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
                if y != 1:
                    y = 0
                x1 = np.array(x)

                y_predict = self.predict(x)

                err = (y - y_predict)
                weq = x1 * (err * lr)
                self.weights += weq

                print("\rEpoch #{} - error: {}".format(i + 1, err, 3))
        np.savetxt(self.fileName, self.weights, fmt='%1.4f')
        print("Total - error: {} ".format(err, 3))

    def activation(self, x):
        """ Функция активации (бинарная) """
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


# """our data samples"""
m = mnist.MNIST('D:\MNIST_DATA')
m.gz = True
X, Y = m.load_training()

file = 'test.txt'

perceptron = Perceptron(inputs=784, name=file)

perceptron.train(X, Y, epochs=1, lr=.01)

# """ for debugging"""
# # [print(perceptron.predict(np.array(x))) for x in X]
[print(perceptron.give_me_an_answer(x)) for x in X]
for i in range(1000):
    print(perceptron.give_me_an_answer(X[i]))
    print(Y[i])