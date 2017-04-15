import numpy as np
from scipy import optimize
import random



# X = (hours sleeping, hours studying), y = score on test
X = np.array(([3,5], [5,1], [10,2], [6,1.5]), dtype=float)
y = np.array(([75], [82], [93], [70]), dtype=float)

X = X/np.amax(X, axis=0)
y = y/100 #Max test score is 100

def generatetrain(lenght,max):
    X = np.random.randint(max+1, size=(lenght, 2))
    y = []
    for i in range(lenght):
        y = np.append(y, [X[i][0]+X[i][1]])
        #y[i] = X[i][0]+X[i][1]
    return X.astype(float), y.astype(int).reshape(lenght, 1)

train = generatetrain(1000, 10)
#Training Data:
trainX = np.array(train[0], dtype=float)
trainY = np.array(train[1], dtype=float)

#Training Data:
#trainX = np.array(([1,1], [2,2], [3,3], [4,4], [5,5], [6,6], [7,7], [0,0]), dtype=float)
#trainY = np.array(([2], [4], [6], [8], [10], [12], [14], [0]), dtype=float)
#print trainY

#Testing Data:
testX = np.array(([0.5, 1.5], [3,5.5], [10.2, 4.1], [10, 2]), dtype=float)
testY = np.array(([2], [8.5], [14.3], [12]), dtype=float)

#Normalize:
normstep = np.amax(trainX, axis=0)
trainX = trainX/normstep #np.amax(trainX, axis=0)
trainY = trainY/100 #Max test score is 100

#Normalize:
testX = testX/np.amax(testX, axis=0)
testY = testY/100 #Max test score is 100

Lambda = 0.0001

# New complete class, with changes:
class Neural_Network(object):
    def __init__(self, Lambda=0):
        # Define Hyperparameters
        self.inputLayerSize = 2
        self.outputLayerSize = 1
        self.hiddenLayerSize = 10

        # Weights (parameters)
        self.W1 = np.random.randn(self.inputLayerSize, self.hiddenLayerSize)
        self.W2 = np.random.randn(self.hiddenLayerSize, self.outputLayerSize)

        # Regularization Parameter:
        self.Lambda = Lambda

    def forward(self, X):
        # Propogate inputs though network
        self.z2 = np.dot(X, self.W1)
        self.a2 = self.sigmoid(self.z2)
        self.z3 = np.dot(self.a2, self.W2)
        yHat = self.sigmoid(self.z3)
        return yHat

    def sigmoid(self, z):
        # Apply sigmoid activation function to scalar, vector, or matrix
        return 1 / (1 + np.exp(-z))

    def sigmoidPrime(self, z):
        # Gradient of sigmoid
        return np.exp(-z) / ((1 + np.exp(-z)) ** 2)

    def costFunction(self, X, y):
        # Compute cost for given X,y, use weights already stored in class.
        self.yHat = self.forward(X)
        J = 0.5 * sum((y - self.yHat) ** 2) / X.shape[0] + (self.Lambda / 2) * (
        np.sum(self.W1 ** 2) + np.sum(self.W2 ** 2))
        return J

    def costFunctionPrime(self, X, y):
        # Compute derivative with respect to W and W2 for a given X and y:
        self.yHat = self.forward(X)

        delta3 = np.multiply(-(y - self.yHat), self.sigmoidPrime(self.z3))
        # Add gradient of regularization term:
        dJdW2 = np.dot(self.a2.T, delta3) / X.shape[0] + self.Lambda * self.W2

        delta2 = np.dot(delta3, self.W2.T) * self.sigmoidPrime(self.z2)
        # Add gradient of regularization term:
        dJdW1 = np.dot(X.T, delta2) / X.shape[0] + self.Lambda * self.W1

        return dJdW1, dJdW2

    # Helper functions for interacting with other methods/classes
    def getParams(self):
        # Get W1 and W2 Rolled into vector:
        params = np.concatenate((self.W1.ravel(), self.W2.ravel()))
        return params

    def setParams(self, params):
        # Set W1 and W2 using single parameter vector:
        W1_start = 0
        W1_end = self.hiddenLayerSize * self.inputLayerSize
        self.W1 = np.reshape(params[W1_start:W1_end], \
                             (self.inputLayerSize, self.hiddenLayerSize))
        W2_end = W1_end + self.hiddenLayerSize * self.outputLayerSize
        self.W2 = np.reshape(params[W1_end:W2_end], \
                             (self.hiddenLayerSize, self.outputLayerSize))

    def computeGradients(self, X, y):
        dJdW1, dJdW2 = self.costFunctionPrime(X, y)
        return np.concatenate((dJdW1.ravel(), dJdW2.ravel()))


