import numpy
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
t=11


x_real_array=[]
y_real_array=[]
dpsi_real_array=[]
Vx_real_array=[]
Vy_real_array=[]
ddpsi_real_array=[]

with open('lab3_brig4_12a.txt',"r",encoding='utf-8') as file:
    file.readline()
    for line in file:
        x_real_array.append(float(line.split()[12]))
        y_real_array.append(float(line.split()[13]))
        dpsi_real_array.append(float(line.split()[14]))
        Vx_real_array.append(float(line.split()[9]))
        Vy_real_array.append(float(line.split()[10]))
        ddpsi_real_array.append(float(line.split()[11]))

x_id_array=[0]
y_id_array=[0]
dpsi_id_array=[0]
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


for i in range(1,len(Vx_id_array)):
    x_id_array.append(x_id_array[i-1]+0.1*Vx_id_array[i-1]*np.cos(dpsi_id_array[i-1]))
    y_id_array.append(y_id_array[i-1] + 0.1*Vx_id_array[i-1]*np.sin(dpsi_id_array[i-1]))
    dpsi_id_array.append(dpsi_id_array[i-1]+0.1*ddpsi_id_array[i-1])



dX_array=[]
dY_array=[]
delPsi_array=[]
dVx_array=[]
dVy_array=[]
ddPsi_array=[]

for i in range(0,t*10):
    dX_array.append(x_id_array[i]-x_real_array[i])
    dY_array.append(y_id_array[i]-y_real_array[i])
    delPsi_array.append(dpsi_id_array[i]-dpsi_real_array[i])
    ddPsi_array.append(ddpsi_id_array[i]-ddpsi_real_array[i])
    dVx_array.append(Vx_id_array[i]-Vx_real_array[i])
    dVy_array.append(Vy_id_array[i]-Vy_real_array[i])






integrals_dVx=[]
integrals_dVy=[]
integrals_ddpsi=[]

integrals_dVx.append(dVx_array[0]*0.1)
integrals_dVy.append(dVy_array[0]*0.1)
integrals_ddpsi.append(ddPsi_array[0]*0.1)

for i in range (1,t*10):
    integrals_dVx.append(dVx_array[i]*0.1+integrals_dVx[i-1])
    integrals_dVy.append(dVy_array[i]*0.1 + integrals_dVy[i - 1])
    integrals_ddpsi.append(ddPsi_array[i]*0.1 + integrals_ddpsi[i - 1])

B=[]

for i in range(0,t*10):
    B.append(dX_array[i]-integrals_dVx[i]*0.1)
    B.append(dY_array[i]-integrals_dVy[i]*0.1)
    B.append(delPsi_array[i]-integrals_ddpsi[i]*0.1)



A=[]
for i in range(0,t*10):
    A.append(Vx_id_array[i])
    A.append(Vy_id_array[i])
    A.append(dpsi_id_array[i])




A_mat=numpy.array(A)
A_mat=A_mat.T

B_mat=numpy.array(B)
B_mat=B_mat.T


dtzap=float(1/(A_mat.T @ A_mat))*float(A_mat.T@B_mat)

cprint("время запаздывания равно: {} секунд".format(round(dtzap,3)),"green")


x_vost=[]
y_vost=[]
psi_vost=[]
for i in range(0,t*10):
    x_vost.append(x_real_array[i]-Vx_id_array[i]*dtzap+integrals_dVx[i])
    y_vost.append(y_real_array[i]-Vy_id_array[i]*dtzap+integrals_dVy[i])
    psi_vost.append(dpsi_real_array[i]-ddpsi_id_array[i]*dtzap+integrals_ddpsi[i])




# модель 2
#
#4b
# print("средне квадратичное отклонение dvx: ",(numpy.array(dVx_array)).std())
# print("средне квадратичное отклонение dvy: ",(numpy.array(dVy_array)).std())
# print("средне квадратичное отклонение ddpsi: ",(numpy.array(ddPsi_array)).std())
#
#
# print("математическое ожидание dvx равно: ",sum(dVx_array)/(len(dVx_array)))
# print("математическое ожидание dvy равно: ",sum(dVy_array)/len(dVy_array))
# print("математическое ожидание ddpsi равно: ",sum(ddPsi_array)/len(ddPsi_array))
#
# print('дисперсия dvx равна',np.var(dVx_array))
# print('дисперсия dvy равна',np.var(dVy_array))
# print('дисперсия ddpsi равна',np.var(ddPsi_array))
#
#
# #4c
# print("средне квадратичное отклонение dx: ",(numpy.array(dX_array)).std())
# print("средне квадратичное отклонение dy: ",(numpy.array(dY_array)).std())
# print("средне квадратичное отклонение dpsi: ",(numpy.array(delPsi_array)).std())
#
#
# print("математическое ожидание dx равно: ",sum(dX_array)/(len(dX_array)))
# print("математическое ожидание dy равно: ",sum(dY_array)/len(dY_array))
# print("математическое ожидание dpsi равно: ",sum(delPsi_array)/len(delPsi_array))
# #
# fig=plt.figure(figsize=(7,4))
# fig.suptitle('отклонение dx')
# ax1=fig.add_subplot()
#
# ax1.set_xlabel('step')
# ax1.set_ylabel('delta,m')
# ax1.grid()
# ax1.plot(dX_array)
# #
# fig1=plt.figure(figsize=(7,4))
# fig1.suptitle('отклонение dy')
# ax1=fig1.add_subplot()
#
# ax1.set_xlabel('step')
# ax1.set_ylabel('delta,m')
# ax1.grid()
# ax1.plot(dY_array)

