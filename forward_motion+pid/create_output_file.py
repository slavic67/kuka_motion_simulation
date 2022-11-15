import numpy as np
import matplotlib.pyplot as plt
t=20
dt=0.1

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


Vx_real_array=[]
Vy_real_array=[]
ddpsi_real_array=[]
x_real_array=[]
y_real_array=[]
dpsi_real_array=[]


with open('lab1_output.txt',"r",encoding='utf-8') as file:
    file.readline()
    for line in file:
        Vx_real_array.append(float(line.split()[9]))
        Vy_real_array.append(float(line.split()[10]))
        ddpsi_real_array.append(float(line.split()[11]))
        x_real_array.append(float(line.split()[12]))
        y_real_array.append(float(line.split()[13]))
        dpsi_real_array.append(float(line.split()[14]))

Vx_id_array=[]
Vy_id_array=[]
ddpsi_id_array=[]
x_id_array=[0]
y_id_array=[0]
psi_id_array=[0]

with open('lab1_input.txt',mode='r',encoding='utf-8') as file:
    for line in file:
        vx,vy,om=line.split()
        om=float(om)
        vx=float(vx)
        vy=float(vy)
        Vx_id_array.append(vx)
        Vy_id_array.append(vy)
        ddpsi_id_array.append(om)

for i in range(1,t*10):
    x_id_array.append(x_id_array[i-1]+0.1*Vx_id_array[i-1])
    y_id_array.append(y_id_array[i-1] + 0.1 * Vy_id_array[i-1])
    psi_id_array.append(psi_id_array[i - 1] + 0.1 * ddpsi_id_array[i - 1])



dVx=[]
dVy=[]
dOm=[]

for i in range(0,t*10):
    dVx.append(-Vx_id_array[i]+Vx_real_array[i])
    dVy.append(-Vy_id_array[i]+Vy_real_array[i])
    dOm.append(-ddpsi_id_array[i]+ddpsi_real_array[i])

ddVx=[0]
ddVy=[0]
ddOm=[0]

for i in range(1,t*10):
    ddVx.append((dVx[i]-dVx[i-1])/dt)
    ddVy.append((dVy[i]-dVy[i-1]) / dt)
    ddOm.append((dOm[i]-dOm[i-1])/dt)

#строим контур управления

#ось x
# шаг 0
Vxu=[Vx_id_array[0]]
Xp=[0]
# шаг 1
Vxp=[0,Vx_id_array[1]+ddVx[1]*dt]
Xp.append(Vxp[1]*dt+Xp[0])
Vxu.append(Vx_id_array[1]+Vx_id_array[1]-Vxp[1]+(x_id_array[1]-Xp[1])/dt)

for i in range(2,t*10):
    Vxp.append(Vx_id_array[i]+ddVx[i]*dt)
    Xp.append(Vxp[i]*dt+Xp[i-1])
    Vxu.append(Vx_id_array[i]+0.25*(Vx_id_array[i]-Vxp[i])+(x_id_array[i]-Xp[i])/dt)

#ось y
#шаг 0
Vyu=[Vy_id_array[0]]
Yp=[0]
#шаг 1
Vyp=[0,Vy_id_array[1]+ddVy[1]*dt]
Yp.append(Vyp[1]*dt+Yp[0])
Vyu.append(Vy_id_array[1]+Vy_id_array[1]-Vyp[1]+(y_id_array[1]-Yp[1])/dt)

for i in range(2,t*10):
    Vyp.append(Vy_id_array[i]+ddVy[i]*dt)
    Yp.append(Vyp[i]*dt+Yp[i-1])
    Vyu.append(Vy_id_array[i]+0.25*(Vy_id_array[i]-Vyp[i])+(y_id_array[i]-Yp[i])/dt)

#ось z
#шаг 0
Omu=[ddpsi_id_array[0]]
Psip=[0]
#шаг 1
Omp=[0,ddpsi_id_array[1]+ddOm[1]*dt]
Psip.append(Omp[1]*dt+Psip[0])
Omu.append(ddpsi_id_array[1]+ddpsi_id_array[1]-Omp[1]+(psi_id_array[1]-Psip[1])/dt)

