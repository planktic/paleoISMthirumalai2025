#%% Figure 1: Map %%#
# Fig. 1: October Salinity and JJAS Rainfall
# This code needs the following datasets: ORA-S4 Salinity, GPCC Precipitation 
#================================#
#
# ----
# Written by: Kaustubh Thirumalai, University of Arizona | [Github](https://github.com/planktic)
#
# Written on: August 10, 2023 | Updated: March 08, 2025
# ----
 
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import matplotlib as mpl
import scipy.io as spio
import seaborn as sns
import pandas as pd
import xarray as xr
import numpy as np
import sys

#%% Import Datasets %%#
# Import salininty (ORA-S4), precipitation (GPCC)
#================================#

#---- ORA-S4 ----#
ora4 = xr.open_dataset('/Users/kaustubh/Documents/Python/Datasets/ORAS4_SSS.nc')
S_4 = np.squeeze(ora4.get('SO'))
S_4 = S_4.rename({'TIME': 'time'})
S_4 = S_4.rename({'LONN179_180': 'longitude'})
S_4 = S_4.rename({'LAT': 'latitude'})
S_4['month'] = S_4.time.dt.month
So = S_4

#---- GPCC ----#
gpcc = xr.open_dataset('/Users/kaustubh/Documents/Python/Datasets/GPCC_Rain.nc')
Pr = np.squeeze(gpcc.get('P'))
Pr = Pr.rename({'TIME': 'time'})
Pr = Pr.rename({'LON': 'longitude'})
Pr = Pr.rename({'LAT': 'latitude'})
Pr['month'] = Pr.time.dt.month

#---- Bay of Bengal ----#
X1 = 68.5
X2 = 99.5
Z1 = 5.5
Z2 = 30.5

#---- Mean Fields & Seasons ----#

Pr_JJAS = Pr.where((Pr.month >= 6) & (Pr.month <= 9), drop=True).sel(time=slice('1975-01-15', '2015-12-15'))

# Grouping by year but calculating sums in cm total and then converting to cm per year to cm/season
Pr_JJAS_field = Pr_JJAS.groupby('time.year').sum(dim='time').mean('year')
S_ON = So.where((So.month >= 10) & (So.month <= 11), drop=True).sel(time=slice('1975-01-15', '2015-12-15'))
S_ON_field = S_ON.mean('time')

#%% Full Plot %%#
#  Mean JJAS Pr & O Salinity
#================================#

import matplotlib.gridspec as gridspec

fig1 = plt.figure(figsize=(8, 5))
gs = fig1.add_gridspec(1, 1)
ax1 = fig1.add_subplot(gs[0, 0],projection=ccrs.PlateCarree())
# ax2 = fig1ab.add_subplot(gs[0, 1],projection=ccrs.PlateCarree())
sns.set(style='white',palette='muted',font='Menlo',font_scale=1)

#---- Projection ----#
ax1.set_extent([X1, X2, Z1, Z2])

#---- Colormap ----#
import matplotlib as mpl
cmap1 = mpl.colormaps['Greens']
cmap2 = mpl.colormaps['Blues']
cmap1 = mpl.colors.LinearSegmentedColormap.from_list("", ["xkcd:light beige","xkcd:washed out green","xkcd:apple green","xkcd:kelly green","xkcd:forest green"],N=128)
cmap2 = cmap2.reversed()

#---- Plot ----#
im_pr = ax1.contourf(Pr.longitude,Pr.latitude,Pr_JJAS_field/1000,np.arange(0,2.5,0.2),transform=ccrs.PlateCarree(),cmap=cmap1,extend='max') 
im_s = ax1.contourf(S_ON_field.longitude,S_ON_field.latitude,S_ON_field,np.arange(28,37.1,0.5),transform=ccrs.PlateCarree(),cmap=cmap2,extend='both')

#---- Colorbar ----#
cbar1 = plt.colorbar(im_pr,shrink=0.75,location='left')
cbar2 = plt.colorbar(im_s,shrink=0.75,location='left')
cbar1.set_label('Precipitation Totals (mm)')
cbar2.set_label('Surface Salinity (‰)')

# #---- Coastlines ----#
from cartopy.io.shapereader import Reader
from cartopy import feature as cfeature
ax1.coastlines(linewidth=1)

#---- Rivers ----#
from cartopy.io.shapereader import Reader
from cartopy import feature as cfeature
fname2 = '/Users/kaustubh/Documents/Python/Datasets/Maps/ne_10m_rivers_lake_centerlines/ne_10m_rivers_lake_centerlines.shp'
ax1.add_geometries(Reader(fname2).geometries(),
                  ccrs.PlateCarree(),linestyle='-',linewidth=1,facecolor='None',edgecolor='xkcd:blue',alpha=0.5,zorder=4)


#---- Gridlines ----#
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
gl2b = ax1.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,linewidth=2, color='xkcd:white', alpha=0.5, linestyle=':')
gl2b.top_labels = True
gl2b.bottom_labels = False
gl2b.right_labels = True
gl2b.left_labels = False
gl2b.xlocator = mpl.ticker.FixedLocator(np.arange(0,120,5))
gl2b.ylocator = mpl.ticker.FixedLocator(np.arange(-10,55,5))
gl2b.xformatter = LONGITUDE_FORMATTER    # Gives the degree sign
gl2b.yformatter = LATITUDE_FORMATTER

#---- Core Sites ----#

ax1.plot(86.5,19.5,'*',ms=26,mfc='xkcd:bright yellow',mec='xkcd:black',mew=2,alpha=1,transform=ccrs.PlateCarree())
ax1.plot(90,20,'o',ms=15,mfc='xkcd:earth',mec='xkcd:black',mew=2,alpha=1,transform=ccrs.PlateCarree())
ax1.plot(94,7.7,'o',ms=15,mfc='xkcd:kelly green',mec='xkcd:black',mew=2,alpha=1,transform=ccrs.PlateCarree())
ax1.plot(75,11,'o',ms=15,mfc='xkcd:blue purple',mec='xkcd:black',mew=2,alpha=1,transform=ccrs.PlateCarree())
ax1.plot(92,25,'^',ms=15,mfc='xkcd:bright red',mec='xkcd:black',mew=2,alpha=1,transform=ccrs.PlateCarree())
plt.tight_layout
plt.show()

#---- Save figure ----#
mpl.rcParams['pdf.fonttype'] = 42
fig1.savefig('250308-Fig1-Map.pdf')