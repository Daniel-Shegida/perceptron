import os
from random import random

from mnist.loader import np

from functions.binar import binar



class Kohonen_neironet():
    def __init__(self, X, size):
        self.net = []
        for i in range(size):
            self.net.append(Kohonen_perceptron(inputs=X, name=str(i)))

    def acceleration(self, X, education_rate):
        for j in range(3000):
            education_element = normal_list(X[j])
            for i in range(len(self.net)):
                self.net[i].test_train(education_element, education_rate)

    def train(self, education_data, education_rate, decrease_value, epochs=1):
        while education_rate > 0:
            for i in range(epochs):
                for j in range(len(education_data)):
                    # for j in range(3000):
                    education_element = normal_list(education_data[j])
                    print("progress is {} in {}".format(j, len(education_data)))
                    id, min = self.predict(education_element)
                    self.net[id].test_train(education_element, education_rate)
            education_rate -= decrease_value
        self.save_net()

    def predict(self, X):
        min = 99999
        id = 0
        for k in range(len(self.net)):
            prediction = self.net[k].activation(X)
            if prediction < min:
                id = k
                min = prediction
        return id, min

    def save_net(self):
        for i in range(len(self.net)):
            self.net[i].save_weights()



class recognition_net():
    def __init__(self, size):
        self.id = 0
        self.size = size
        self.net = []

    def add_neiron(self):
        self.net.append(Perceptron(len(self.net), inputs=self.size))


    def phase_recognition(self, input_c, blocked_neurons):
        recognition_win = 0
        net_win = 0
        for i, recognition in enumerate(self.layer_recognition):

            next_step = False
            for j in blocked_neurons:
                if j == i:
                    next_step = True
                    break
            if next_step:
                continue

            net = recognition.calculate_r(input_c)
            if net > net_win:
                net_win = net
                recognition_win = i
        return recognition_win


layer_recognition = recognition_net(len(input_x))
blocked_neurons = []
receiver = G1(len(input_x))
reseter1 = reseter(0.9)
while len(blocked_neurons) < len(layer_recognition.net):

    # Фаза распознавания
    recognition_win = layer_recognition.phase_recognition(input_x, blocked_neurons)

    # Фаза сравнения
    receiver.give(input_x, layer_recognition.net[recognition_win].get_t())

    output_c = compare(input_x, recognition_win)

    reset = reseter1.compare(input_x, output_c)

    if reset:
        blocked_neurons.append(recognition_win)
        continue

    layer_recognition[recognition_win].learn(output_c)

layer_recognition.add_neiron
layer_recognition[len(layer_recognition) - 1].learn(input_x)





