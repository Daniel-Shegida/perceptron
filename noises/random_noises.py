import numpy as np
import random

def add_noise(size,noise_value):
    noise = np.random.normal(0, noise_value, size)
    return noise


def get_random_noise_data(data, noise_percent, data_size = 256):
    noise_data = []
    for i in range(len(data)):
        noise_data.append(list(data[i]))
    noise_value = data_size/100 * noise_percent
    for i in range(len(noise_data)):
        for k in range(len(noise_data[i])):
            if random.randint(0, 100) < noise_percent:
                noise_data[i][k] = abs(noise_data[i][k] - data_size)
    # print(len(noise_data))
    # print(len(noise_data[0]))

    return noise_data

