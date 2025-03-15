import numpy as np
import matplotlib.pyplot as plt

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return sigmoid(x) * (1 - sigmoid(x))

def xor_neural_network(epochs=10000, learning_rate=0.1):
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]]) 
    y_true = np.array([[0], [1], [1], [0]]) 

    W1 = np.random.uniform(-1, 1, size=(2, 2)) #vahy mezi vstupni a skrytou vrstvou
    b1 = np.random.uniform(-1, 1, size=(1, 2)) #biasy skrytych neuronu
    W2 = np.random.uniform(-1, 1, size=(2, 1)) #vahy mezi skrytou a vystupni vrstvou
    b2 = np.random.uniform(-1, 1, size=(1, 1)) #bias vystupniho neuronu

    for epoch in range(epochs):
        #vazene soucty a aktivace
        Z1 = np.dot(X, W1) + b1
        A1 = sigmoid(Z1)
        Z2 = np.dot(A1, W2) + b2
        y_pred = sigmoid(Z2)

        
        error = y_true - y_pred #vypocet chyby

        #backpropagation
        dA2 = error * sigmoid_derivative(Z2)  #gradient chyby pro vystupni neuron
        dW2 = np.dot(A1.T, dA2)  #gradient vah mezi skrytou a vystupni vrstvou
        db2 = np.sum(dA2, axis=0, keepdims=True)  #gradient biasu vystupni vrstvy

        dA1 = np.dot(dA2, W2.T) * sigmoid_derivative(Z1)  #gradient chyby pro skrytou vrstvu
        dW1 = np.dot(X.T, dA1)  #gradient vah mezi vstupni a skrytou vrstvou
        db1 = np.sum(dA1, axis=0, keepdims=True)  #gradient biasu skryte vrstvy

        #gradientni sestup (aktualizace vah a biasu)
        W1 += learning_rate * dW1
        b1 += learning_rate * db1
        W2 += learning_rate * dW2
        b2 += learning_rate * db2

        if epoch % 1000 == 0:
            print(f"Epoch: {epoch}\n W1: {W1}\n b1: {b1}\n W2: {W2}\n b2: {b2}\n y_pred: {y_pred}\n")
            


    return W1, b1, W2, b2

#train
W1, b1, W2, b2 = xor_neural_network()

X_test = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
Y_test = np.array([[0], [1], [1], [0]])
Z1_test = np.dot(X_test, W1) + b1
A1_test = sigmoid(Z1_test)
Z2_test = np.dot(A1_test, W2) + b2
y_pred_test = sigmoid(Z2_test)

for i in range(len(X_test)):
    print(f"X {X_test[i]} {Y_test[i]} -> y_pred: {y_pred_test[i]}")
