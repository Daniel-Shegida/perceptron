# функции для регулирования входных данных ответов
def ones(x):
    if x == 1:
        return 1
    else:
        return 0


def base(x):
    return x


def give_me_ones(X, answers):
    ones = []
    for i in range(len(X)):
        if answers[i] == 1:
            ones.append(X[i])
    return ones


def give_me_ones_list(X):
    ones = []
    for i in range(len(X)):
        ones.append(1)
    return ones


def copy2(arr):
    copy = []
    for i in range(len(arr)):
        copy.append(list(arr[i]))
    return copy


def normalization(x, max=256, min=0, d2=1, d1=0):
    normal = (x - min) * (d2 - d1) / (max - min)
    return normal


def normal_list(list22):
    new_list = []
    for i in range(len(list22)):
        new_list.append(normalization(list22[i]))
    return new_list

