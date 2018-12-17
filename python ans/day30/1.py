import scipy as sp
import scipy.optimize as ot
import numpy as np
import matplotlib.pyplot as plt

x = np.array([2,3,5,7,9])
y = np.array([4,5,7,10,15])

f = lambda m,x,c: m*x+c

popt,poc = ot.curve_fit(f,x,y)
vf = sp.vectorize(f)
yc = vf(popt[0],x,popt[1])

#vfxf = sp.vectorize(fxf)
#cy = vfxf(popt[0],x,popt[1])


plt.plot(x,y,'r:o',label = 'observed')
plt.plot(x,yc,'b-v',label = 'calc')
plt.legend(loc='best')
plt.show()