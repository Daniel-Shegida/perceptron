import matplotlib.pyplot as plt

from graphics.python_module import get_by_scipy


def show(tablex, tabley, accuracy = 100):
    tablex, tabley = get_by_scipy(tablex, tabley, accuracy)
    plt.plot(tablex, tabley,
             label="данные наборов данных через scipy")
    plt.title('task #2')  # выбор названия графика
    plt.ylim(bottom=0)  # выбор начала графика от 0 по оси y
    plt.legend(loc="lower right")  # отображение легенды
    plt.show()  # показ графика