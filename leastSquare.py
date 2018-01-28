import numpy as np
from numpy import random, exp, dot

class leastSquare: #the class for least square algorithm
    def __init__(self, inputs, custom): #constructor
        if (custom == 0): #sets weights using 1 more input as 1 and its weight as bias
            self.weights = 2 * random.random((len(inputs[0]) + 1, len(inputs[0]))) - 1
        else: #takes the weights already calculated for quicker testing
            self.weights = inputs

    def predict(self, x, i, outputGate): #predicts the outcome OF PARTICULAR GATE using perceptron algorithm
        bias = 0
        for j in range(1683):
            bias += x[i,j] * self.weights[j,outputGate]
        if (bias >= 0): #Enabling function is >=0
            bias = 1
        else:
            bias = 0
        return bias #returns 0 or 1
    def test(self, x , y): #tests the leastSquare but doesn't update it's weights
        newArray = np.ones((len(x), 1))
        x = np.append(newArray, x, axis=1)
        rightAnswers = 0 #counts the right answers the algorithm makes
        outOf = 0
        for k in range (943):
            for j in range (1682):
                bias = 0
                for i in range (1683):
                    bias += x[k][i] * self.weights[i,j] #predicts outcome of ALL gates using perceptron
                if (bias >= 0):
                    bias = 1
                else:
                    bias = 0
                if (bias == y[k,j]):
                    rightAnswers += 1
                outOf += 1
                print(rightAnswers,outOf,"percentage= ",rightAnswers/outOf) #prints right answers as percentage of all answers
    def train(self, sampleArray, expectedResults, numOfInputs, Lrate): #finds the weights that give  least square
        MSEofOutputGate = np.zeros(1682)
        newArray = np.ones((len(sampleArray), 1))
        sampleArray = np.append(newArray, sampleArray, axis=1)
        for j in range (len(MSEofOutputGate)): #for better testing the success of each individual output gate is calculated individualy
            while(True):
                miniSquareErrors = np.zeros(numOfInputs)
                MSEofOutputGate[j] = 0
                for i in range(numOfInputs):
                    miniSquareErrors[i] = self.predict(sampleArray,i, j) - expectedResults[i][j]
                    MSEofOutputGate[j] += miniSquareErrors[i]**2
                if (MSEofOutputGate[j] < 0.0):
                    print("MSE of gate: ", j, "fixed") # prints if the gate has a success rate close to 0.0
                    break #breaks only if the gate gives the least square
                for i in range(1683): #calculates the partial dirivative of the output  with respect to each weight
                    partialDir = 0
                    for k in range(numOfInputs):
                        partialDir += 2 * miniSquareErrors[k] * sampleArray[k][i] #changes the weights
                    self.weights[i,j] -= Lrate * partialDir
        MSE = 0
        for i in range(1682):
            MSE += MSEofOutputGate[i]

if __name__ == '__main__':
    base = np.arange(4 * 80000).reshape(80000, 4)

    # Read all from base file 1
    fileStream = open('u1.base', 'r')
    lines = fileStream.readlines()
    i = 0
    for line in lines:
        base[i] = line.split("\t")
        i += 1
    fileStream.close()
    #convert results to a 943 * 1682 array
    usersMovies = np.zeros((943, 1682), dtype='float32')

    for i in range(80000):
        usersMovies[base[i][0] - 1][base[i][1] - 1] = 1
    '''
    squares = leastSquare(usersMovies, 0)
    squares.train(usersMovies,usersMovies,10,0.1)

    np.save('doneWeights.npy', squares.weights)
    '''



    #FOR TESTING



    customedWeights = np.load('doneWeights.npy')

    squares = leastSquare(customedWeights, 1)

    test = np.arange(4 * 20000).reshape(20000, 4)
    
    # Read all from test file 1
    fileStream = open('u1.test', 'r')
    lines = fileStream.readlines()
    i = 0
    for line in lines:
        test[i] = line.split("\t")
        i += 1
    fileStream.close()
    #convert it to an array of shape (943, 1682)
    tests = np.zeros((943, 1682), dtype='float32')

    for i in range(20000):
        tests[test[i][0] - 1][test[i][1] - 1] = 1

    rightAnswers = squares.test(tests,tests)