for i in range(2,t*10):
    Omp.append(ddpsi_id_array[i]+ddOm[i]*dt)
    Psip.append(Omp[i]*dt+Psip[i-1])
    Omu.append(ddpsi_id_array[i]+0.25*(ddpsi_id_array[i]-Omp[i])+(psi_id_array[i]-Psip[i])/dt)



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
#НСК
Vx_real_nsk=[]
Vy_real_nsk=[]
Psi_real_nsk=dpsi_real_array
Om_real_nsk=ddpsi_real_array
X_real_nsk=x_real_array
Y_real_nsk=y_real_array

for i in range(0,t*10):
    Vx_real_nsk.append(Vx_real_array[i]*np.cos(dpsi_real_array[i]*np.pi)-Vy_real_array[i]*np.sin(dpsi_real_array[i]*np.pi))
    Vy_real_nsk.append(Vx_real_array[i]*np.sin(dpsi_real_array[i]*np.pi)+Vy_real_array[i]*np.cos(dpsi_real_array[i]*np.pi))

Psi_id_nsk=psi_id_array
Om_id_nsk=ddpsi_id_array
Vx_id_nsk=[]
Vy_id_nsk=[]

for i in range(0,t*10):
    Vx_id_nsk.append(Vx_id_array[i]*np.cos(Psi_id_nsk[i]*np.pi)-Vy_id_array[i]*np.sin(Psi_id_nsk[i]*np.pi))
    Vy_id_nsk.append(Vx_id_array[i]*np.sin(Psi_id_nsk[i]*np.pi)+Vy_id_array[i]*np.cos(Psi_id_nsk[i]*np.pi))

X_id_nsk=[0]
Y_id_nsk=[0]
for i in range(1,t*10):
    X_id_nsk.append(X_id_nsk[i-1]+0.1*Vx_id_nsk[i-1])
    Y_id_nsk.append(Y_id_nsk[i-1] + 0.1 * Vy_id_nsk[i-1])


dVx_nsk=[]
dVy_nsk=[]
dOm_nsk=[]

for i in range(0,t*10):
    dVx_nsk.append(-Vx_id_nsk[i]+Vx_real_nsk[i])
    dVy_nsk.append(-Vy_id_nsk[i]+Vy_real_nsk[i])
    dOm_nsk.append(-Om_id_nsk[i]+Om_real_nsk[i])

ddVx_nsk=[0]
ddVy_nsk=[0]
ddOm_nsk=[0]

for i in range(1,t*10):
    ddVx_nsk.append((dVx_nsk[i]-dVx_nsk[i-1])/dt)
    ddVy_nsk.append((dVy_nsk[i]-dVy_nsk[i-1]) / dt)
    ddOm_nsk.append((dOm_nsk[i]-dOm_nsk[i-1])/dt)


#строим контур управления

#ось x
# шаг 0
Vxu_nsk=[Vx_id_nsk[0]]
Xp_nsk=[0]
# шаг 1
Vxp_nsk=[0,Vx_id_nsk[1]+ddVx_nsk[1]*dt]
Xp_nsk.append(Vxp_nsk[1]*dt+Xp_nsk[0])
Vxu_nsk.append(Vx_id_nsk[1]+Vx_id_nsk[1]-Vxp_nsk[1]+(X_id_nsk[1]-Xp_nsk[1])/dt)

for i in range(2,t*10):
    Vxp_nsk.append(Vx_id_nsk[i]+ddVx_nsk[i]*dt)
    Xp_nsk.append(Vxp_nsk[i]*dt+Xp_nsk[i-1])
    Vxu_nsk.append(Vx_id_nsk[i]+0.25*(Vx_id_nsk[i]-Vxp_nsk[i])+(X_id_nsk[i]-Xp_nsk[i])/dt)


#ось y
# шаг 0
Vyu_nsk=[Vy_id_nsk[0]]
Yp_nsk=[0]
# шаг 1
Vyp_nsk=[0,Vy_id_nsk[1]+ddVy_nsk[1]*dt]
Yp_nsk.append(Vyp_nsk[1]*dt+Yp_nsk[0])
Vyu_nsk.append(Vy_id_nsk[1]+Vy_id_nsk[1]-Vyp_nsk[1]+(Y_id_nsk[1]-Yp_nsk[1])/dt)

