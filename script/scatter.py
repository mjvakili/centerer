import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['text.latex.preamble'] = [r"\usepackage{lmodern}"]
params = {'text.usetex' : True, 'font.size' : 17 , 'font.family' : 'lmodern' , 'text.latex.unicode' : True, }
plt.rcParams.update(params)

################################################################# DATA #####################################

s1 = (np.loadtxt("noise5_20_0.txt")**-1.)*.478/2.
s2 = (np.loadtxt("noise5_28_0.txt")**-1.)*.478/2.8
s3 = (np.loadtxt("noise5_40_0.txt")**-1.)*.478/4.0
s4 = (np.loadtxt("noise5_56_0.txt")**-1.)*.478/5.6
a1 = np.loadtxt("erx5_20_0.txt")
a2 = np.loadtxt("erx5_28_0.txt")
a3 = np.loadtxt("erx5_40_0.txt")
a4 = np.loadtxt("erx5_56_0.txt")

################################################################# FLAGGED OBJECTS ##########################

crap1 = np.array([1])#np.loadtxt("flag2_20_0.txt").astype(int)
crap2 = np.array([1])#np.loadtxt("flag2_28_0.txt").astype(int)
crap3 = np.array([1])#np.loadtxt("flag2_40_0.txt").astype(int)
crap4 = np.array([1])#np.loadtxt("flag2_56_0.txt").astype(int)

fig , axarr = plt.subplots(2 , 2 , sharex= True, sharey= True) 

total_bins = 400
###################################################################### axarr[0,0] ################
a = s1
b = a1

a_clean = np.delete(s1, crap1,  axis=0)
a_flag = a[crap1]

b_clean = np.delete(a1, crap1,  axis=0)
b_flag = b[crap1]

bins = np.linspace(a.min()-1, a.max(), total_bins)
delta = bins[1]-bins[0]
idx  = np.digitize(a,bins)

axarr[0,0].loglog(np.sort(a) , (2.*.68466)/(np.sort(a)) , 'g-', lw = 1 , alpha = 1.)
axarr[0,0].scatter(a_clean , b_clean**.5 , s=1 , c = 'y' , marker='+' , label='FWHM = 2.8' , alpha = .2)
axarr[0,0].scatter(a_flag  , b_flag , s=1 , c = 'c' , marker='+' , label='FWHM = 2.8' , alpha = .2)
running_mean= [np.mean(b[idx==k]) for k in range(total_bins)]
running_median= [np.median(b[idx==k]) for k in range(total_bins)]
axarr[0,0].plot(bins-delta/2,np.array(running_mean)**.5,'b-',lw=1,alpha=1.)
axarr[0,0].plot(bins-delta/2,np.array(running_median)**.5,'r-',lw=1,alpha=1.)
#axarr[0,0].set_yticks([10**-3. , 10**-2. , 10**-1.])

axarr[0,0].set_ylabel(r"$\Delta x$ (pixel)")
axarr[1,1].set_ylim([10.**-6.,5.])
axarr[0,0].set_xlim([5.,150.])

################################################################### axarr[0,1] ###########################
aa = s2
bb = a2

aa_clean = np.delete(s2, crap2,  axis=0)
aa_flag = aa[crap2]

bb_clean = np.delete(a2, crap2,  axis=0)
bb_flag = bb[crap2]

bins = np.linspace(aa.min()-1,aa.max(), total_bins)
delta = bins[1]-bins[0]
idx  = np.digitize(aa,bins)

axarr[0,1].loglog(np.sort(aa) , (2.8*.68466)/(np.sort(aa)) , 'g-', lw = 1 , alpha = 1.)
axarr[0,1].scatter(aa_clean , bb_clean**.5 , s=1 , c = 'y' , marker='+' , label='FWHM = 2.8' , alpha = .2)
axarr[0,1].scatter(aa_flag  , bb_flag , s=1 , c = 'c' , marker='+' , label='FWHM = 2.8' , alpha = .2)
running_mean= [np.mean(bb[idx==k]) for k in range(total_bins)]
running_median= [np.median(bb[idx==k]) for k in range(total_bins)]
axarr[0,1].plot(bins-delta/2,np.array(running_mean)**.5,'b-',lw=1,alpha=1.)
axarr[0,1].plot(bins-delta/2,np.array(running_median)**.5,'r-',lw=1,alpha=1.)