# fig2=plt.figure(figsize=(7,4))
# fig2.suptitle('отклонение dpsi')
# ax1=fig2.add_subplot()
#
# ax1.set_xlabel('step')
# ax1.set_ylabel('delta,rad')
# ax1.grid()
# ax1.plot(delPsi_array)
#
#
#
# #4d
dX_vost=numpy.array(x_id_array)[0:110]-numpy.array(x_vost)[0:110]
dY_vost=numpy.array(y_id_array)[0:110]-numpy.array(y_vost)[0:110]
dPSI_vost=numpy.array(dpsi_id_array)[0:110]-numpy.array(psi_vost)[0:110]
# print("ско разности идеальных и восстановленных x: ",dX_vost.std())
# print("ско разности идеальных и восстановленных y: ",dY_vost.std())
# print("ско разности идеальных и восстановленных dpsi: ",dPSI_vost.std())
# print("математическое ожидание разности идеальных и восстановленных x равно: ",sum(dX_vost)/len(dX_vost))
# print("математическое ожидание разности идеальных и восстановленных y равно: ",sum(dY_vost)/len(dY_vost))
# print("математическое ожидание разности идеальных и восстановленных psi равно: ",sum(dPSI_vost)/len(dPSI_vost))
#
#
# fig=plt.figure(figsize=(7,4))
# fig.suptitle('отклонение dx')
# ax1=fig.add_subplot()
#
# ax1.set_xlabel('step')
# ax1.set_ylabel('delta,m')
# ax1.grid()
# ax1.plot(dX_vost)
#
# fig1=plt.figure(figsize=(7,4))
# fig1.suptitle('отклонение dy')
# ax1=fig1.add_subplot()
#
# ax1.set_xlabel('step')
# ax1.set_ylabel('delta,m')
# ax1.grid()
# ax1.plot(dY_vost)
#
# fig2=plt.figure(figsize=(7,4))
# fig2.suptitle('отклонение dpsi')
# ax1=fig2.add_subplot()
#
# ax1.set_xlabel('step')
# ax1.set_ylabel('delta,rad')
# ax1.grid()
# ax1.plot(dPSI_vost)
#
#
#
#
#
#
#
#
#
#
#
#
#
# #построение графиков
#
# fig=plt.figure(figsize=(7,4))
# fig.suptitle('траектория восстановленных координат')
# ax1=fig.add_subplot()
#
# ax1.set_xlabel('X,m')
# ax1.set_ylabel('Y,m')
# ax1.grid()
# ax1.plot(x_vost,y_vost)
# #
# #
# #
# # fig1=plt.figure(figsize=(7,4))
# # fig1.suptitle('график реальных координат')
# # ax2=fig1.add_subplot()
# #
# # ax2.set_xlabel('X,m')
# # ax2.set_ylabel('Y,m')
# # ax2.grid()
# # ax2.plot(x_real_array,y_real_array)
# #
# #
# #
# #
# # fig2=plt.figure(figsize=(7,4))
# # fig2.suptitle('график идеальных координат')
# # ax3=fig2.add_subplot()
# #
# # ax3.set_xlabel('X,m')
# # ax3.set_ylabel('Y,m')
# # ax3.grid()
# # ax3.plot(x_id_array,y_id_array)
# #
# #
# #
fig3=plt.figure(figsize=(7,4))
fig3.suptitle('все траектории вместе')
ax4=fig3.add_subplot()
#
#
ax4.set_xlabel('X,m')
ax4.set_ylabel('Y,m')
ax4.grid()
ax4.plot(x_vost,y_vost,x_id_array,y_id_array,x_real_array,y_real_array)



ax4.legend(['восстановленные','идеальные','реальные'])
#
#
plt.show()