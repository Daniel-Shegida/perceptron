# функции для регулирования входных данных ответов
def ones(x):
    if x == 1:
        return 1
    else:
        return 0

def base(x):
    return x

def give_me_ones(X,answers):
    ones = []
    for i in range(len(X)):
        if answers[i] == 1:
            ones.append(X[i])
    return ones

