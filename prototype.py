import numpy as np

from data_downloaders.test_data import get_test_data
from model.perseptron import Perceptron
from functions.binar import binar
from noises.random_noises import get_random_noise_data
from test import get_noise_data

if __name__ == '__main__':
    """our data samples"""
    X, answers = get_test_data()
    print(X[0])
    file = 'prototype.txt'

    perceptron = Perceptron(inputs=35, name=file)
    # perceptron.train(X, answers, epochs=1111, lr=.01)
    # for i in range(len(X)):
    #     print(perceptron.give_me_an_answer(X[i]))
    #     print("answer is: ", answers[i])
    # print(X)
    # get_noise_data(X,5,data_size=1)




    # noise_perc = 0
    # errors = []
    # number_of_study = 100
    # for i in range(20):
    #     noise_perc +=5
    #     errors.append(0)
    #     # noise_x = get_noise_data(X, noise_perc, data_size=1)
    #     # print(noise_x[0])
    #     # print(X[0])
    #     for k in range(number_of_study):
    #         noise_x = get_noise_data(X,noise_perc,data_size=1)
    #         for z in range(len(noise_x)):
    #             print("weasd")
    #             print(perceptron.give_me_an_answer(noise_x[z]))
    #             print(answers[z][0])
    #             print("sadasd")
    #             if (perceptron.give_me_an_answer(noise_x[z]) != answers[z][0]):
    #                 errors[i] += 1
    # print((np.array(errors) ) / len(X) / number_of_study)
    #
    # print(errors)


    noise_perc = 0
    errors = []
    number_of_study = 1
    print(X[0])
    for i in range(5):
        print("wow")
        noise_perc +=20
        errors.append(0)
        # noise_x = get_noise_data(X, noise_perc, data_size=1)
        # print(noise_x[0])
        # print(X[0])
        for k in range(number_of_study):
            test = X
            print(X[0])
            print("there?")
            noise_x = get_random_noise_data(test,noise_perc,data_size=1)
            print(X[0])
            print("there?")
            for z in range(len(noise_x)):
                # print(noise_x[z])
                # print(X[z])
                # print("new")
                # print("weasd")
                # print(perceptron.give_me_an_answer(noise_x[z]))
                # print(answers[z][0])
                # print("sadasd")
                if (perceptron.give_me_an_answer(noise_x[z]) != answers[z][0]):
                    print("error",answers[z][0])
                    print("answer",perceptron.give_me_an_answer(noise_x[z]))
                    print(noise_x[z])
                    print(X[z])
                    print(z)
                    print("new")
                    errors[i] += 1

    print(errors)


