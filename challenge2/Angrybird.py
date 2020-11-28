import numpy as np
from scipy.linalg import expm

class AngryBird():    
    def __init__(self):    
        self.d = np.array([100, 0])
        self.g = np.array([0, -4])
        self.V0 = np.array([10., 20.])
        self.Delta_T = 0.1
        self.lamb = 0.01
        self.A = np.array([[0.9, 1], [1, 0.9]])
        self.cov = np.linalg.inv(self.A).dot(np.eye(2) - expm(-2*self.Delta_T*self.A)) / 2
        self.coeff = expm(-self.Delta_T * self.A)
        self.reset()

    def init_vent(self):
        X = np.random.multivariate_normal(mean=np.zeros(shape=2), cov=self.cov, size=100)
        vent = np.zeros(shape=(100, 2))
        for i in range(1, 100):
            vent[i] = X[i-1] + np.matmul(self.coeff, vent[i-1])
        return vent

    def reset(self):    
        self.X = np.array([0, 0., 0.])
        self.vent = self.init_vent()
        self.discrete_t = 0
        self.cost = 0.
        self.trajectoire = [np.copy(self.X)]
        return self.X
    
    def dynamique_pos(self, controle):
        t = self.discrete_t / 10
        term1 = self.V0 * self.Delta_T
        term2 = self.g / 2 * ((t + self.Delta_T)**2 - t ** 2)
        term3 = self.lamb * self.X[1:] * self.Delta_T
        term4 = self.vent[self.discrete_t] * self.Delta_T
        term5 = controle * self.Delta_T
        return self.X[1:] + term1 + term2 - term3 + term4 + term5
    
    def step(self, action):
        i = int(self.X[0])
        done = False

        for j in range(10):
            self.X[1:] = self.dynamique_pos(action)
            self.trajectoire.append(np.copy(self.X))
            self.discrete_t += 1
        
        self.X[0] += 1
        local_cost = np.linalg.norm(action) ** 2
        self.cost += local_cost
        if i == 9:
            #local_cost += self.normL()
            self.cost += self.normL()
            done = True
            return self.X, self.cost, done, None
        return self.X, 0, done, None

    def normL(self):
        u1 = ((self.X[1] - 100) - self.X[2]) / np.sqrt(2)
        u2 = ((self.X[1] - 100) + self.X[2]) / np.sqrt(2)
        return (u1 + u1 * (u1>0)) ** 2 + u2 ** 2
