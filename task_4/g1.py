
## no need

class G1():
    def __init__(self, size):
        self.size = size

    def give(self, X, R):
        y = []
        if (sum(X) == 1 and sum(R) != 1):
            for i in range(self.size):
                y.append(1)
            return y
        else:
            for i in range(self.size):
                y.append(0)
            return y