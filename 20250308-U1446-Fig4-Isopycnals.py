#%% Figure 4: Isopycnals %%#
# Plotting T-S isopycnals for EH, HS1, and LGM at Site U1446 and SO188KL342 in the Bay of Bengal
# 
#================================#
#
# ----
# Written by: Kaustubh Thirumalai, University of Arizona | [Github](https://github.com/planktic)
#
# Written on: August 10, 2023 | Updated: March 08, 2025
# ----
# %%

import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import matplotlib as mpl
import scipy.io as spio
import seaborn as sns
import pandas as pd
import xarray as xr
import numpy as np
import sys
import seawater
import gsw

gundu = pd.ExcelFile("/Users/kaustubh/Documents/Python/FullRepos/250308-paleoISMthirumalai2025/20250308-U1446-DataFile.xlsx")
krup = gundu.parse('TS')
chuc = krup.values
CT_T = chuc[:,0]
CT_TE = chuc[:,1]
CT_S = chuc[:,2]
CT_SE = chuc[:,3]
EH_T = chuc[:,4]
EH_TE = chuc[:,5]
EH_S = chuc[:,6]
EH_SE = chuc[:,7]
HS_T = chuc[:,8]
HS_TE = chuc[:,9]
HS_S = chuc[:,10]
HS_SE = chuc[:,11]
LGM_T = chuc[:,12]
LGM_TE = chuc[:,13]
LGM_S = chuc[:,14]
LGM_SE = chuc[:,15]
BA_T = chuc[:,16]
BA_TE = chuc[:,17]
BA_S = chuc[:,18]
BA_SE = chuc[:,19]

W_CT_T = chuc[:,20]
W_CT_TE = chuc[:,21]
W_CT_S = chuc[:,22]
W_CT_SE = chuc[:,23]
W_EH_T = chuc[:,24]
W_EH_TE = chuc[:,25]
W_EH_S = chuc[:,26]
W_EH_SE = chuc[:,27]
W_HS_T = chuc[:,28]
W_HS_TE = chuc[:,29]
W_HS_S = chuc[:,30]
W_HS_SE = chuc[:,31]
W_LGM_T = chuc[:,32]
W_LGM_TE = chuc[:,33]
W_LGM_S = chuc[:,34]
W_LGM_SE = chuc[:,35]
W_BA_T = chuc[:,36]
W_BA_TE = chuc[:,37]
W_BA_S = chuc[:,38]
W_BA_SE = chuc[:,39]

# %%

# TS Diagram with density contours
plt.figure(figsize=(8,6))

# Calculate the density lines
x = np.arange(30, 36, .1)
y = np.arange(23.5, 32.1, .5)
X, Y = np.meshgrid(x, y)
Z = seawater.eos80.dens0(X,Y) - 1000 # Substract 1000 to convert to sigma-t
K = gsw.spiciness1(X,Y)

# Plot the contour lines
sns.set(style='darkgrid',palette='muted',font='Menlo',font_scale=1.5)
[fig,ax] = plt.subplots(1,1,figsize=(8,4.5))

CS = plt.contour(X, Y, Z, colors='grey', linestyles='dashed', levels=np.arange(16.5,24.5,.5))
manual_locations = [(30, 31.5),(30.2, 30.5),(30.2, 28.7),(30.5, 27.5), (30.6, 26.5), (31, 25.8), (31.2, 25), (31.6, 25), (32.4, 25), (33.1, 25), (33.8, 25), (34.5, 25),(35.1, 25)]
plt.clabel(CS, inline=1, fontsize=10, fmt='%0.1f',manual=manual_locations)

# Plot the data
nprof = 25 #Selected profile
plt.errorbar(np.nanmean(CT_S),np.nanmean(CT_T),xerr=np.nanstd(CT_S),yerr=np.nanstd(CT_T),marker='o',markeredgecolor='xkcd:black',color='xkcd:black',linestyle='none',linewidth=10,elinewidth=1.5,markersize=12,markerfacecolor='xkcd:orange',zorder=6)
plt.errorbar(np.nanmean(HS_S),np.nanmean(HS_T),xerr=np.nanstd(HS_S),yerr=np.nanstd(HS_T),marker='o',markeredgecolor='xkcd:black',color='xkcd:black',linestyle='none',linewidth=10,elinewidth=1.5,markersize=12,markerfacecolor='xkcd:purple',zorder=5)
plt.errorbar(np.nanmean(EH_S),np.nanmean(EH_T),xerr=np.nanstd(EH_S),yerr=np.nanstd(EH_T),marker='o',markeredgecolor='xkcd:black',color='xkcd:black',linestyle='none',linewidth=10,elinewidth=1.5,markersize=12,markerfacecolor='xkcd:teal',zorder=5)
plt.errorbar(np.nanmean(LGM_S),np.nanmean(LGM_T),xerr=np.nanstd(LGM_S),yerr=np.nanstd(LGM_T),marker='o',markeredgecolor='xkcd:black',color='xkcd:black',linestyle='none',linewidth=10,elinewidth=1.5,markersize=12,markerfacecolor='xkcd:navy blue',zorder=5)
plt.errorbar(np.nanmean(BA_S),np.nanmean(BA_T),xerr=np.nanstd(BA_S),yerr=np.nanstd(BA_T),marker='o',markeredgecolor='xkcd:black',color='xkcd:black',linestyle='none',linewidth=10,elinewidth=1.5,markersize=12,markerfacecolor='xkcd:sky blue',zorder=5)
plt.errorbar(np.nanmean(W_CT_S),np.nanmean(W_CT_T),xerr=np.nanstd(W_CT_S),yerr=np.nanstd(W_CT_T),marker='d',markeredgecolor='xkcd:black',color='xkcd:black',linestyle='none',linewidth=10,elinewidth=1.5,markersize=12,markerfacecolor='xkcd:orange',zorder=6)
plt.errorbar(np.nanmean(W_HS_S),np.nanmean(W_HS_T),xerr=np.nanstd(W_HS_S),yerr=np.nanstd(W_HS_T),marker='d',markeredgecolor='xkcd:black',color='xkcd:black',linestyle='none',linewidth=10,elinewidth=1.5,markersize=12,markerfacecolor='xkcd:purple',zorder=5)
plt.errorbar(np.nanmean(W_EH_S),np.nanmean(W_EH_T),xerr=np.nanstd(W_EH_S),yerr=np.nanstd(W_EH_T),marker='d',markeredgecolor='xkcd:black',color='xkcd:black',linestyle='none',linewidth=10,elinewidth=1.5,markersize=12,markerfacecolor='xkcd:teal',zorder=5)
plt.errorbar(np.nanmean(W_LGM_S),np.nanmean(W_LGM_T),xerr=np.nanstd(W_LGM_S),yerr=np.nanstd(W_LGM_T),marker='d',markeredgecolor='xkcd:black',color='xkcd:black',linestyle='none',linewidth=10,elinewidth=1.5,markersize=12,markerfacecolor='xkcd:navy blue',zorder=5)
plt.errorbar(np.nanmean(W_BA_S),np.nanmean(W_BA_T),xerr=np.nanstd(W_BA_S),yerr=np.nanstd(W_BA_T),marker='d',markeredgecolor='xkcd:black',color='xkcd:black',linestyle='none',linewidth=10,elinewidth=1.5,markersize=12,markerfacecolor='xkcd:sky blue',zorder=5)

