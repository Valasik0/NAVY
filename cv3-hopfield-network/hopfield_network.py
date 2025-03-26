import numpy as np

class HopfieldNetwork:
    def __init__(self, size):
        self.size = size
        self.weights = np.zeros((self.size, self.size))

    def train(self, patterns):
        self.weights.fill(0)
        for pattern in patterns:
            p = np.array(pattern).reshape(self.size, 1)
            self.weights += p @ p.T
        np.fill_diagonal(self.weights, 0)

    def sync_update(self, pattern):
        new_pattern = np.sign(self.weights @ pattern)
        new_pattern[new_pattern == 0] = 1
        return new_pattern

    def async_update(self, pattern):
        new_pattern = pattern.copy()
        for i in range(self.size):
            new_pattern[i] = np.sign(np.dot(self.weights[i], new_pattern))
            if new_pattern[i] == 0:
                new_pattern[i] = 1
        return new_pattern
        