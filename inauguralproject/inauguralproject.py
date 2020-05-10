import numpy as np
import scipy.optimize as opt

class ConsumerProblem:
    """ The following class solves the consumerproblem. Firstly the parameters of the model are assigned with intial
    values. Further it relies on the given equations and constraints of the  utility maximization that is the consumer problem. 
    Lastly it also calculates the tax revenue when considering N individuals in a model economy.

    """

    # Parameters are assigned with the given initial value
    def __init__(self): 
        self.m = 1 #cash-on-hand
        self.v = 10 #disutility of labor
        self.eps = 0.3 #elasticity of labor supply
        self.tau_0 = 0.4 #standard labor income tax
        self.tau_1 = 0.1 #top bracket labor income tax
        self.kappa = 0.4 #cut-off for top labor income tax
        self.w = 1 #wage rate

    # Defining the utility equation (the first order condition of the utilitty maximization?)
    def utility(self,c,l):
        u = np.log(c) - self.v*(l**(1+1/self.eps)/(1+1/self.eps))
        return u

    # Defining the budget constraint
    def eq(self,l):
        x = self.m + self.w*l - (self.tau_0*self.w*l + self.tau_1*np.fmax(self.w*l-self.kappa,0))
        return x

    # Defining the choice of consumption which is equal to the solution of total ressources x.
    def choice(self,l):
        c = self.eq(l)
        return -self.utility(c,l)


    def optimizer(self):
        """ solves the consumer problem by optimizing utility.

        Args:
            self (list): list of parameter values (which can be modified from the notebook) 
            

        Returns:
            l_star: optimal labour supply
            c_star: optimal consumption
            u_star: utility given the optimal labour and consumption values.
            result: print of the complete results

        """

        res = opt.minimize_scalar(self.choice, method='bounded', bounds=(0,1))
    
        l_star = res.x
        c_star = self.eq(l_star)
        u_star = self.utility(c_star,l_star)
        result = f'Labour is: {round(l_star,4)}, Consumption is: {round(c_star,4)} and utility is: {round(u_star,4)}'
        return l_star, c_star, u_star, result

    # Tax for the given Consumption and Labour 
    def tax(self,N=10000):
        """ solves the consumer problem by optimizing utility.

        Args:
            self (list): list of parameter values (which can be modified from the notebook) 
            N (int): number of consumers in the simulation
            

        Returns:
            tax_rev: The total tax revenue given the N consumers

        """
        np.random.seed(117)
        w_vec = np.random.uniform(0.5, 1.5, size=N)
        l_opt = np.empty(N)

        for i in range(0,N):
            l_opt[i]=self.optimizer()[0]

        tax = lambda l_opt, w_vec: self.tau_0*w_vec*l_opt + self.tau_1*np.fmax(w_vec*l_opt-self.kappa,0)
        tax_rev=np.sum(tax(l_opt,w_vec))
        return tax_rev

    def para(self): # To print the parameters
        para =  f'm: {self.m}, v: {self.v}, eps: {self.eps}, tau0: {self.tau_0}, tau1: {self.tau_1}, kappa: {self.kappa} and w: {self.w}'
        return para


"""
def tax_revenue(seed,size,low,high,eps=0.3):
    # a. set seed, draw random numbers
    np.random.seed(seed)
    wi = np.random.uniform(low=low,high=high,size=size)
    
    # b. define local parameter values
    kappa = 0.4
    nu = 10
    m = 1
    tau0 = 0.4
    tau1 = 0.1

    # c. solve each individual's optimisation problem
    tax_rev = 0
    
    for i, wi in enumerate (wi):        
        lc = u_optimiser(eps,kappa,nu,m,tau0,tau1,wi)
        tax_i = tau0*wi*lc[0] + tau1*max(wi*lc[0]-kappa,0)
        tax_rev += tax_i

    return tax_rev
"""