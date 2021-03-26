import random


def get_random_inversion(noise_data, noise_percent, data_size=256):
    for i in range(len(noise_data)):
        for k in range(len(noise_data[i])):
            if random.randint(0, 100) < noise_percent:
                noise_data[i][k] = abs(noise_data[i][k] - data_size)
    return noise_data
