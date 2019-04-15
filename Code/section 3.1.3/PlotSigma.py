#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 18:30:41 2017

@author: ashcat

Plots the surface charge density sigma on a grounded conducting sphere near a point charge

"""

import matplotlib.pyplot as plt
import numpy as np


# Definition of surface charge density.
def sigma (gamma, rR = 2):
    rR_inv = 1/rR
    s = rR_inv * (1 - rR_inv**2)/(np.sqrt((1 + rR_inv**2 - 2 * rR_inv * np.cos(gamma))**3))
    return s

# Number of steps in the calculation 
steps = 10000


gamma = np.arange(0.0, np.pi, 1/steps)

plt.plot(gamma , sigma(gamma, rR=2) , label = r"$\frac{r'}{R} = 2$")
plt.plot(gamma , sigma(gamma, rR=4) , label = r"$\frac{r'}{R} = 4$")

# Plot Labels
plt.xlabel(r"$\gamma $")
plt.ylabel(r"$\frac{\sigma}{4\pi R^2}$")
plt.legend()

# Save Plot and show it
plt.savefig('sigma.pdf')
plt.show()