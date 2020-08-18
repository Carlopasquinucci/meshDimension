# version 1.0
# created by Carlo Pasquinucci - carlo.a.pasquinucci@gmail.com
# relesead under license GPL GNU 3 

### python file
### how to choose the dimension of the mesh
### Usage: passing k epsilon and omega and omega and rl in this order

## need sys
## need math


## Initial data, can be calculated bu the k, omega , epsilon calculator - https://github.com/Carlopasquinucci/k-epsilon-omega-python
import math
"""
k= 10
epsilon= 20
omega= 30
Rl= 5 #deafult 5, for more accuracy, 10
"""

import sys

## Check number of argument

narg=len(sys.argv)
if narg!=6:
    print("Number of argument is not 5")
    if narg>6:
        print("Reduce the number of arguments")
    else:
        print("Increase the number of arguments")
    exit() 


k=float(sys.argv[1])
epsilon=float(sys.argv[2])
omega= float(sys.argv[3])
Rl= float(sys.argv[4])



## Calcolus
l0=k**0.5/(0.09*omega)
l0=k**1.5/(epsilon)
volume=l0*Rl

meshdimension=volume

print(meshdimension)
