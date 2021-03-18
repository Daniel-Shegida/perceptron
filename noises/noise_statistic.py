from functions.utils import copy2

def get_noise_stat(perceptron, X, answers, noise_fun,number_of_study = 1000, noise_rise = 5):
    errors = []
    perc = []
    noise_perc = noise_rise
    perc_iteration = 0
    while noise_perc <= 100:
        perc.append(noise_perc)
        errors.append(0)
        for k in range(number_of_study):
            noise_x = noise_fun(copy2(X), noise_perc, data_size=1)
            for z in range(len(noise_x)):
                if (perceptron.give_me_an_answer(noise_x[z]) != answers[z][0]):
                    errors[perc_iteration] += 1
        errors[perc_iteration] = errors[perc_iteration] / number_of_study / len(X) * 100
        print("{}% ready".format(noise_perc))
        noise_perc += noise_rise
        perc_iteration += 1
    return perc,errors