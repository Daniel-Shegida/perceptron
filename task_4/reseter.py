class reseter():
    def __init__(self, limit):
        self.limit = limit

    def compare(self, X, C):
        if (sum(X) / sum(C) >= self.limit):
            return False
        else:
            return True