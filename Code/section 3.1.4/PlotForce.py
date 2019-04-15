#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 18:30:41 2017

@author: ashcat

Plots the Force on a charge in the presence of a charged, insulated conducting sphere

"""

import matplotlib.pyplot as plt
import numpy as np


# Definition of Force.
def Force (rR, Qq = 3):
    rR_inv = 1/rR
    f = Qq - (rR_inv)*(2*rR - 1)/(rR**2 -1)**2
    return f

# Number of steps in the calculation 
steps = 10000


rR = np.arange(1.1, 5., 1/steps)

plt.plot(rR , Force(rR, Qq=3) , label = r"$\frac{Q}{q} = 3$")
plt.plot(rR , Force(rR, Qq=1) , label = r"$\frac{Q}{q} = 1$")
plt.plot(rR , Force(rR, Qq=0) , label = r"$\frac{Q}{q} = 0$")
plt.plot(rR , Force(rR, Qq= -1) , label = r"$\frac{Q}{q} = -1$")



# Plot Labels
plt.xlabel(r"$\gamma $")
plt.ylabel(r"$\frac{4 \pi \epsilon_0 F r^2}{q^2}$")
plt.legend()

# plot axis ranges
plt.ylim(-5,5)

plt.xticks(np.arange(0,6,1))
plt.yticks(np.arange(-5,5,1))


# Save Plot and show it
plt.savefig('force.pdf')
plt.show()