for i in range(2,t*10):
    Vyp_nsk.append(Vy_id_nsk[i]+ddVy_nsk[i]*dt)
    Yp_nsk.append(Vyp_nsk[i]*dt+Yp_nsk[i-1])
    Vyu_nsk.append(Vy_id_nsk[i]+0.25*(Vy_id_nsk[i]-Vyp_nsk[i])+(Y_id_nsk[i]-Yp_nsk[i])/dt)


#ось z
#шаг 0
Omu_nsk=[Om_id_nsk[0]]
Psip_nsk=[0]
#шаг 1
Omp_nsk=[0,Om_id_nsk[1]+ddOm_nsk[1]*dt]
Psip_nsk.append(Omp_nsk[1]*dt+Psip_nsk[0])
Omu_nsk.append(Om_id_nsk[1]+Om_id_nsk[1]-Omp_nsk[1]+(Psi_id_nsk[1]-Psip_nsk[1])/dt)

for i in range(2,t*10):
    Omp_nsk.append(Om_id_nsk[i]+ddOm_nsk[i]*dt)
    Psip_nsk.append(Omp_nsk[i]*dt+Psip_nsk[i-1])
    Omu_nsk.append(Om_id_nsk[i]+0.25*(Om_id_nsk[i]-Omp_nsk[i])+(Psip_nsk[i]-Psip_nsk[i])/dt)

#
#
#
#НСК
#разность идеальных и реальных координат
dX_ip_nsk=np.array(X_real_nsk)-np.array(X_id_nsk)
dY_ip_nsk=np.array(Y_real_nsk)-np.array(Y_id_nsk)
dPSI_ip_nsk=np.array(Psi_id_nsk)-np.array(Psi_real_nsk)

#разность идеальных и восстановленных координат
dX_ios_nsk=np.array(X_id_nsk)-np.array(Xp_nsk)
dY_ios_nsk=np.array(X_id_nsk)-np.array(Yp_nsk)
DPSI_ios_nsk=np.array(Psi_id_nsk)-np.array(Psip_nsk)

# print("Для нск")
# print("ско разности идеальных и реальных x: ",dX_ip_nsk.std())
# print("ско разности идеальных и восстановленных х: ",dX_ios_nsk.std())
# print("ско разности идеальных и реальных y: ",dY_ip_nsk.std())
# print("ско разности идеальных и восстановленных у: ",dY_ios_nsk.std())
# print("ско разности идеальных и реальных psi: ",dPSI_ip_nsk.std())
# print("ско разности идеальных и восстановленных psi: ",DPSI_ios_nsk.std())
#
#
# print("математическое ожидание разности идеальных и реальных x равно: ",sum(dX_ip_nsk)/len(dX_ip_nsk))
# print("математическое ожидание  разности идеальных и восстановленных х  равно: ",sum(dX_ios_nsk)/len(dX_ios_nsk))
# print("математическое ожидание разности идеальных и реальных y равно: ",sum(dY_ip_nsk)/len(dY_ip_nsk))
# print("математическое ожидание  разности идеальных и восстановленных y  равно: ",sum(dY_ios_nsk)/len(dY_ios_nsk))
# print("математическое ожидание разности идеальных и реальных psi равно: ",sum(dPSI_ip_nsk)/len(dPSI_ip_nsk))
# print("математическое ожидание  разности идеальных и восстановленных psi  равно: ",sum(DPSI_ios_nsk)/len(DPSI_ios_nsk))

#
#
#ССК
#разность идеальных и реальных координат
dX_ip=np.array(x_real_array)-np.array(x_id_array)
dY_ip=np.array(y_real_array)-np.array(y_id_array)
dPSI_ip=np.array(psi_id_array)-np.array(dpsi_real_array)

#разность идеальных и восстановленных координат
dX_ios=np.array(x_id_array)-np.array(Xp)
dY_ios=np.array(x_id_array)-np.array(Yp)
DPSI_ios=np.array(psi_id_array)-np.array(Psip)

