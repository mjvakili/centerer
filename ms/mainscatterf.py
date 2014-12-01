import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['text.latex.preamble'] = [r"\usepackage{lmodern}"]
params = {'text.usetex' : True, 'font.size' : 17 , 'font.family' : 'lmodern' , 'text.latex.unicode' : True, }
plt.rcParams.update(params)



s1 = np.loadtxt("fwhm5_s5_00tb.txt")
s2 = np.loadtxt("fwhm5_s10_00.txt")
s3 = np.loadtxt("fwhm5_s20_00.txt")
s4 = np.loadtxt("fwhm5_s40_00.txt")
a1 = np.loadtxt("erx5_s5_00tb.txt")
a2 = np.loadtxt("erx5_s10_00.txt")
a3 = np.loadtxt("erx5_s20_00.txt")
a4 = np.loadtxt("erx5_s40_00.txt")


crap1 = np.array([1]) #np.loadtxt("flag5_s10_0.txt").astype(int)
crap2 = np.array([1]) #np.loadtxt("flag5_s50_0.txt").astype(int)
crap3 = np.array([1]) #np.loadtxt("flag5_s100_0.txt").astype(int)
crap4 = np.array([1]) #np.loadtxt("flag5_s150_0.txt").astype(int)



labels = [ 'S/N=5' ,  'S/N=10' ,  'S/N=20' ,  'S/N=40']

fig , axarr = plt.subplots(2,2 , sharex = True , sharey = True) 

total_bins = 40
###################################################################### axarr[0,0] ################

a = np.delete(s1, crap1,  axis=0)
b = np.delete(a1, crap1,  axis=0)
#a = a[b<10.]
#b = b[b<10.]

bins = np.linspace(a.min(), a.max(), total_bins)
delta = bins[1]-bins[0]
idx  = np.digitize(a,bins)

textstr = 'S/N=5'

axarr[0,0].text(0.6, 0.15, textstr, transform=axarr[0,0].transAxes, fontsize=18,
        verticalalignment='top')

axarr[0,0].semilogy(np.sort(a) , (np.sort(a)*.68466)/5. , 'g-', lw = 1 , alpha = 1. )
axarr[0,0].scatter(a , b**.5 , s=1 , c = 'y' , marker='+' , alpha = 1.)
running_mean   =   [np.mean(b[idx==k]) for k in range(total_bins)]
running_median =   [np.median(b[idx==k]) for k in range(total_bins)]
axarr[0,0].plot(bins-delta/2, np.array(running_mean)**.5   ,'b-', lw=1, alpha=1.)
axarr[0,0].plot(bins-delta/2, np.array(running_median)**.5 ,'r-', lw=1, alpha=1.)
#axarr[0,0].set_yticks(([.01 , .2]))
axarr[0,0].set_xticks(())
axarr[0,0].set_ylabel(r"$\sqrt{\Delta x^{2}}$ (pixel)")
axarr[1,1].set_ylim([10.**-3.,10.])
axarr[0,0].set_xlim([2.,10.])
axarr[0,0].legend(loc="lower right", bbox_to_anchor=[1, 0],
           ncol=1, shadow=False, fancybox=False)
################################################################### axarr[0,1] ###########################

aa = np.delete(s2, crap2,  axis=0)
bb = np.delete(a2, crap2,  axis=0)
#aa = aa[bb<10]
#bb = bb[bb<10]
bins = np.linspace(aa.min(), aa.max(), total_bins)
delta = bins[1]-bins[0]
idx  = np.digitize(aa,bins)
textstr = 'S/N=10'

axarr[0,1].text(0.6, 0.15, textstr, transform=axarr[0,1].transAxes, fontsize=18,
        verticalalignment='top')
axarr[0,1].semilogy(np.sort(aa) , (np.sort(aa)*.68466)/10 , 'g-', lw = 1 , alpha = 1.)
axarr[0,1].scatter(aa , bb**.5 , s=1 , c = 'y' , marker='+'  , alpha = 1.)
running_mean = [np.mean(bb[idx==k]) for k in range(total_bins)]
running_median = [np.median(bb[idx==k]) for k in range(total_bins)]
axarr[0,1].plot(bins-delta/2,np.array(running_mean)**.5,'b-',lw=1,alpha=1.)
axarr[0,1].plot(bins-delta/2,np.array(running_median)**.5,'r-',lw=1,alpha=1.)
#axarr[0,1].set_xticks(())
#axarr[0,1].set_yticks(())
axarr[1,1].set_ylim([10.**-3.,10.])
axarr[0,0].set_xlim([2.,10.])
axarr[0,1].legend(loc="lower right", bbox_to_anchor=[1, 0],
           ncol=1, shadow=False, fancybox=False)
