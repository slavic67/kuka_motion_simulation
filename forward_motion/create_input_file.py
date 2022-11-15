import numpy
import matplotlib
from numpy import sqrt
import numpy as np
import matplotlib.pyplot as plt

time=20
dt=0.1
v=0.1
length=2
a=length/5
omega=0
# 1 side
vx1=a/4
vy1=0
# 2 side
vy2=a/4
vx2=0
# 3 side
vx3=round(0.1*np.cos(120/180*np.pi),3)
vy3=round(0.1*np.sin(120/180*np.pi),3)
# 4 side
vx4=round(0.1*np.cos(240/180*np.pi),3)
vy4=round(0.1*np.sin(240/180*np.pi),3)
# 5 side
vy5=-a/4
vx5=0

print(vx1,vy1)
print(vx2,vy2)
print(vx3,vy3)
print(vx4,vy4)
print(vx5,vy5)

side1='{} {} {}\n'.format(vx1,vy1,omega)
side2='{} {} {}\n'.format(vx2,vy2,omega)
side3='{} {} {}\n'.format(vx3,vy3,omega)
side4='{} {} {}\n'.format(vx4,vy4,omega)
side5='{} {} {}\n'.format(vx5,vy5,omega)
sides=[side1,side2,side3,side4,side5]

with open('lab1_input.txt',mode='w',encoding='utf-8') as file:
    for side in sides:
        for i in range(1,41):
            file.write(side)



vx_array=[]
vy_array=[]
x=[0]
y=[0]
with open('lab1_input.txt',mode='r',encoding='utf-8') as file:
    for line in file:
        vx,vy,om=line.split()
        vx=float(vx)
        vy=float(vy)
        vx_array.append(vx)
        vy_array.append(vy)

# print(vx_array)
# print(vy_array)

for i in range(1,len(vx_array)):
    x.append(x[i-1]+0.1*vx_array[i-1])
    y.append(y[i-1] + 0.1 * vy_array[i-1])

# print(x)
# print(y)

plt.plot(x,y)
plt.grid()
plt.show()






