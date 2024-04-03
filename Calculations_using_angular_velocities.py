import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.integrate import odeint

π=3.14
η=0.13 # šķīduma viskozitāte
r=0.01 #  objekta rādiuss
b= 0.001 # lauka stiprums
q =1100 #  šķīduma blīvums
M=0.02 # magnētiskais moments
y = 8*pi*n*(r**3) # Rotācijas berzes koeficients
I=1 # Inerces moments
W=10000

W1=
W0=10
Wc=1

def q_derivatives(z,t):
    return [z[1], (-W1*(z[1]-W0)-(W1*Wc*np.sin(z[0])) )]

time = np.arange(0, 1000, 0.01)

angle, velocity = odeint(q_derivatives, [0, W0], time).T 

plt.plot(time, angle+ W0*time , 'orange', linewidth = 2)
plt.xlabel('time (s)')
plt.ylabel('Angle(rad)')
plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
plt.grid(True)