plt.errorbar(CT_S,CT_T,xerr=CT_SE,yerr=CT_TE,color='xkcd:orange',alpha=0.45,linestyle='none',marker='.',lw=0.75,ms=8)
plt.errorbar(HS_S,HS_T,xerr=HS_SE,yerr=HS_TE,color='xkcd:purple',alpha=0.45,linestyle='none',marker='.',lw=0.75,ms=8)
plt.errorbar(EH_S,EH_T,xerr=EH_SE,yerr=EH_TE,color='xkcd:teal',alpha=0.45,linestyle='none',marker='.',lw=0.75,ms=8)
plt.errorbar(LGM_S,LGM_T,xerr=LGM_SE,yerr=LGM_TE,color='xkcd:navy blue',alpha=0.45,linestyle='none',marker='.',lw=0.75,ms=8)
plt.errorbar(BA_S,BA_T,xerr=BA_SE,yerr=BA_TE,color='xkcd:sky blue',alpha=0.45,linestyle='none',marker='.',lw=0.75,ms=8)

plt.errorbar(W_CT_S,W_CT_T,xerr=W_CT_SE,yerr=W_CT_TE,color='xkcd:orange',alpha=0.45,linestyle='none',marker='.',lw=0.75,ms=8)
plt.errorbar(W_HS_S,W_HS_T,xerr=W_HS_SE,yerr=W_HS_TE,color='xkcd:purple',alpha=0.45,linestyle='none',marker='.',lw=0.75,ms=8)
plt.errorbar(W_EH_S,W_EH_T,xerr=W_EH_SE,yerr=W_EH_TE,color='xkcd:teal',alpha=0.45,linestyle='none',marker='.',lw=0.75,ms=8)
plt.errorbar(W_LGM_S,W_LGM_T,xerr=W_LGM_SE,yerr=W_LGM_TE,color='xkcd:navy blue',alpha=0.45,linestyle='none',marker='.',lw=0.75,ms=8)
plt.errorbar(W_BA_S,W_BA_T,xerr=W_BA_SE,yerr=W_BA_TE,color='xkcd:sky blue',alpha=0.45,linestyle='none',marker='.',lw=0.75,ms=8)

#====Plotting Data from Models====#
plt.errorbar(32.54512973,27.64664791,xerr=1.677404535/2,yerr=0.638520726/2,marker='s',markeredgecolor='xkcd:black',color='xkcd:red',linestyle='none',linewidth=10,elinewidth=1.5,markersize=12,markerfacecolor='xkcd:red',zorder=5)
plt.errorbar(32.3571783,29.3921067,xerr=1.501079417/2,yerr=0.976126377/2,marker='s',markeredgecolor='xkcd:black',color='xkcd:orange red',linestyle='none',linewidth=10,elinewidth=1.5,markersize=12,markerfacecolor='xkcd:orange red',zorder=5)
plt.errorbar(32.28818961,30.89921993,xerr=1.553979395/2,yerr=0.899318267/2,marker='s',markeredgecolor='xkcd:black',color='xkcd:dark brown',linestyle='none',linewidth=10,elinewidth=1.5,markersize=12,markerfacecolor='xkcd:dark red',zorder=5)
plt.plot()

ax.set_yticks(np.arange(24,31.1,1))
ax.set_xlim(30,35.5)
ax.set_ylim(24.5,31.5)
ax.grid(which='both',linestyle='--')
plt.xlabel('Salinity (‰)');
plt.ylabel('Temperature (°C)')
plt.show()

#---- Save figure ----#
mpl.rcParams['pdf.fonttype'] = 42
fig.savefig('250308-Fig4-TS.pdf')