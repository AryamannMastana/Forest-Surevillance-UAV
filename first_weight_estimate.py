import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

We = np.array([2.5,4,4.03,5.1,5.3,6.58,7.4,7.7])
Wp = np.array([1,1.1,1.5,1.6,1,1.2,1.2,1.2])
W0 = np.array([5,7.5,8.6,10,13,13.5,15,15.5])
Wb = np.array([1.5,2.36,2.56,3.3,6.7,4.72,5.1,5.1])
Wb_by_W0 = np.divide(Wb, W0)
We_by_W0 = np.divide(We, W0)
print(np.average(Wb_by_W0))
plt.plot(W0, Wb_by_W0, color = 'red', label = 'Curve Fit')
# def curve(W0,a,c):
#     return a*pow(W0,c)
# popt, _ = curve_fit(curve, W0, We_by_W0)
# a,c = popt
# print(a)
# print(c)
# plt.scatter(W0, We_by_W0, label = 'Actual Points')
# plt.plot(W0, curve(W0,a,c), color = 'red', label = 'Curve Fit')
# plt.ylabel('Empty weight fraction We/W0')
# plt.xlabel('Maximum takeoff weight W0(kg)')
# plt.title('We/W0 vs W0')
# plt.tight_layout()
# plt.legend()
# plt.xticks()
# plt.yticks()
plt.show()
