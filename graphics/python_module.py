import numpy as np
from scipy.interpolate import InterpolatedUnivariateSpline


def get_by_scipy(x, y, z):

    spl = InterpolatedUnivariateSpline(x, y)
    xnew = np.linspace(np.min(x), np.max(x), z)
    ynew = spl(xnew)
    return xnew, ynew

# x = np.linspace(-3, 3, 50)
# y = np.exp(-x**2) + 0.1 * np.random.randn(50)
# spl = InterpolatedUnivariateSpline(x, y)
# plt.plot(x, y, 'ro', ms=5)
# xs = np.linspace(-3, 3, 1000)
# plt.plot(xs, spl(xs))
# plt.show()
