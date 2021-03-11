import mnist

def get_mnist_data():
    PATH_NAME = 'D:\MNIST_DATA' # местоположения данных мнист
    m = mnist.MNIST(PATH_NAME) # загрузка данных мнист в m
    m.gz = True # разрешение на разархивацию данных (в данном случае данные в gz архиве)
    X, Y = m.load_training() # X - входные данные, Y - ответы
    return X,Y