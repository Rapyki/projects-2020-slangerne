import numpy as np
import scipy.optimize as opt


# Defining utility



class ConsumerClass:

    def __init__(self):
        self.m = 1 #cash-on-hand
        self.v = 10 #disutility of labor
        self.eps = 0.3 #elasticity of labor supply
        self.tau_0 = 0.4 #standard labor income tax
        self.tau_1 = 0.1 #top bracket labor income tax
        self.kappa = 0.4 #cut-off for top labor income tax
        self.w = 0.5 #wage rate

    def utility(self,c,l):
        u = np.log(c) - self.v*(l**(1+1/self.eps)/(1+1/self.eps))
        return u

    # Defining constraint

    def eq(self,l):
        x = self.m + self.w*l - (self.tau_0*self.w*l + self.tau_1*np.max(self.w*l-self.kappa,0))
        return x


    def choice(self,l):
        c = self.eq(l)
        return -self.utility(c,l)


    def optimizer(self):
        res = opt.minimize_scalar(
        self.choice, method='bounded',
        bounds=(0,1), args=(self))
    
        l_star = res.x
        c_star = self.eq(l_star)
        u_star = self.utility(c_star,l_star)
    
        return l_star, c_star, u_star
        

