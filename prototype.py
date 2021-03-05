import numpy as np

from data_downloaders.test_data import get_test_data
from model.perseptron import Perceptron
from functions.binar import binar

if __name__ == '__main__':
    """our data samples"""
    X, answers = get_test_data()
    file = 'prototype.txt'

    perceptron = Perceptron(inputs=35, name=file,activ_fun= binar)
    perceptron.train(X, answers, epochs=1111, lr=.01)

    for i in len(X):
        print(perceptron.give_me_an_answer(X[i]))
        print("answer is: ", answers[i])
