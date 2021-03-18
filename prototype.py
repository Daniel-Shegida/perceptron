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
    table_x, table_y = get_noise_stat(perceptron,X,answers,get_random_inversion,)
    show(table_x,table_y)