# print("для сск")
# print("ско разности идеальных и реальных x: ",dX_ip.std())
# print("ско разности идеальных и восстановленных х: ",dX_ios.std())
# print("ско разности идеальных и реальных y: ",dY_ip.std())
# print("ско разности идеальных и восстановленных у: ",dY_ios.std())
# print("ско разности идеальных и реальных psi: ",dPSI_ip.std())
# print("ско разности идеальных и восстановленных psi: ",DPSI_ios.std())
#
#
# print("математическое ожидание разности идеальных и реальных x равно: ",sum(dX_ip)/len(dX_ip))
# print("математическое ожидание  разности идеальных и восстановленных х  равно: ",sum(dX_ios)/len(dX_ios))
# print("математическое ожидание разности идеальных и реальных y равно: ",sum(dY_ip)/len(dY_ip))
# print("математическое ожидание  разности идеальных и восстановленных y  равно: ",sum(dY_ios)/len(dY_ios))
# print("математическое ожидание разности идеальных и реальных psi равно: ",sum(dPSI_ip)/len(dPSI_ip))
# print("математическое ожидание  разности идеальных и восстановленных psi  равно: ",sum(DPSI_ios)/len(DPSI_ios))
#
#

x_youbot=[]
y_youbot=[]
psi_youbot=[]
#снимаем данные с робота
with open('lab4_output.txt',"r",encoding='utf-8') as file:
    file.readline()
    for line in file:
        x_youbot.append(float(line.split()[12]))
        y_youbot.append(float(line.split()[13]))
        psi_youbot.append(float(line.split()[14]))


fig=plt.figure(figsize=(7,4))
ax1=fig.add_subplot()
# по x
# fig.suptitle('разность реальных и идеальных координат по оси x')
# ax1.set_xlabel('номер итерации')
# ax1.set_ylabel('разница, м')
# ax1.plot(dX_ip)
#
# fig.suptitle('разность оос и идеальных координат по оси x')
# ax1.set_xlabel('номер итерации')
# ax1.set_ylabel('разница, м')
# ax1.plot(dX_ios)

# по у
# fig.suptitle('разность реальных и идеальных координат по оси y')
# ax1.set_xlabel('номер итерации')
# ax1.set_ylabel('разница, м')
# ax1.plot(dY_ip)

# fig.suptitle('разность оос и идеальных координат по оси y')
# ax1.set_xlabel('номер итерации')
# ax1.set_ylabel('разница, м')
# ax1.plot(dY_ios)
# по z
# fig.suptitle('разность реальных и идеальных координат по оси z')
# ax1.set_xlabel('номер итерации')
# ax1.set_ylabel('разница, м')
# ax1.plot(dPSI_ip)
#
# fig.suptitle('разность оос и идеальных координат по оси z')
# ax1.set_xlabel('номер итерации')
# ax1.set_ylabel('разница, м')
# ax1.plot(DPSI_ios)

#траектории
# fig.suptitle('угол поворота робота')
# ax1.set_xlabel('номер итерации')
# ax1.set_ylabel('угол, рад')
# ax1.plot(psi_id_array)
# ax1.plot(dpsi_real_array)
# ax1.plot(Psip)
# fig.suptitle('траектория робота')
# ax1.set_xlabel('X,m')
# ax1.set_ylabel('Y,m')
# ax1.plot(x_id_array,y_id_array)
# ax1.plot(x_real_array,y_real_array)
# ax1.plot(Xp,Yp)
# ax1.legend(['идеальный','реальный','оос'])

#разность сск и нск
# fig.suptitle('разность углов при применении ос в ССК и НСК')
# ax1.plot(np.array(Psip)-np.array(Psip_nsk))
# ax1.set_xlabel('номер итерации')
# ax1.set_ylabel('отклонение, рад')

#разность прогноза и реальной оос
fig.suptitle('график прогноза по оос и реальной оос')
ax1.plot(Xp,Yp)
ax1.plot(x_youbot,y_youbot)
ax1.set_xlabel('X,m')
ax1.set_ylabel('Y,m')
ax1.legend(['прогноз оос','реальная оос'])

ax1.grid()
plt.show()


