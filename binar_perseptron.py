import mnist
from model.perseptron import Perceptron
from functions.binar import binar
from functions.utils import ones

"""our data samples"""
m = mnist.MNIST('D:\MNIST_DATA')
m.gz = True
X, Y = m.load_training()

file = 'test.txt'

perceptron = Perceptron(inputs=784, name=file, activ_fun= binar, train_fun=ones)
perceptron.train(X, Y, epochs=1, lr=.01)


for i in range(1000):
    print(perceptron.give_me_an_answer(X[i]))
    print("answer is: ", Y[i])


