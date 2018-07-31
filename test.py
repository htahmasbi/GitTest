#!/usr/bin/env python
import numpy as np

np.random.seed(1)
a=np.random.randint(5 , size=(3, 4))
b=np.random.randint(6 , size=(3, 4))
c = a*b
print c[:,1]
print c[:,2]
print c[:,3]
