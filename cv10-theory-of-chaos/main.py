import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

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

plt.title("Bifurcation diagram")
plt.show()


X_train, y_train = generate_data(num_samples=100000, iterations=100)

model = Sequential([
    Dense(64, activation='relu', input_shape=(2,)),
    Dense(64, activation='relu'),
    Dense(1, activation='linear')
])
model.compile(optimizer='adam', loss='mse')
model.fit(X_train, y_train, epochs=30, batch_size=32, verbose=1)

a_values = np.linspace(0, 4, 10000)
x_actual = 1e-5 * np.ones(len(a_values))
x_predicted = 1e-5 * np.ones(len(a_values))
last = 100
n_iterations = 1000

plt.figure(figsize=(12, 7))
for i in range(n_iterations):
    x_actual = logistic_map(a_values, x_actual)
    if i >= (n_iterations - last):
        plt.plot(a_values, x_actual, ',k', alpha=1.0, label="Actual" if i == (n_iterations - last) else "")

    X_pred = np.vstack((a_values, x_predicted)).T
    x_predicted = model.predict(X_pred, batch_size=256).flatten()
    if i >= (n_iterations - last):
        plt.plot(a_values, x_predicted, ',r', alpha=1.0, label="Predicted" if i == (n_iterations - last) else "")

plt.title("Bifurcation Diagram with Predictions")
plt.xlabel("Parameter (a)")
plt.ylabel("Population")
plt.legend()
plt.grid(True)
plt.show()