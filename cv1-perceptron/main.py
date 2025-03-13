import numpy as np
import matplotlib.pyplot as plt

def generate_points(lower_bound, upper_bound, n):
    x = np.random.uniform(lower_bound, upper_bound, n)
    y = np.random.uniform(lower_bound, upper_bound, n)
    points = np.column_stack((x, y))
    return points

def line(x):
    y = 3 * x + 2
    return y

def assign_class(x, y):
    if y > line(x):
        return 1
    else:
        return -1

def train_perceptron(points, learning_rate=0.01, epochs=100):
    #nahodne vahy a bias na zacatek
    w = np.random.uniform(-1, 1, size=2)
    b = np.random.uniform(-1, 1)
    
    for _ in range(epochs):
        for point in points:
            y_pred = w[0] * point[0] + w[1] * point[1] + b #aktivacni funkce signum (x1*w1 + x2*w2 + b)
            y_true = assign_class(point[0], point[1]) #label

            #pokud se predikce nerovna skutecnosti, upravuji se vahy a bias
            if y_pred != y_true:
                w[0] = w[0] + learning_rate * (y_true - y_pred) * point[0]
                w[1] = w[1] + learning_rate * (y_true - y_pred) * point[1]
                b = b + learning_rate * (y_true - y_pred)
    return w, b

points = generate_points(-10, 10, 100)
labels = np.array([assign_class(p[0], p[1]) for p in points]) #tvorba labelu pro perceptron (nad nebo pod primkou)

w, b = train_perceptron(points)

x_vals = np.linspace(-10, 10, 100)
y_vals_line = line(x_vals)


plt.scatter(points[labels == 1][:, 0], points[labels == 1][:, 1], color="blue", label="Nad přímkou")
plt.scatter(points[labels == -1][:, 0], points[labels == -1][:, 1], color="red", label="Pod přímkou")

#referencni primka (y = 3x + 2)
plt.plot(x_vals, y_vals_line, 'k-', label="Referenční přímka (y = 3x + 2)")

#rozhodovaci hranice perceptronu
y_vals_perceptron = - (w[0] / w[1]) * x_vals - (b / w[1])
plt.plot(x_vals, y_vals_perceptron, 'k--', label="Rozhodovací hranice")

plt.xlabel("X")
plt.ylabel("Y")
plt.legend()
plt.title("Perceptron - Rozdělení bodů a rozhodovací hranice")
plt.show()