#axarr[0,1].set_xticks(())
#axarr[0,1].set_yticks(())
axarr[1,1].set_ylim([10.**-6.,5.])
axarr[0,1].set_xlim([5.,150.])

############################################################### axarr[1,0] ###################################3
aaa = s3
bbb = a3

aaa_clean = np.delete(s3, crap3,  axis=0)
aaa_flag = aaa[crap3]

bbb_clean = np.delete(a3, crap3,  axis=0)
bbb_flag = bbb[crap3]


bins = np.linspace(aaa.min()-1,aaa.max(), total_bins)
delta = bins[1]-bins[0]
idx  = np.digitize(aaa,bins)
running_mean= [np.mean(bbb[idx==k]) for k in range(total_bins)]

axarr[1,0].loglog(np.sort(aaa) , (4.*.68466)/(np.sort(aaa)) , 'g-', lw = 1 , alpha = 1.)
axarr[1,0].scatter(aaa_clean , bbb_clean**.5 , s=1 , c = 'y' , marker='+' , label='FWHM = 2.8' , alpha = .2)
axarr[1,0].scatter(aaa_flag  , bbb_flag , s=1 , c = 'c' , marker='+' , label='FWHM = 2.8' , alpha = .2)
running_mean= [np.mean(bbb[idx==k]) for k in range(total_bins)]
running_median= [np.median(bbb[idx==k]) for k in range(total_bins)]
axarr[1,0].plot(bins-delta/2,np.array(running_mean)**.5,'b-',lw=1,alpha=1.)
axarr[1,0].plot(bins-delta/2,np.array(running_median)**.5,'r-',lw=1,alpha=1.)
#axarr[1,0].set_yticks([10**-3. , 10**-2. , 10**-1.])
axarr[1,0].set_xlabel("SNR")
axarr[1,0].set_ylabel(r"$\Delta x$ (pixel)")
axarr[1,1].set_ylim([10.**-6.,5.])
axarr[1,0].set_xlim([5.,150.])
#axarr[1,0].set_yticks([.001,.01,.1])

################################################################axarr[1,1] ##############################

aaaa = s4
bbbb = a4

aaaa_clean = np.delete(s4, crap4,  axis=0)
aaaa_flag = aaaa[crap3]

bbbb_clean = np.delete(a4, crap4,  axis=0)
bbbb_flag = bbbb[crap3]

bins = np.linspace(aaaa.min()-1,aaaa.max(), total_bins)
delta = bins[1]-bins[0]
idx  = np.digitize(aaaa,bins)



axarr[1,1].loglog(np.sort(aaaa) , (5.6*.68466)/(np.sort(aaaa)) , 'g-', lw = 1 , alpha = 1.)
axarr[1,1].scatter(aaaa_clean , bbbb_clean**.5 , s=1 , c = 'y' , marker='+' , label='FWHM = 2.8' , alpha = .2)
axarr[1,1].scatter(aaaa_flag  , bbbb_flag , s=1 , c = 'c' , marker='+' , label='FWHM = 2.8' , alpha = .2)
running_mean= [np.mean(bbbb[idx==k]) for k in range(total_bins)]
running_median= [np.median(bbbb[idx==k]) for k in range(total_bins)]
axarr[1,1].plot(bins-delta/2,np.array(running_mean)**.5,'b-',lw=1,alpha=1.)
axarr[1,1].plot(bins-delta/2,np.array(running_median)**.5,'r-',lw=1,alpha=1.)
#axarr[1,1].set_yticks(())

axarr[1,1].set_xlabel("SNR")
axarr[1,1].set_ylim([10.**-6.,5.])
axarr[1,1].set_xlim([5.,150.])

#fig.subplots_adjust(hspace=0.001 , wspace=0)
plt.setp([a.get_xticklabels() for a in axarr[0, :]], visible=False)
plt.setp([a.get_yticklabels() for a in axarr[:, 1]], visible=False)
plt.tight_layout()
fig.set_size_inches(7,7)

plt.savefig("snr_spoly_mean.png" , dpi=200)
