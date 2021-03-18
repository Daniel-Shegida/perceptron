import numpy as np
from data_downloaders.test_data import get_test_data
from graphics.shower import show
from model.perseptron import Perceptron
from functions.binar import binar
from noises.random_inversion import get_random_noise_data
from test import get_noise_data

if __name__ == '__main__':
    """our data samples"""
    X, answers = get_test_data()
    print(X[0])
    file = 'prototype.txt'

    perceptron = Perceptron(inputs=35, name=file)
    noise_perc = 0
    errors = []
    perc = []
    number_of_study = 1000
    for i in range(100):
        noise_perc +=1
        perc.append(noise_perc)
        errors.append(0)
        for k in range(number_of_study):
            test = X
            noise_x = get_random_noise_data(test,noise_perc,data_size=1)
            for z in range(len(noise_x)):
                if (perceptron.give_me_an_answer(noise_x[z]) != answers[z][0]):
                    errors[i] += 1
        errors[i] = errors[i] / number_of_study / len(X) * 100

    print(errors)
    print(perc)
    show(perc,errors)


