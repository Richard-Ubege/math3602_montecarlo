import numpy as np

def cos_sq(x):
    '''
    Inputs:
        x: n-dimensional array
    Returns: 
        (cos^2(x)) for input x
    '''
    return np.cos(x) ** 2   

def trapezium_rule(f, a, b, n, return_error, true_val=None):
    '''
    Inputs:
        f: the function integral to estimate
        a,b: respectively, the upper and lower bounds
        n: number of trapezia to construct
        
    Returns:
        area: estimate for the integral
    '''
    
    x = np.linspace(a, b, n)
    h = (b - a) / n
    y = f(x)
    
    area = 0.5 * h * (y[0] + 2 * (np.sum(y[1:-1])) + y[-1])
    
    if return_error=='mea':
        error = np.mean(np.abs(true_val - area))
        return area, error




def monte_carlo_integral(f, a, b, n):
    
    '''Using Monte Carlo Method to approximate the 
    integral of function f between bounds a and b by 
    generating n, uniformly distibuted points
    
    Inputs:
        f: the function integral to estimate
        a, b: (respectively) the upper and lower bounds of the function
        n: number of points to randomly generate
        return_error: if true, error will be returned also
        
    Returns:
        estimate: the sestimated integral
        error: the error of the estimate
    '''
    
    x = np.random.uniform(a, b, n)
    f_x = f(x)
    
    sigma_sq = np.var(f_x)
    
    estimate = ((b-a) / n) * np.mean(np.sum(f_x))
    error = (b - a) * np.sqrt(sigma_sq) / np.sqrt(n)
    
    

    return estimate, error




    