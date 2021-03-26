import mnist
from model.perseptron import Perceptron
from functions.binar import binar
from functions.utils import ones, give_me_ones
from test import get_noise_data

"""our data samples"""
m = mnist.MNIST('D:\MNIST_DATA')
m.gz = True
X, Y = m.load_training()

file = 'binar_perseptron.txt'

perceptron = Perceptron(inputs=784, name=file, activ_fun= binar, train_fun=ones)
#perceptron.train(X, Y, epochs=1, lr=.01)


# for i in range(1000):
#     print(perceptron.give_me_an_answer(X[i]))
#     print("answer is: ", Y[i])


new_x = give_me_ones(X,Y)

noise_perc = 0
errors = []
number_of_study = 1
for i in range(5):
    noise_perc += 20
    errors.append(0)
    for k in range(number_of_study):
        noise_x = get_noise_data(new_x, noise_perc)
        print(len(noise_x))
        for z in range(len(noise_x)):
            # print("weasd")
            # print(perceptron.give_me_an_answer(noise_x[z]))
            # print("sadasd")
            if (perceptron.give_me_an_answer(noise_x[z]) != 1):
                errors[i] += 1
# print((np.array(errors)) / len(X) / number_of_study)
print(len(new_x))
print(errors)
