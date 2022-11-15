import numpy
import matplotlib
from numpy import sqrt
import numpy as np
import matplotlib.pyplot as plt
from termcolor import cprint

t=11


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


phi1_real_array=[]
phi2_real_array=[]
phi3_real_array=[]
phi4_real_array=[]
Vx_real_array=[]
Vy_real_array=[]
ddpsi_real_array=[]

with open('lab3_brig4_12a.txt',"r",encoding='utf-8') as file:
    file.readline()
    for line in file:
        phi1_real_array.append(float(line.split()[1]))
        phi2_real_array.append(float(line.split()[2]))
        phi3_real_array.append(float(line.split()[3]))
        phi4_real_array.append(float(line.split()[4]))
        Vx_real_array.append(float(line.split()[9]))
        Vy_real_array.append(float(line.split()[10]))
        ddpsi_real_array.append(float(line.split()[11]))


Vx_id_array=[]
Vy_id_array=[]
ddpsi_id_array=[]


with open('lab3_brig_4.txt',mode='r',encoding='utf-8') as file:
    for line in file:
        vx,vy,om=line.split()
        om=float(om)
        vx=float(vx)
        vy=float(vy)
        Vx_id_array.append(vx)
        Vy_id_array.append(vy)
        ddpsi_id_array.append(om)


omega1_id_array=[]
omega2_id_array=[]
omega3_id_array=[]
omega4_id_array=[]

R=0.05
h=0.235
l=0.15

for i in range(0,t*10):
    omega1_id_array.append(1/R*(Vx_id_array[i]-Vy_id_array[i]-(l+h)*ddpsi_id_array[i]))
    omega2_id_array.append(1 / R * (Vx_id_array[i] + Vy_id_array[i] + (l + h) * ddpsi_id_array[i]))
    omega3_id_array.append(1 / R * (Vx_id_array[i] + Vy_id_array[i] - (l + h) * ddpsi_id_array[i]))
    omega4_id_array.append(1 / R * (Vx_id_array[i] - Vy_id_array[i] + (l + h) * ddpsi_id_array[i]))

dphi1=[]
dphi2=[]
dphi3=[]
dphi4=[]

for i in range(0,t*10):
    dphi1.append(omega1_id_array[i]-phi1_real_array[i])
    dphi2.append(omega2_id_array[i] - phi2_real_array[i])
    dphi3.append(omega3_id_array[i] - phi3_real_array[i])
    dphi4.append(omega4_id_array[i] - phi4_real_array[i])

x_id_array=[0]
y_id_array=[0]

for i in range(1,len(Vx_id_array)):
    x_id_array.append(x_id_array[i-1]+0.1*Vx_id_array[i-1])
    y_id_array.append(y_id_array[i-1] + 0.1*Vy_id_array[i-1])


#4a

# fig=plt.figure(figsize=(7,4))
# fig.suptitle('first wheel')
# ax1=fig.add_subplot()
# ax1.set_xlabel('step')
# ax1.set_ylabel('delta,rad/s')
# ax1.grid()
# ax1.plot(dphi1)

# fig1=plt.figure(figsize=(7,4))
# fig1.suptitle('second wheel')
# ax1=fig1.add_subplot()
# ax1.set_xlabel('step')
# ax1.set_ylabel('delta,rad/s')
# ax1.grid()
# ax1.plot(dphi2)
#
# fig2=plt.figure(figsize=(7,4))
# fig2.suptitle('third wheel')
# ax1=fig2.add_subplot()
# ax1.set_xlabel('step')
# ax1.set_ylabel('delta,rad/s')
# ax1.grid()
# ax1.plot(dphi3)
#
fig3=plt.figure(figsize=(7,4))
fig3.suptitle('fourth wheel')
ax1=fig3.add_subplot()
ax1.set_xlabel('step')
ax1.set_ylabel('delta,rad/s')
ax1.grid()
ax1.plot(dphi4)

plt.show()