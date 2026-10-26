import numpy as np

def cos_sq(x):
    '''
    Inputs:
        x: n-dimensional array
    Returns: 
        (cos^2(x)) for input x
    '''
    return np.cos(x) ** 2   

def trapezium_rule(f, a, b, n):
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
    return area