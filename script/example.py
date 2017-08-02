import spolynom , psfpoly , fitting , moment , profile 
import numpy as np

#np.random.seed(114)
import numpy as np
import scipy 

#486
#41
#35
#786
#56
#2389
size = 17 
xmin, xmax = size/2, size/2+1
ymin, ymax = size/2, size/2+1
f1, f2 = 2. , 4.
s1 , s2 = 5., 100.
sample = 4

##housekeeping : sigma = .478*np.array([f1*s1, f2*s1, f1*s2, f2*s2])**-1.
xx = np.random.uniform(xmin, xmax, sample)
yy = np.random.uniform(ymin, ymax, sample)  
F = np.array([f1,f2,f1,f2])
SNR = np.array([s1,s1,s2,s2])
sigma = .478/(F*SNR)

"""
noise1 = np.random.normal(0. , sigma[0] , (size , size))
noise2 = np.random.normal(0. , sigma[1] , (size , size))
noise3 = np.random.normal(0. , sigma[2] , (size , size))
noise4 = np.random.normal(0. , sigma[3] , (size , size))
"""
data1  = profile.makeMoffat(size , 2. , 2.5 , (xx[0] , yy[0])) + np.random.normal(0. , .478/(2.*10.) , (size , size))
data2  = profile.makeMoffat(size , 4. , 2.5 , (xx[1] , yy[1])) + np.random.normal(0. , .478/(4.*10.) , (size , size))
"""
np.savetxt("data1.txt" , data1.flatten() , fmt = '%.12f')
np.savetxt("data2.txt" , data2.flatten() , fmt = '%.12f')
x1 = np.savetxt("x1.txt" , np.array([xx[0] , yy[0]]) , fmt = '%.12f')
x2 = np.savetxt("x2.txt" , np.array([xx[1] , yy[1]]) , fmt = '%.12f')

data1 = np.loadtxt("data1.txt").reshape(17,17)
data2 = np.loadtxt("data2.txt").reshape(17,17)
xx[0] , yy[0] = np.loadtxt("x1.txt")[0] , np.loadtxt("x1.txt")[1]
xx[1] , yy[1] = np.loadtxt("x2.txt")[0] , np.loadtxt("x2.txt")[1]
"""
data3  = profile.makeMoffat(size , 2. , 2.5 , (xx[2] , yy[2])) + np.random.normal(0. , .478/(2.*20.) , (size , size))
data4  = profile.makeMoffat(size , 4. , 2.5 , (xx[3] , yy[3])) + np.random.normal(0. , .478/(4.*20.) , (size , size))
c1 , c2 , c3, c4 = [],[],[],[]
print xx[0] , yy [0]
c1.append(fitting.fitting_centroid(data1 , .478/(2.*10.), 2. , 2.5))
c1.append(psfpoly.find_centroid(data1 , 2. , .478/(2.*10.)))
c1.append(spolynom.find_centroid(data1 , 2.8, .478/(2.*10.)))
c1.append(moment.find_cen(data1))
print c1
c2.append(fitting.fitting_centroid(data2 ,  .478/(4.*10.), 4. , 2.5))
c2.append(psfpoly.find_centroid(data2 , 4. , .478/(4.*10.)))
c2.append(spolynom.find_centroid(data2 , 2.8, .478/(4.*10.)))
c2.append(moment.find_cen(data2))

c3.append(fitting.fitting_centroid(data3 , .478/(2.*20.), 2. , 2.5))
c3.append(psfpoly.find_centroid(data3 , 2. , .478/(2.*20.)))
c3.append(spolynom.find_centroid(data3 , 2.8, .478/(2.*20.)))
c3.append(moment.find_cen(data3))

c4.append(fitting.fitting_centroid(data4 ,  .478/(4.*20.), 4. , 2.5))
c4.append(psfpoly.find_centroid(data4 , 4. , .478/(4.*20.)))
c4.append(spolynom.find_centroid(data4 , 2.8, .478/(4.*20.)))
c4.append(moment.find_cen(data4))


import matplotlib.pyplot as plt
plt.rcParams['text.latex.preamble'] = [r"\usepackage{lmodern}"]
params = {'text.usetex' : True, 'font.size' : 17 , 'font.family' : 'lmodern' , 'text.latex.unicode' : True, }
plt.rcParams.update(params)
fig , axarr = plt.subplots(2 , 2 , sharex= True, sharey= True) 

