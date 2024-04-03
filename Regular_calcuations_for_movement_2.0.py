import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.integrate import odeint

pi=3.14
n=0.13 # šķīduma viskozitāte
r=0.003 #  objekta rādiuss
b= 0.001 # lauka stiprums
q =1100 #  šķīduma blīvums
M=0.02 # magnētiskais moments
y = 8*pi*n*(r**3) # Rotācijas berzes koeficients
I=2 # Inerces moments
W=10000

def q_derivatives(z,t):
    return [z[1], ((1/2)*(-(y)*(z[1]+W) - M*b*np.sin(z[0]) ))]

time = np.arange(0, 1000000, 1)

angle, velocity = odeint(q_derivatives, [0, -W], time).T 

plt.plot(time, angle+ W*time , 'orange', linewidth = 2)
plt.xlabel('time (s)')
plt.ylabel('Angle(rad)')
plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
plt.grid(True)