def computeNumericalGradient(N, X, y):
    paramsInitial = N.getParams()
    numgrad = np.zeros(paramsInitial.shape)
    perturb = np.zeros(paramsInitial.shape)
    e = 1e-4

    for p in range(len(paramsInitial)):
        # Set perturbation vector
        perturb[p] = e
        N.setParams(paramsInitial + perturb)
        loss2 = N.costFunction(X, y)

        N.setParams(paramsInitial - perturb)
        loss1 = N.costFunction(X, y)

        # Compute Numerical Gradient
        numgrad[p] = (loss2 - loss1) / (2 * e)

        # Return the value we changed to zero:
        perturb[p] = 0

    # Return Params to original value:
    N.setParams(paramsInitial)

    return numgrad
#Need to make changes to costFunction and costFunctionPrime
def costFunction(self, X, y):
    #Compute cost for given X,y, use weights already stored in class.
    self.yHat = self.forward(X)
    J = 0.5*sum((y-self.yHat)**2)/X.shape[0] + (self.Lambda/2)*(sum(self.W1**2)+sum(self.W2**2))
    return J

def costFunctionPrime(self, X, y):
    #Compute derivative with respect to W and W2 for a given X and y:
    self.yHat = self.forward(X)

    delta3 = np.multiply(-(y-self.yHat), self.sigmoidPrime(self.z3))
    #Add gradient of regularization term:
    dJdW2 = np.dot(self.a2.T, delta3) + self.Lambda*self.W2

    delta2 = np.dot(delta3, self.W2.T)*self.sigmoidPrime(self.z2)
    #Add gradient of regularization term:
    dJdW1 = np.dot(X.T, delta2) + self.Lambda*self.W1

    return dJdW1, dJdW2

##Need to modify trainer class a bit to check testing error during training:
class trainer(object):
    def __init__(self, N):
        #Make Local reference to network:
        self.N = N

    def callbackF(self, params):
        self.N.setParams(params)
        self.J.append(self.N.costFunction(self.X, self.y))
        self.testJ.append(self.N.costFunction(self.testX, self.testY))

    def costFunctionWrapper(self, params, X, y):
        self.N.setParams(params)
        cost = self.N.costFunction(X, y)
        grad = self.N.computeGradients(X,y)

        return cost, grad

    def train(self, trainX, trainY, testX, testY):
        #Make an internal variable for the callback function:
        self.X = trainX
        self.y = trainY

        self.testX = testX
        self.testY = testY

        #Make empty list to store training costs:
        self.J = []
        self.testJ = []

        params0 = self.N.getParams()

        options = {'maxiter': 200, 'disp' : True}
        _res = optimize.minimize(self.costFunctionWrapper, params0, jac=True, method='BFGS', \
                                 args=(trainX, trainY), options=options, callback=self.callbackF)

        self.N.setParams(_res.x)
        self.optimizationResults = _res

Lambda = 0.0001
NN = Neural_Network(Lambda=0.0001)

numgrad = computeNumericalGradient(NN, X, y)
grad = NN.computeGradients(X,y)
print(np.linalg.norm(grad-numgrad)/np.linalg.norm(grad+numgrad))

NN = Neural_Network()

T = trainer(NN)
T.train(trainX, trainY, testX, testY)

#declare what you want to estimate
while True:
    input = map(float, raw_input("Enter your 2 values seperated by a space \n").split())

    print input
    X = np.array((input), dtype=float)
    X = X/normstep

    #X = np.array(([3,5]), dtype=float)
    #X = X/normstep
    print "^^^^^^^^^"
    print "Imput: \n", X*normstep, '\n'
    print 'Output: \n',round(NN.forward(X), 2)*100
    print "^^^^^^^^^"