image = np.zeros((size*2 , size*2))

image[:size , :size] = data1
image[size: , :size] = data2
image[:size , size:] = data3
image[size: , size:] = data4

x = np.arange(size)
y = size/2*np.ones_like(x)
vmi , vma = np.min(image) , np.max(image)

axarr[0,0].imshow(data3 , interpolation = "None" , origin = 'lower' , aspect='auto' , vmin=np.min(data3) , vmax=np.max(data3), cmap=plt.get_cmap("cool"))
axarr[0,0].plot(xx[2]-.5 , yy[2]-.5, 'k*')
axarr[0,0].plot(c3[0][0]-.5 , c3[0][1]-.5, 'k.')
axarr[0,0].plot(c3[1][1]-.5 , c3[1][0]-.5, 'k+')
axarr[0,0].plot(c3[2][1]-.5 , c3[2][0]-.5, 'kx')
axarr[0,0].plot(c3[3][1]-.5 , c3[3][0]-.5, 'k^')

axarr[0,0].set_xticks(())
axarr[0,0].set_yticks(())
axarr[0,0].set_ylabel("SNR = 15")

axarr[0,1].imshow(data4 , interpolation = "None" , origin = 'lower' , aspect='auto' , vmin=np.min(data4) , vmax=np.max(data4), cmap=plt.get_cmap("cool"))
axarr[0,1].plot(xx[3]-.5 , yy[3]-.5, 'k*')

axarr[0,1].plot(c4[0][0]-.5 , c4[0][1]-.5, 'k.')
axarr[0,1].plot(c4[1][1]-.5 , c4[1][0]-.5, 'k+')
axarr[0,1].plot(c4[2][1]-.5 , c4[2][0]-.5, 'kx')
axarr[0,1].plot(c4[3][1]-.5 , c4[3][0]-.5, 'k^')
axarr[0,1].set_xticks(())
axarr[0,1].set_yticks(())
#axarr[0,1].set_xlabel(SNR = 15)

axarr[1,0].imshow(data1 , interpolation = "None" , origin = 'lower' , aspect='auto' , vmin=np.min(data1) , vmax=np.max(data1) , cmap=plt.get_cmap("cool"))
axarr[1,0].plot(xx[0]-.5 , yy[0]-.5, 'k*')
axarr[1,0].plot(c1[0][0]-.5 , c1[0][1]-.5, 'k.')
axarr[1,0].plot(c1[1][1]-.5 , c1[1][0]-.5, 'k+')
axarr[1,0].plot(c1[2][1]-.5 , c1[2][0]-.5, 'kx')
axarr[1,0].plot(c1[3][1]-.5 , c1[3][0]-.5, 'k^')

axarr[1,0].set_xlim([5.5,10.5])
axarr[1,0].set_ylim([5.5,10.5])
axarr[1,0].set_xticks(())
axarr[1,0].set_yticks(())
axarr[1,0].set_xlabel("PSF FWHM = 2 pixels")
axarr[1,0].set_ylabel("SNR = 7.5")

axarr[1,1].imshow(data2 , interpolation = "None" , origin = 'lower' , aspect='auto' , vmin=np.min(data2) , vmax=np.max(data2), cmap=plt.get_cmap("cool"))
axarr[1,1].plot(xx[1]-.5 , yy[1]-.5, 'k*')
axarr[1,1].plot(c2[0][0]-.5 , c2[0][1]-.5, 'k.')
axarr[1,1].plot(c2[1][1]-.5 , c2[1][0]-.5, 'k+')
axarr[1,1].plot(c2[2][1]-.5 , c2[2][0]-.5, 'kx')
axarr[1,1].plot(c2[3][1]-.5 , c2[3][0]-.5, 'k^')
axarr[1,1].set_xticks(())
axarr[1,1].set_yticks(())
axarr[1,1].set_xlabel("PSF FWHM = 4 pixels")

plt.setp([a.get_xticklabels() for a in axarr[0, :]], visible=False)
plt.setp([a.get_yticklabels() for a in axarr[0, :]], visible=False)
plt.setp([a.get_xticklabels() for a in axarr[1, :]], visible=False)
plt.setp([a.get_yticklabels() for a in axarr[1, :]], visible=False)
plt.tight_layout()
fig.set_size_inches(7,7)
plt.savefig("q.png")
