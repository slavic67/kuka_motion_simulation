from numpy import cos,sin
import matplotlib.pyplot as plt
step=6.28/16
dt=0.1
side='{} {} {}\n'.format(0,0,step)
count=0

x=[]
y=[]
with open('lab2_input_file.txt',mode='w',encoding='utf-8') as file:
        for i in range(1,161):
            file.write(side)
            x.append(cos(count))
            y.append(sin(count))
            count+=step*0.1

print(count)
plt.plot(x,y)
plt.grid()
plt.show()