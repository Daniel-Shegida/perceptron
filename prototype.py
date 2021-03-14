import numpy as np

from data_downloaders.test_data import get_test_data
from model.perseptron import Perceptron
from functions.binar import binar
from test import get_noise_data

if __name__ == '__main__':
    """our data samples"""
    X, answers = get_test_data()
    file = 'prototype.txt'

    perceptron = Perceptron(inputs=35, name=file)
    # perceptron.train(X, answers, epochs=1111, lr=.01)
    # for i in range(len(X)):
    #     print(perceptron.give_me_an_answer(X[i]))
    #     print("answer is: ", answers[i])
    # print(X)
    # get_noise_data(X,5,data_size=1)
    noise_perc = 0
    errors = []
    number_of_study = 100
    for i in range(20):
        noise_perc +=5
        errors.append(0)
        # noise_x = get_noise_data(X, noise_perc, data_size=1)
        # print(noise_x[0])
        # print(X[0])
        for k in range(number_of_study):
            noise_x = get_noise_data(X,noise_perc,data_size=1)
            for z in range(len(noise_x)):
                print("weasd")
                print(perceptron.give_me_an_answer(noise_x[z]))
                print(answers[z][0])
                print("sadasd")
                if (perceptron.give_me_an_answer(noise_x[z]) != answers[z][0]):
                    errors[i] += 1
    print((np.array(errors) ) / len(X) / number_of_study)

    print(errors)



