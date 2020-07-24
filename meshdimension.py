# version 1.0
# created by Carlo Pasquinucci - carlo.a.pasquinucci@gmail.com
# relaesed under license GPL GNU 3 

### python file
### how to choose the dimension of the mesh

## need math

import math

## Initial data, can be calculated bu the k, omega , epsilon calculator - https://github.com/Carlopasquinucci/k-epsilon-omega-python

k= 10
epsilon= 20
omega= 30
Rl=5 #deafult 5, for more accuracy, 10



## Calcolus
l0=k**0.5/(0.09*omega)
l0=k**1.5/(epsilon)
volume=l0*Rl

meshdimension=volume

print(meshdimension)
