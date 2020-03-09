def square(x):
    """ square numpy array
    
    Args:
    
        x (ndarray): input array
        
    Returns:
    
        y (ndarray): output array
    
    """
    
    y = x**2
    return y


def f(c,l,v=10, epsilon=0.3):
    #Function is given as: 
    import numpy as np
    return  np.log(c)-v*(l**(1+1/epsilon))/(1+1/epsilon)


def c(l,w , m=1, tau0=0.4, tau1=0.1,kappa=0.4):
    #x = m + w*l - (tau0*w*l+tau1*(w*l-kappa))

    return m + w*l - (tau0*w*l+tau1*(w*l-kappa))