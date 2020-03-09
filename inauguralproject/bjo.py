import numpy as np
from scipy import optimize

def square(x):
    """ square numpy array
    
    Args:
    
        x (ndarray): input array
        
    Returns:
    
        y (ndarray): output array
    
    """
    
    y = x**2
    return y
#end


def max(m=1, v=10):
    """ Funktion der returnerer summen af to parametre """
    x = m+v 

    return x

"""
def maxproblem(l, v=10, eps=0.3, w = 1.5, kappa = 0.4, tauzero = 0.4, tauone = 0.1, m= 1):
    # ensure you understand what this function is doing
    x = m + w*l - tauzero*w*l + tauone * np.max(w*l-kappa,0)
    
    for svar_nu in l : 
        svar = np.max(np.log(x) - v * (l**(1+(1/eps))/(1+(1/eps))))
    return svar
    """

m = 1 #cash-on-hand
v = 10 #disutility of labor
eps = 0.3 #elasticity of labor supply
tau_0 = 0.4 #standard labor income tax
tau_1 = 0.1 #top bracket labor income tax
kappa = 0.4 #cut-off for top labor income tax


# Defining utility

def utility(c,v,l,eps):
    u = np.log(c) - v*(l**(1+1/eps)/(1+1/eps))
    return u

# Defining constraint

def eq(m,w,l,tau_0,tau_1,kappa):
    x = m + w*l - (tau_0*w*l + tau_1*np.max(w*l-kappa,0))
    return x


def choice(l,w,eps,v,tau_0,tau_1,kappa):
    c = eq(m,w,l,tau_0,tau_1,kappa)
    return -utility(c,v,l,eps)


def optimizer(w,eps,v,tau_0,tau_1,kappa,m):
    res = optimize.minimize_scalar(
    choice, method='bounded',
    bounds=(0,1), args=(w,eps,v,tau_0,tau_1,kappa))
    
    l_star = res.x
    c_star = eq(m,w,l_star,tau_0,tau_1,kappa)
    utility_star = (c_star,l_star,v,eps)
    
    return l_star,c_star,utility_star

