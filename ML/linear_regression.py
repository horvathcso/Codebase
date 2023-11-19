import numpy as np
import matplotlib.pyplot as plt

class LinearClassifierwithSGD():
    '''
        Python implementation of the Linear classifier with Stochastic Gradient Descent. 
        Implementation copied from (https://www.section.io/engineering-education/sgd-classifier/, https://replit.com/@lalithNarayan/CumbersomePromotedDictionaries?lite=true)
    '''
    def __init__(self,learning_rate=0.5,tolerance=1e-3, seed=42, normalize=True, num_iterations= 500):
        np.random.seed(seed)
        self.weight = None
        self.num_iterations = num_iterations
        self.bias = None
        self.learning_rate = learning_rate
        self.tolerance = tolerance
        self.length = None
        self.normalize= normalize
        self.m = None
        self.costs  = []
        self.iterations = []
    
    def sigmoid(self,z):
        return 1/(1+np.exp(-z)+1e-8)
    
    def initalize_weights(self):
        self.weight = np.random.random(self.length)
        self.bias = 0

    def logistic_loss(self,p,y):
        individual_loss = -(y*np.log(p)+(1-y)*np.log(1-p))
        cost = np.sum(individual_loss)/self.m
        return cost

    def optimize(self,X,y):
        estimated_y = self.sigmoid(np.dot(X,self.weight)+self.bias)
        dw = np.dot(X.T,(estimated_y-y))/self.m
        db = np.sum(estimated_y - y)/self.m
        self.weight = self.weight - self.learning_rate * dw
        self.bias = self.bias - self.learning_rate * db

    def normalize_function(self,X):
        return (X-np.mean(X))/np.std(X)        
    
    def fit(self,X,y):
        if self.normalize:
            X = self.normalize_function(X)
        self.m,self.length = X.shape
        self.initalize_weights()
        previous_cost , iteration_number = float('inf'), 0 
        self.costs.append(previous_cost)
        self.iterations.append(iteration_number)

        while iteration_number<self.num_iterations:
            estimated_y  = self.sigmoid(np.dot(X,self.weight)+self.bias)
            cost = self.logistic_loss(estimated_y, y)

            if iteration_number%10==0:
                print(f"Iteration:{iteration_number}, Cost: {cost:.3f}")
            self.optimize(X,y)
            if previous_cost - cost < self.tolerance:
                break
            else:
                previous_cost, iteration_number = cost, iteration_number + 1
                self.costs.append(cost)
                self.iterations.append(iteration_number)
    

    def predict(self, X):
        return self.predict_probabilty(X)[:, 1] > 0.5

    def predict_probabilty(self, X):
        if self.normalize:
            X = self.normalize_function(X)
            ones = self.sigmoid(np.dot(X,self.weight)+self.bias)
            return np.c_[1-ones, ones]
    
    def plot(self):
        plt.figure(figsize= (7,6))
        plt.plot(self.iterations, self.costs,marker='.',linestyle='-')
        plt.xlabel('Iterations')
        plt.ylabel(('Loss'))
        plt.title('Iterations vs Loss')
        plt.show()
    
    def score(self,X,y):
        return (self.predict(X) == y).sum()/len(y)

    @property
    def coef_(self):
        return self.weight
    
    @property
    def intercept(self):
        return self.bias