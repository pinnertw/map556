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
        self.cost = np.zeros(11)
        self.trajectoire = [np.copy(self.X)]
        return self.X

    def reset_s(self, i, bool_reset_vent=True):
        if i == 0:
            self.reset()
        else:
            self.X = np.copy(self.trajectoire[10 * i])
            self.discrete_t = i * 10
            last_cost = self.cost[:i]
            self.cost = np.zeros(11)
            self.cost[:i] = last_cost
            self.trajectoire = self.trajectoire[:10*i + 1]
            if bool_reset_vent:
                self.reset_vent(i)
            return self.X

    def reset_vent(self, i):
        X = np.random.multivariate_normal(mean=np.zeros(shape=2), cov=self.cov, size=(10 - i) * 10)
        for j in range(i * 10, 100):
            self.vent[j] = X[j-10*i] + np.matmul(self.coeff, self.vent[j-1])
    
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
        if i == 10:
            return self.X, self.cost[10], True, None
        for j in range(10):
            self.X[1:] = self.dynamique_pos(action)
            self.trajectoire.append(np.copy(self.X))
            self.discrete_t += 1
        self.trajectoire[-1][0] += 1
        
        self.X[0] += 1
        self.cost[i] = np.linalg.norm(action) ** 2
        if i == 9:
            self.cost[10] = self.g_func()
        return self.X, self.cost[i], False, None
        #return self.X, 0., done, None

    def g_func(self):
        u1 = ((self.X[1] - 100) - self.X[2]) / np.sqrt(2)
        u2 = ((self.X[1] - 100) + self.X[2]) / np.sqrt(2)
        return (u1 + u1 * (u1>0)) ** 2 + u2 ** 2

    def g_prime(self):
        x1 = self.X[1]
        x2 = self.X[2]
        dx1 = x1 - 100. - x2
        dx2 = x2 + 100. - x1

        dx1_ = x1 + x2 - 100.
        if x1 - 100. - x2 > 0:
            dx1 *= 4
            dx2 *= 4
        return np.array([dx1 + dx1_, dx2 + dx1_])
