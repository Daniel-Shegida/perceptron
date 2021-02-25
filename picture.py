
from PIL import Image
from numpy import asarray
import numpy as np
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


if __name__ == '__main__':
    file = 'pics.txt'
    img = Image.open('data\one.png').convert('L')
    one = asarray(img).flatten()
    img = Image.open('data\ones.png').convert('L')
    one1 = asarray(img).flatten()
    img = Image.open('data\wo.png').convert('L')
    two = asarray(img).flatten()
    img = Image.open('data\ee.png').convert('L')
    tree = asarray(img).flatten()
    img = Image.open('data\our.png').convert('L')
    four = asarray(img).flatten()
    img = Image.open('data\lack.png').convert('L')
    blank = asarray(img).flatten()

    X = [one, one1, two, tree, four, blank]
    Y = [1, 1, 0, 0, 0, 0]

    print(len(one))

    Perceptron = Perceptron(inputs=10100, name=file)
    Perceptron.train(X, Y, epochs=1111, lr=.01)


    """ for debugging"""
    # [print(perceptron.predict(np.array(x))) for x in X]
    [print(Perceptron.give_me_an_answer(x)) for x in X]
    """" тестовое изображение """
    img = Image.open('data\oneee.png').convert('L')
    one = asarray(img).flatten()
    print(Perceptron.predict(np.array(one)))
