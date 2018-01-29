import numpy as np
from numpy import random, exp, dot

class NN: #neural network class
    hl1 = 10
    hl2 = 10

    def __init__(self, inputs, outputs): #neural network constructor
        random.seed(1) #takes desired inputs and outputs for testing

        self.input = inputs
        self.output = outputs

        self.layer_1_nodes = self.hl1
        self.layer_2_nodes = self.hl2

        self.input_shape = (1, 1682)
        self.output_shape = (1, 1682)

        self.weights_1 = 2 * random.random((self.input_shape[1], self.layer_1_nodes)) - 1
        self.weights_2 = 2 * random.random((self.layer_1_nodes, self.layer_2_nodes)) - 1

        self.out_weights = 2 * random.random((self.layer_2_nodes, self.output_shape[1])) - 1

    def sigmoid(self, x): #sigmoid function used
        for i in range(len(x)):
            for j in range(np.shape(x)[1]):
                if (x[i][j] < -10): x[i][j] = -5

        return 1 / (1 + exp(-x))


    def sigmoid_derivative(self, x): #calculates sigmoid dirivative
        return x * (1 - x)

    def think(self, x, outs):
        # Inputs are multiplied with weights and then passed to next layer
        layer1 = self.sigmoid(dot(x, self.weights_1))
        layer2 = self.sigmoid(dot(layer1, self.weights_2))
        output = self.sigmoid(dot(layer2, self.out_weights))

        for i in range (943):
            for j in range(1682):
                if (output[i][j] >=  0.5):
                    output[i][j] = 1.0 #activation function
                else:
                    output[i][j] = 0.0
        return x - output

    def train(self): #training function
        layer1 = self.sigmoid(dot(self.input, self.weights_1))

        layer2 = self.sigmoid(dot(layer1, self.weights_2))

        output = self.sigmoid(dot(layer2, self.out_weights))

        outputError = self.output - output

        delta = outputError * self.sigmoid_derivative(output) #calculates delta of output

        out_weights_adjustment = dot(layer2.T, delta) #adjusts all the weights using backpropagation algorithm

        self.out_weights += out_weights_adjustment

        delta = dot(delta, self.out_weights.T) * self.sigmoid_derivative(layer2)

        weight_2_adjustment = dot(layer1.T, delta)
        self.weights_2 += weight_2_adjustment

        delta = dot(delta, self.weights_2.T) * self.sigmoid_derivative(layer1)
        weight_1_adjustment = dot(self.input.T, delta)
        self.weights_1 += weight_1_adjustment


if __name__ == '__main__': #testing and initializations
    base = np.arange(4 * 80000).reshape(80000, 4)

    # Read all from base file 1
    fileStream = open('u1.base', 'r')
    lines = fileStream.readlines()
    i = 0
    for line in lines:
        base[i] = line.split("\t")
        i += 1
    fileStream.close()

    usersMovies = np.zeros((943, 1682), dtype='float32')

    for i in range(80000):
        usersMovies[base[i][0] - 1][base[i][1] - 1] = 1



    neuralN = NN(usersMovies, usersMovies)

    neuralN.train() #trains neural network

    test = np.arange(4 * 20000).reshape(20000, 4)

    # Read all from test file 1
    fileStream = open('u1.test', 'r')
    lines = fileStream.readlines()
    i = 0
    for line in lines:
        test[i] = line.split("\t")
        i += 1
    fileStream.close()

    tests = np.zeros((943, 1682), dtype='float32')

    for i in range(20000):
        tests[test[i][0] - 1][test[i][1] - 1] = 1

    results = neuralN.think(tests,tests) #tests the erros made for test file
    errors = 0
    for j in range (943):
        for i in range (1682):
            if(results[j][i] != 0.0):
                errors += 1
    print (errors)