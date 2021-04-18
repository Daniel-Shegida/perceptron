from task_4.compare import compare
from task_4.g1 import G1
from task_4.reseter import reseter
from test import recognition_net


class art():
    def __init__(self, size, accuracy=0.9):
        self.layer_recognition = recognition_net(len(size))
        self.blocked_neurons = []
        self.receiver = G1(len(size))
        self.reseter1 = reseter(accuracy)

    def work(self, input_x):
        while len(self.blocked_neurons) < len(self.layer_recognition.net):

            # Фаза распознавания
            recognition_win = self.layer_recognition.phase_recognition(input_x, self.blocked_neurons)

            # Фаза сравнения
            self.receiver.give(input_x, self.layer_recognition.net[recognition_win].get_t())

            output_c = compare(self.receiver.give(input_x, self.layer_recognition.net[recognition_win].get_t()),
                               input_x,
                               recognition_win)

            reset = self.reseter1.compare(input_x, output_c)

            if reset:
                self.blocked_neurons.append(recognition_win)
                continue

            self.layer_recognition.net[recognition_win].learn(output_c)

        self.layer_recognition.add_neiron()
        self.layer_recognition[len(self.layer_recognition.net) - 1].learn(input_x)
