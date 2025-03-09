#%% Figure 3: U1446 IFA Histograms %%#
# *Program to visualize IFA data at Site U1446: late Holocene, early Holocene, and Heinrich Stadial 1*
#================================#
#
# ----
# Written by: Kaustubh Thirumalai, University of Arizona | [Github](https://github.com/planktic)
#
# Written on: Wednesday, June 7, 2023 | Updated: March 08, 2025
# ----

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

#%% Data Import %%#
# Import data into Pandas
#================================#

xls = pd.ExcelFile('/Users/kaustubh/Documents/Python/FullRepos/250308-paleoISMthirumalai2025/20250308-U1446-DataFile.xlsx')
df = xls.parse('IFA')

#---- By Species ----#
gr = df[(df['Species'] == 'G. ruber')]
ts = df[(df['Species'] == 'T. sacculifer')]
nd = df[(df['Species'] == 'N. dutertrei')]

# Function to assign values based on conditions
def assign_value(row):
    if row['Species'] == 'N. dutertrei':
        return 'Subsurface'
    else:
        return 'Surface'
    
df['Depth'] = df.apply(assign_value, axis=1)    

#%% Surface vs Subsurface Full Plot %%#
# Plot grouping species by depth
#++================================++#

import matplotlib.gridspec as gridspec
gs = gridspec.GridSpec(2, 3)
fig1 = plt.figure(figsize=(6.9,4.4))
sns.set(style='darkgrid',palette='muted',font='Menlo')
ax1 = plt.subplot(gs[0, 0])
ax2 = plt.subplot(gs[0, 1])
ax3 = plt.subplot(gs[0, 2])
ax4 = plt.subplot(gs[1, 0])
ax5 = plt.subplot(gs[1, 1])
ax6 = plt.subplot(gs[1, 2])

#---- Parameters ----#
# pal = sns.color_palette([sns.color_palette("magma", 10)[7],sns.color_palette("magma", 10)[2]])
pal = sns.color_palette("ocean_r", 2)
xl = (0.5,-5)
yl = (0,40)
xt = np.arange(1,-5.5,-1)
a1 = 0.5

#---- SubPlot 1: Heinrich 1 δ¹⁸O ----#
sns.histplot(
   data=df,x=df[(df['Time Period'] == 'Heinrich 1')]['δ¹⁸O'], fill=True, palette=pal, hue="Depth",
   alpha=a1, linewidth=0,kde=True,ax=ax1,legend=False)
# ax1.set_xlim((-2,0.5))
# ax1.set_xticklabels(np.arange(-2.5,0.8,1))
ax1.set_xlim(xl)
ax1.set_xticks(xt)
# ax1.invert_xaxis()
ax1.set_ylim(yl)
ax1.grid('major',axis='both',linestyle=':')
ax1.set_title("HEINRICH STADIAL 1")

#---- SubPlot 2: Early Holocene δ¹⁸O ----#
sns.histplot(
   data=df,x=df[(df['Time Period'] == 'Early Holocene')]['δ¹⁸O'], fill=True, palette=pal, hue="Depth",
   alpha=a1, linewidth=0,kde=True,ax=ax2,legend=False)
ax2.set_xlim(xl)
ax2.set_xticks(xt)
ax2.set_ylim(yl)
ax2.grid('major',axis='both',linestyle=':')
ax2.set_ylabel("")
ax2.set_yticklabels("")
ax2.tick_params(axis='y',left=False,right=False)
ax2.set_title("EARLY HOLOCENE")

#---- SubPlot 3: Late Holocene δ¹⁸O ----#
sns.histplot(
   data=df,x=df[(df['Time Period'] == 'Late Holocene')]['δ¹⁸O'], fill=True, palette=pal, hue="Depth",
   alpha=a1, linewidth=0,kde=True,ax=ax3,legend=False)
ax3.set_xlim(xl)
ax3.set_xticks(xt)
ax3.set_ylim(yl)
ax3.grid('major',axis='both',linestyle=':')
ax3.set_ylabel('')
ax3.tick_params(axis='y',labelright=True,right=False,labelleft=False,left=False)
ax3.set_title("LATE HOLOCENE")

#---- δ¹³C Parameters ----#
xl = (-1,3)
xt = np.arange(-1.,3.1,1)
a1 = 0.5

#---- SubPlot 4: Heinrich 1 δ¹³C ----#
sns.histplot(
   data=df,x=df[(df['Time Period'] == 'Heinrich 1')]['δ¹³C'], fill=True, palette=pal, hue="Depth",
   alpha=a1, linewidth=0,kde=True,ax=ax4,legend=False)
# ax4.set_xlim((-3,4))
# ax4.set_xticks(np.arange(-4,3.5,1))
ax4.set_xlim(xl)
ax4.set_xticks(xt)
ax4.set_ylim(yl)
ax4.grid('major',axis='both',linestyle=':')

#---- SubPlot 5: Early Holocene δ¹³C ----#
sns.histplot(
   data=df,x=df[(df['Time Period'] == 'Early Holocene')]['δ¹³C'], fill=True, palette=pal, hue="Depth",
   alpha=a1, linewidth=0,kde=True,ax=ax5,legend=False)
ax5.set_xlim(xl)
ax5.set_xticks(xt)
ax5.set_ylim(yl)
ax5.grid('major',axis='both',linestyle=':')
ax5.set_ylabel("")
ax5.set_yticklabels("")
ax5.tick_params(axis='y',left=False,right=False)

#---- SubPlot 6: Late Holocene δ¹³C ----#
sns.histplot(
   data=df,x=df[(df['Time Period'] == 'Late Holocene')]['δ¹³C'], fill=True, palette=pal, hue="Depth",
   alpha=a1, linewidth=0,kde=True,ax=ax6,legend=False)
