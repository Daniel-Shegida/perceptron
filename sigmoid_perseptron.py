from data_downloaders.mnist_data import get_mnist_data
from model.perseptron import Perceptron
from functions.utils import ones

file = 'test.txt'

"""our data samples"""
X, Y = get_mnist_data()

perceptron = Perceptron(inputs=784, name=file,train_fun=ones)
perceptron.train(X, Y, epochs=1, lr=.01)

[print(perceptron.give_me_an_answer(x)) for x in X]
for i in range(1000):
    print(perceptron.give_me_an_answer(X[i]))
    print("answer is: ", Y[i])