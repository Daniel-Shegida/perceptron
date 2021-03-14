import numpy as np

def add_noise(size,noise_value):
    noise = np.random.normal(0, noise_value, size)
    return noise


def get_noise_data(data, noise_percent, data_size = 256):
    noise_data = []
    noise_value = data_size/100 * noise_percent
    for i in data:
        noise_data.append((i + add_noise(len(i),noise_value)).tolist())
    return noise_data

