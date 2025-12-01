import numpy as np
import math as mt
from scipy.interpolate import make_interp_spline
import scipy.stats as stats
import matplotlib.pyplot as plt

xx = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
# xx is the number of counts in the preset interval
ff = [0, 1, 8, 18, 29, 22, 27, 31, 30, 19, 9, 4, 2, 1, 2, 2]
# ff is the number of times out of a total of fi = 200 that we get xi counts
xxff = []

xf = 0
for i in range(len(xx)):
    # Calculating total xx times ff
    xf = xf + (xx[i] * ff[i])
    xxff.append(xf)

#Sample Average x bar
xb = xf / 205

xxdif = []
xxdifs = []
pp = []
xxdp = []
for i in range(len(xx)):
    xdif = (xx[i] - xb)
    xdifs = (xx[i] - xb) ** 2
    p = ff[i] / 205
    xdp = p * xdifs
    xxdif.append(xdif)
    xxdifs.append(xdifs)
    pp.append(p)
    xxdp.append(xdp)

# Standard Deviation
s = 0
for i in range(len(xx)):
    s = s + xxdp[i]

sd = s ** (1 / 2)

print('Standard Deviation = ',sd,'\nMean = ', xb)

#error calculation
err = []
for i in range(len(xx)):
    errcal = ((pp[i]) ** (1 / 2)) * (205 ** (-0.5))
    err.append(errcal)

aa = np.linspace(0, 15, 1501)
bb = []
cc = []
for i in range(len(aa)):
    b = (xb ** aa[i]) * (mt.exp(-xb)) * ((mt.gamma(aa[i] + 1)) ** (-1))
    c = ((2*mt.pi*s)**(-0.5))*(mt.exp((-(aa[i]-xb)**(2))/(2*(sd**2))))
    bb.append(b)
    cc.append(c)
bbff=[]
ccff=[]
for i in range(0, 1501, 100):
    bbf=bb[i]
    ccf=cc[i]
    bbff.append(bbf)
    ccff.append(ccf)

#Chi-Squared Value Calculation
chi=0
chig=0
'''for i in range(len(pp)):
    chi=chi+((((pp[i]-bbff[i])**2)*205)/bbff[i])
    chig = chig + ((((pp[i] - ccff[i]) ** 2) * 205) / ccff[i])'''

poi=[]
goi=[]
for i in range(len(xx)):
    c1 = (xb ** xx[i]) * (mt.exp(-xb)) * ((mt.gamma(xx[i] + 1)) ** (-1))
    c2 = ((2 * mt.pi * s) ** (-0.5)) * (mt.exp((-(xx[i] - xb) ** (2)) / (2 * (sd ** 2))))
    e1 = 200 * c1
    e2 = 200 * c2
    pchi = ((ff[i]-e1)**2)/e1
    gchi = ((ff[i]-e2)**2)/e2
    poi.append(pchi)
    goi.append(gchi)

for i in range(len(poi)):
    chi = chi + poi[i]
    chig = chig + goi[i]

rt = stats.chi2.sf(chi,15)
rtg = stats.chi2.sf(chig,15)

print('Chi-Square Value(Poisson) = ',chi,'\nRight-Tail probability(Poisson) = ',rt)
print('Chi-Square Value(Gaussian) = ',chig,'\nRight-Tail probability(Gaussian) = ',rtg)

X_Y_Spline = make_interp_spline(xx, pp)
X_ = np.linspace(0, 9, 901)
Y_ = X_Y_Spline(X_)#

plt.plot(aa, bb, linewidth=1.1, label="Poisson", color='blue')
plt.plot(aa, cc, linewidth=1.1, label="Gaussian", color='purple')
#plt.plot(X_, Y_, linewidth=1.1, label="Data", color='red')
plt.errorbar(xx, pp, yerr=err, linewidth=1.1, fmt='.', capsize=3, color='red')
for i in range(0, 1501, 100):
    plt.scatter(aa[i], bb[i], marker='x', color='blue')
for i in range(0, 1501, 100):
    plt.scatter(aa[i], cc[i], marker='x', color='purple')

plt.legend()
plt.xlabel('Number of Background Counts')
plt.ylabel('Probability')
plt.title('Counting Statistic for 20 sec.')
plt.grid(color='green')
plt.show()