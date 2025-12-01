import numpy as np
import math as mt
from scipy.interpolate import make_interp_spline
import scipy.stats as stats
import matplotlib.pyplot as plt

xx=[0,1,2,3,4,5,6]
# xx is the number of counts in the preset interval

ff=[45,54,56,28,12,4,1]
# ff is the number of times out of a total of fi = 200 that we get xi counts

xxff=[]

xf=0
for i in range(len(xx)):
    #Calculating total xx times ff
    xf=xf+(xx[i]*ff[i])
    xxff.append(xf)

#Sample Average x bar
xb=xf/200

xxdif=[]
xxdifs=[]
pp=[]
xxdp=[]
for i in range(len(xx)):
    xdif = (xx[i]-xb)
    xdifs = (xx[i]-xb)**2
    p = ff[i]/200
    xdp = p*xdifs
    xxdif.append(xdif)
    xxdifs.append(xdifs)
    pp.append(p)
    xxdp.append(xdp)

# Standard Deviation
s=0
for i in range(len(xx)):
    s = s + xxdp[i]

sd = s**(1/2)

print('Standard Deviation = ',sd,'\nMean = ', xb)

#error calculation
err=[]
for i in range(len(xx)):
    errcal = ((pp[i])**(1/2))*(200**(-0.5))
    err.append(errcal)

aa=np.linspace(0,6,601)
bb=[]

for i in range(len(aa)):
    b = (xb**aa[i])*(mt.exp(-xb))*((mt.gamma(aa[i]+1))**(-1))
    bb.append(b)

X_Y_Spline = make_interp_spline(xx,pp)
X_ = np.linspace(0,6,601)
Y_ = X_Y_Spline(X_)
bbff=[]
for i in range(0, 601, 100):
    bbf=bb[i]
    bbff.append(bbf)

plt.plot(aa,bb,linewidth = 1.1,label="Poisson",color='blue')
plt.plot(X_,Y_,linewidth = 1.1,label="Data",color='red')
plt.errorbar(xx,pp,yerr=err,linewidth = 1.1,fmt='.',capsize=3, color='red')
for i in range(0,601,100):
    plt.scatter(aa[i],bb[i],marker='x',color='blue')

#Chi-Squared Value Calculation
chi = 0

poi=[]
for i in range(len(xx)):
    c1 = (xb ** xx[i]) * (mt.exp(-xb)) * ((mt.gamma(xx[i] + 1)) ** (-1))
    e1= 200 * c1
    pchi = ((ff[i]-e1)**2)/e1
    poi.append(pchi)

for i in range(len(poi)):
    chi = chi + poi[i]

rt = stats.chi2.sf(chi,6)

print('Chi-Square Value = ',chi,'\nRight-Tail probability = ',rt)

plt.legend()
plt.xlabel('Number of Background Counts')
plt.ylabel('Probability')
plt.title('Counting Statistic for 5 sec.')
plt.grid(color='green')
plt.show()