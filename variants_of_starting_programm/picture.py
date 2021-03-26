import numpy as np
from PIL import Image
from numpy import asarray
from data_downloaders.pic_data import get_pic_data, get_test_pic
from model.perseptron import Perceptron

if __name__ == '__main__':
    file = 'pics.txt'

    X, Y = get_pic_data()

    perceptron = Perceptron(inputs=10100, name=file)
    perceptron.train(X, Y, epochs=1111, lr=.01)

    [print(x, perceptron.give_me_an_answer(x)) for x in X]

    """" test with not study data"""
    one = get_test_pic()
    print("test",perceptron.give_me_an_answer(one))
