from math import exp

''' Find the diode operation point with newton-raphson method
 f(vd) = V - vd - R*Is*((np.exp**(vd/vt)) - 1)     
 Id = Is(e^(vd/vt))                                #Equations and constants
 vt = 26 mV
'''

V = 10
R = 1e3                   # Circuit data for example
Is = 0.1e-6
vt = 26e-3
Eps = 5e-6
Miter = 100

def f(vd): # Fuction of the diode voltage
    return V - vd - R*Is*((exp(vd/vt)) - 1)

def fder(vd): # Derivative of the diode voltage function
    return -((exp((500*vd)/13)/260)-1)

def id(vd): # Function of the current on the diode
    return Is*((exp(vd / vt)) - 1)

xInicio = 1 # Initial value for convergence (newton-raphson method)
i = 0

while abs(f(xInicio)) > Eps and i <= Miter: #loop loop with iterations
    xProx = xInicio - f(xInicio) / fder(xInicio)
    xInicio = xProx
    #print(xProx)                           #uncomment to see the iterations updating
    i += 1

print(f'The voltage on the diode is {xInicio}V')
print(f'Iterations made: {i}')
print(f'The current on the diode is {id(xInicio)} A')
