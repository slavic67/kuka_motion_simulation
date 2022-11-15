_v=0.25
_t=11.3
_R=0.45


vx=_v
vy=0
omega=_v/_R

with open("lab3_brig_4.txt","w",encoding='utf-8') as file:
    for i in range(1,114):
        file.write("{} {} {}\n".format(vx,vy,round(omega,3)))

