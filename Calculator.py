# JupiterLab
#pip install scipy

import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.integrate import odeint

d=3.14
n=0.13 #viskozitāte
r=0.003 # rādiuss
b= 0.001 # lauka stiprums
p=1100 # blīvums
m=0.02 # moments
y = 8*d**n*(r**3)

def q_derivatives(z,t):
    return [z[1], (y)*z[1] - m*b*np.sin(z[0])]

time = np.arange(0, 6, 1e-3)

angle, sth = odeint(q_derivatives, [2e-3, 0], time).T 

plt.plot(time, angle, 'orange', linewidth = 2)
plt.xlabel('time (s)')
plt.ylabel('position (cm)')
plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
plt.grid(True)
