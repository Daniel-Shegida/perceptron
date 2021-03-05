from PIL import Image
from numpy import asarray

def get_pic_data() :
    img = Image.open('data\one.png').convert('L')
    one = asarray(img).flatten()
    img = Image.open('data\ones.png').convert('L')
    one1 = asarray(img).flatten()
    img = Image.open('data\wo.png').convert('L')
    two = asarray(img).flatten()
    img = Image.open('data\ee.png').convert('L')
    tree = asarray(img).flatten()
    img = Image.open('data\our.png').convert('L')
    four = asarray(img).flatten()
    img = Image.open('data\lack.png').convert('L')
    blank = asarray(img).flatten()

    X = [one, one1, two, tree, four, blank]
    Y = [1, 1, 0, 0, 0, 0]
    return X,Y

def get_test_pic():
    img = Image.open('data\oneee.png').convert('L')
    return  asarray(img).flatten()