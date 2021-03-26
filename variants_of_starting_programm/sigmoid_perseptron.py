from data_downloaders.mnist_data import get_mnist_data
from graphics.presentator import show
from model.perseptron import Perceptron
from functions.utils import ones, give_me_ones
from noises.noise_statistic import get_noise_stat
from noises.random_inversion import get_random_inversion

file = 'test.txt'

"""our data samples"""
X, Y = get_mnist_data()

perceptron = Perceptron(inputs=784, name=file,train_fun=ones)
# perceptron.train(X, Y, epochs=1, lr=.01)

# [print(perceptron.give_me_an_answer(x)) for x in X]
# for i in range(1000):
#     print(perceptron.give_me_an_answer(X[i]))
#     print("answer is: ", Y[i])


table_x, table_y = get_noise_stat(perceptron,X,Y,get_random_inversion)

show(table_x, table_y)