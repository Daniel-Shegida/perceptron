import mnist

def get_mnist_data():
    PATH_NAME = 'D:\MNIST_DATA'
    m = mnist.MNIST(PATH_NAME)
    m.gz = True
    X, Y = m.load_training()
    return X,Y