############################################################### axarr[1,0] ###################################3

aaa = np.delete(s3, crap3,  axis=0)
bbb = np.delete(a3, crap3,  axis=0) 
#aaa = aaa[bbb<10.]
#bbb = bbb[bbb<10.]
bins = np.linspace(aaa.min(), aaa.max(), total_bins)
delta = bins[1]-bins[0]
idx  = np.digitize(aaa,bins)
running_mean = [np.mean(bbb[idx==k]) for k in range(total_bins)]

textstr = 'S/N=20'

axarr[1,0].text(0.6, 0.15, textstr, transform=axarr[1,0].transAxes, fontsize=18,
        verticalalignment='top')

axarr[1,0].semilogy(np.sort(aaa) , (np.sort(aaa)*.68466)/20 , 'g-', lw = 1 , alpha = 1.)
axarr[1,0].scatter(aaa , bbb**.5 , s=1 , c = 'y' , marker='+'  , alpha = 1.)
running_mean = [np.mean(bbb[idx==k]) for k in range(total_bins)]
axarr[1,0].plot(bins-delta/2,np.array(running_mean)**.5,'b-',lw=1,alpha=1.)
running_median = [np.median(bbb[idx==k]) for k in range(total_bins)]
axarr[1,0].plot(bins-delta/2,np.array(running_median)**.5,'r-',lw=1,alpha=1.)
#axarr[1,0].set_yticks([10**-3. , 10**-2. , 10**-1.])
axarr[1,0].set_xlabel("FWHM (pixel)")
axarr[1,0].set_ylabel(r"$\sqrt{\Delta x^{2}}$ (pixel)")
axarr[1,0].set_xticks(([2 , 4 , 6 , 8 , 10]))
axarr[1,0].legend(loc="lower right", bbox_to_anchor=[1, 0],
           ncol=1, shadow=False, fancybox=False)
axarr[1,1].set_ylim([10.**-3.,10.])
axarr[0,0].set_xlim([2.,10.])

################################################################axarr[1,1] ##############################

aaaa = np.delete(s4, crap4,  axis=0) 
bbbb = np.delete(a4, crap4,  axis=0) 
#aaaa = aaaa[bbbb<10.]
#bbbb = bbbb[bbbb<10.]

bins = np.linspace(aaaa.min(), aaaa.max(), total_bins)
delta = bins[1]-bins[0]
idx  = np.digitize(aaaa,bins)

textstr = 'S/N=40'

axarr[1,1].text(0.6, 0.15, textstr, transform=axarr[1,1].transAxes, fontsize=18,
        verticalalignment='top')
axarr[1,1].semilogy(np.sort(aaaa) , (np.sort(aaaa)*.68466)/40 , 'g-', lw = 1 , alpha = 1.)
axarr[1,1].scatter(aaaa , bbbb**.5 ,  s=1 , c = 'y' , marker='+'  , alpha = 1.)
running_mean = [np.mean(bbbb[idx==k]) for k in range(total_bins)]
axarr[1,1].plot(bins-delta/2,np.array(running_mean)**.5,'b-',lw=1,alpha=1.)
running_median = [np.median(bbbb[idx==k]) for k in range(total_bins)]
axarr[1,1].plot(bins-delta/2,np.array(running_median)**.5,'r-',lw=1,alpha=1.)

#axarr[1,1].set_yticks(())
axarr[1,1].set_xticks(([2 , 4 , 6 , 8 , 10]))
axarr[1,1].set_xlabel("FWHM (pixel)")
axarr[1,1].set_ylim([10.**-3.,10.])
axarr[0,0].set_xlim([2.,10.])

#fig.subplots_adjust(hspace=0.001 , wspace=0)
plt.setp([a.get_xticklabels() for a in axarr[0, :]], visible=False)
plt.setp([a.get_yticklabels() for a in axarr[:, 1]], visible=False)
plt.tight_layout()

axarr[1,1].legend(loc="lower right",
           ncol=1, shadow=False, fancybox=False)
#axarr.get_legend().get_title().set_color("red")

fig.set_size_inches(7,7)

plt.savefig("3by3sdss_no_regularizationz.png" , dpi=200)
