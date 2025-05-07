import numpy as np
import matplotlib.pyplot as plt

def logistic_map(a, x):
    return a * x * (1 - x)

def generate_data(num_samples=100000, iterations=100):
    a_values = np.random.uniform(0, 4, num_samples)
    x0_values = np.random.uniform(0, 1, num_samples)
    x_values = x0_values.copy()

    for _ in range(iterations):
        x_values = logistic_map(a_values, x_values)

    X = np.vstack((a_values, x0_values)).T
    y = x_values
    return X, y

a_values = np.linspace(0, 4, 10000)
n_iterations = 1000
last = 100
x = 1e-5 * np.ones(len(a_values))

plt.figure(figsize=(12, 7))
for i in range(n_iterations):
    x = logistic_map(a_values, x)
    if i >= (n_iterations - last):
        plt.plot(a_values, x, ',k', alpha=0.25)

plt.title("Bifurkační diagram logistického zobrazení")
plt.xlabel("a")
plt.ylabel("x")
plt.grid(True)
plt.show()