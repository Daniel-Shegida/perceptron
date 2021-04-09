from data_downloaders.test_data import get_test_data
from graphics.presentator import show
from model.perseptron import Perceptron
from noises.noise_statistic import get_noise_stat
from noises.random_inversion import get_random_inversion

if __name__ == '__main__':
    """our data samples"""
    X, answers = get_test_data()
    file = 'prototype.txt'

    perceptron = Perceptron(inputs=35, name=file)
    #perceptron.train(X, answers, epochs=1111, lr=.01)
    """ получение массиово ошибок и соответсвующие  проценты, в функцию передается наш персептрон, тестируемые массивы,
    ответы к ним и функцию добавления шумов (они находятся в папке noises)"""
    table_x, table_y = get_noise_stat(perceptron,X,answers,get_random_inversion)
    """" пропускает через точки сплайн с помощью библиотеки scipy"""
    show(table_x,table_y)


get