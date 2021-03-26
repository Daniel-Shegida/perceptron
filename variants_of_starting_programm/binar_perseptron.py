import mnist

from graphics.presentator import show
from model.perseptron import Perceptron
from functions.binar import binar
from functions.utils import ones, give_me_ones
from noises.noise_statistic import get_noise_stat
from noises.random_inversion import get_random_inversion

"""our data samples"""
m = mnist.MNIST('D:\MNIST_DATA')
m.gz = True
X, Y = m.load_training()

file = 'binar_perseptron.txt'

perceptron = Perceptron(inputs=784, name=file, activ_fun=binar, train_fun=ones)
perceptron.train(X, Y, epochs=1, lr=.01)

for i in range(1000):
    print(perceptron.give_me_an_answer(X[i]))
    print("answer is: ", Y[i])

# table_x, table_y = get_noise_stat(perceptron,X,Y,get_random_inversion)
#
# show(table_x, table_y)
