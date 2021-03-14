from data_downloaders.mnist_data import get_mnist_data
from model.perseptron import Perceptron
from functions.utils import ones, give_me_ones
from test import get_noise_data

file = 'test.txt'

"""our data samples"""
X, Y = get_mnist_data()

perceptron = Perceptron(inputs=784, name=file,train_fun=ones)
# perceptron.train(X, Y, epochs=1, lr=.01)

# [print(perceptron.give_me_an_answer(x)) for x in X]
# for i in range(1000):
#     print(perceptron.give_me_an_answer(X[i]))
#     print("answer is: ", Y[i])
#

# noise_perc = 0
# errors = []
# number_of_study = 1
# for i in range(20):
#     noise_perc += 5
#     errors.append(0)
    # noise_x = get_noise_data(X, noise_perc)
    # print(noise_x[0])
    # print(X[0])
#     for k in range(number_of_study):
#         noise_x = get_noise_data(X, noise_perc)
#         for z in range(len(noise_x)):
#             print("weasd")
#             print(perceptron.give_me_an_answer(noise_x[z]))
#             print(Y[z])
#             print("sadasd")
#             if (perceptron.give_me_an_answer(noise_x[z]) != ones(Y[z])):
#                 errors[i] += 1
# # print((np.array(errors)) / len(X) / number_of_study)
# print(errors)

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