ax6.set_xlim(xl)
ax6.set_xticks(xt)
ax6.set_ylim(yl)
ax6.grid('major',axis='both',linestyle=':')
ax6.set_ylabel('')
ax6.tick_params(axis='y',labelright=True,right=False,labelleft=False,left=False)
# plt.tight_layout()
plt.show()

#---- Save figure ----#
mpl.rcParams['pdf.fonttype'] = 42
fig1.savefig('250308-Fig3-IFA-extra.pdf')

#%% By Species Full Plot %%#
# Plot grouping species by time period
#++================================++#

gs = gridspec.GridSpec(2, 3)
fig = plt.figure(figsize=(11,5))
ax1 = plt.subplot(gs[0, 0])
ax2 = plt.subplot(gs[0, 1])
ax3 = plt.subplot(gs[0, 2])
ax4 = plt.subplot(gs[1, 0])
ax5 = plt.subplot(gs[1, 1])
ax6 = plt.subplot(gs[1, 2])

#---- Parameters ----#

pal = sns.color_palette([sns.color_palette("mako", 10)[7],sns.color_palette("plasma", 10)[4],sns.color_palette("plasma", 10)[8]])
xl = (0.5,-5)
yl = (0,35)
xt = np.arange(0.5,-5.5,-1)
a1 = 0.5

#---- SubPlot 1: Heinrich 1 δ¹⁸O ----#
sns.histplot(
   data=df,x=df[(df['Time Period'] == 'Heinrich 1')]['δ¹⁸O'], fill=True, palette=pal, hue="Species",
   alpha=a1, linewidth=0,kde=True,ax=ax1,legend=False)
# ax1.set_xlim((-2.5,0.5))
# ax1.set_xticks(np.arange(-2,0.8,1))
ax1.set_xlim(xl)
ax1.set_xticks(xt)
# ax1.invert_xaxis()
ax1.set_ylim(yl)
ax1.grid('major',axis='both',linestyle=':')
ax1.set_ylabel("Frequency")
ax1.set_title("HEINRICH STADIAL 1")

#---- SubPlot 2: Early Holocene δ¹⁸O ----#
sns.histplot(
   data=df,x=df[(df['Time Period'] == 'Early Holocene')]['δ¹⁸O'], fill=True, palette=pal, hue="Species",
   alpha=a1, linewidth=0,kde=True,ax=ax2,legend=False)
ax2.set_xlim(xl)
ax2.set_xticks(xt)
ax2.set_ylim(yl)
ax2.grid('major',axis='both',linestyle=':')
ax2.set_ylabel("")
ax2.set_yticklabels("")
ax2.tick_params(axis='y',left=False,right=False)
ax2.set_title("EARLY HOLOCENE")

#---- SubPlot 3: Late Holocene δ¹⁸O ----#
sns.histplot(
   data=df,x=df[(df['Time Period'] == 'Late Holocene')]['δ¹⁸O'], fill=True, palette=pal, hue="Species",
   alpha=a1, linewidth=0,kde=True,ax=ax3,legend=False)
ax3.set_xlim(xl)
ax3.set_xticks(xt)
ax3.set_ylim(yl)
ax3.grid('major',axis='both',linestyle=':')
ax3.set_ylabel('')
ax3.tick_params(axis='y',labelright=True,right=False,labelleft=False,left=False)
ax3.set_title("LATE HOLOCENE")

#---- δ¹³C Parameters ----#
xl = (-1,3)
xt = np.arange(-1.,3.1,1)
a1 = 0.5

#---- SubPlot 4: Heinrich 1 δ¹³C ----#
sns.histplot(
   data=df,x=df[(df['Time Period'] == 'Heinrich 1')]['δ¹³C'], fill=True, palette=pal, hue="Species",
   alpha=a1, linewidth=0,kde=True,ax=ax4,legend=False)
# ax4.set_xlim((-3,4))
# ax4.set_xticks(np.arange(-4,3.5,1))
ax4.set_xlim(xl)
ax4.set_xticks(xt)
ax4.set_ylim(yl)
ax4.grid('major',axis='both',linestyle=':')
ax4.set_ylabel("Frequency")

#---- SubPlot 5: Early Holocene δ¹³C ----#
sns.histplot(
   data=df,x=df[(df['Time Period'] == 'Early Holocene')]['δ¹³C'], fill=True, palette=pal, hue="Species",
   alpha=a1, linewidth=0,kde=True,ax=ax5,legend=False)
ax5.set_xlim(xl)
ax5.set_xticks(xt)
ax5.set_ylim(yl)
ax5.grid('major',axis='both',linestyle=':')
ax5.set_ylabel("")
ax5.set_yticklabels("")
ax5.tick_params(axis='y',left=False,right=False)

#---- SubPlot 6: Late Holocene δ¹³C ----#
sns.histplot(
   data=df,x=df[(df['Time Period'] == 'Late Holocene')]['δ¹³C'], fill=True, palette=pal, hue="Species",
   alpha=a1, linewidth=0,kde=True,ax=ax6,legend=False)
ax6.set_xlim(xl)
ax6.set_xticks(xt)
ax6.set_ylim(yl)
ax6.grid('major',axis='both',linestyle=':')
ax6.set_ylabel('')
ax6.tick_params(axis='y',labelright=True,right=False,labelleft=False,left=False)
sns.set(style='darkgrid',palette='muted',font='Menlo')
plt.tight_layout()
plt.show()

#---- Save figure ----#
mpl.rcParams['pdf.fonttype'] = 42
fig.savefig('250308-Fig3-IFA.pdf')