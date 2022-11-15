import matplotlib
from numpy import sqrt
import numpy as np
import matplotlib.pyplot as plt
from termcolor import cprint

class OutputFile():
    t=0
    omega_1=1,
    omega_2=2,
    omega_3=3,
    omega_4=4,
    M1=5,
    M2=6,
    M3=7,
    M4=8,
    Vx_o=9,
    Vy_o=10,
    dpsi=11,
    x0=12,
    y0=13,
    psi=14

dt=0.1
t=20


x_real_array=[]
y_real_array=[]
dpsi_real_array=[]
Vx_real_array=[]
Vy_real_array=[]
ddpsi_real_array=[]
M1=[]
M2=[]
M3=[]
M4=[]
omega_1=[]
omega_2=[]
omega_3=[]
omega_4=[]

with open('lab1_output.txt',"r",encoding='utf-8') as file:
    file.readline()
    for line in file:
        x_real_array.append(float(line.split()[12]))
        y_real_array.append(float(line.split()[13]))
        dpsi_real_array.append(float(line.split()[14]))
        Vx_real_array.append(float(line.split()[9]))
        Vy_real_array.append(float(line.split()[10]))
        ddpsi_real_array.append(float(line.split()[11]))
        M1.append(float(line.split()[5]))
        M2.append(float(line.split()[6]))
        M3.append(float(line.split()[7]))
        M4.append(float(line.split()[8]))
        omega_1.append(float(line.split()[1]))
        omega_2.append(float(line.split()[2]))
        omega_3.append(float(line.split()[3]))
        omega_4.append(float(line.split()[4]))

R=0.05
l=0.15
h=0.235

Fl=[]
Ft=[]
Vl=[]
Vt=[]

for i in range(0,t*10):
    Fl.append((M1[i]+M2[i]+M3[i]+M4[i])/R)
    Ft.append((-M1[i]+M2[i]+M3[i]-M4[i])/R)
    Vl.append((omega_1[i]+omega_2[i]+omega_3[i]+omega_4[i])/(4*R))
    Vt.append((-omega_1[i] + omega_2[i] + omega_3[i] - omega_4[i]) / (4 * R))

dVl=[0]
dVt=[0]
for i in range(1,t*10):
    dVl.append(Vl[i]-Vl[i-1])
    dVt.append(Vt[i]-Vt[i-1])

r=0.01
m=30

b=[]



for i in range(0,t*10):
    b.append(Fl[i]-m*dVl[i])
    b.append(Ft[i]-m*dVt[i])

b=np.array(b)

H=np.zeros(shape=(400,4))

for i in range(0,t*10,2):
    H[i][0]=Vl[i]
    H[i][1]=0
    H[i][2]=(-np.sign(omega_1[i])+np.sign(omega_2[i])+np.sign(omega_3[i])-np.sign(omega_4[i]))/R
    H[i][3]=0
    H[i+1][0]=0
    H[i+1][1]=Vt[i]
    H[i+1][2]=(-np.sign(omega_1[i])+np.sign(omega_2[i])+np.sign(omega_3[i])-np.sign(omega_4[i]))/R
    H[i+1][3]=4*1.4*np.sign(Vt[i])/r


print(np.linalg.inv(H.T@H)@H.T@b)