import numpy as np
import math as mt
import matplotlib.pyplot as plt

"""Voltage"""
vv=[325,350,358,367,375,380,400,425,450,475,500,525,550,575,600,625,650,675,700,750]

"""Background Counts"""
bc=[0,30,32,30,34,34,28,37,44,45,27,44,31,31,34,45,40,30,31,46]

"""Total Counts"""
tc=[0,198,376,410,408,380,364,469,412,494,492,488,440,522,487,482,479,518,516,516]

"""Net Counts"""
nc=[]

n=len(vv)-2

for i in range(len(vv)):
    ncal=tc[i]-bc[i]
    nc.append(ncal)

print('Net counts = ',nc)

sumx=0
sumy=0
sumxy=0
sumx2=0

for i in range(2,len(vv)):
   sumx= sumx+vv[i]
   sumy= sumy + nc[i]
   sumxy= sumxy + (vv[i]*nc[i])
   sumx2 = sumx2 + (vv[i]*vv[i])
gm1= ((n*sumxy)-(sumx*sumy))/((n*sumx2)-(sumx**2))
c1= ((sumx2*sumy)-(sumx*sumxy))/((n*sumx2)-(sumx**2))

print('Slope = ',gm1,'\nConstant = ',c1)
yy=[]

for i in range(2,len(vv)):
   ycal=gm1*vv[i]+c1
   yy.append(ycal)
xx=[]
for i in range(2,len(vv)):
   xcal=vv[i]
   xx.append(xcal)

err=[]
for i in range(len(vv)):
    errcal = (tc[i]+bc[i])**(1/2)
    err.append(round(errcal))

print('Error = ',err)

plt.errorbar(vv,nc,yerr=err,fmt='.', color='blue')
plt.plot(xx,yy)
plt.legend(['Best Line Fit','Error Bar'])
plt.xlabel("Volatage")
plt.ylabel("Net counts")
plt.title("GM Plateau Best Fit")
plt.grid()
plt.show()