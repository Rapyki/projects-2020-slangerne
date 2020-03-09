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
    return  np.log(c)-v*(l**(1+1/epsilon))/(1+1/epsilon)

    