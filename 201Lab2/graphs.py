#!/usr/bin/python3
import matplotlib.pyplot as plt
import matplotlib
import numpy as np

fig_width_pt = 469.75502  # Get this from LaTeX using \showthe\columnwidth
inches_per_pt = 1.0/72.27               # Convert pt to inch
golden_mean = (np.sqrt(5)-1.0)/2.0         # Aesthetic ratio
fig_width = fig_width_pt*inches_per_pt  # width in inches
fig_height = fig_width*golden_mean      # height in inches
fig_size =  [fig_width,fig_height]
params = {'backend': 'ps',
          'figure.figsize': fig_size}
matplotlib.rcParams.update(params)

plt.rc('text', usetex=True)
plt.rc('font', family='serif')
data1x=[1428.57142857143,1326.5306122449,1224.48979591837,1122.44897959184,1020.40816326531,918.367346938775,816.326530612245,798.367346938776,714.285714285714,612.244897959184,510.204081632653,408.163265306122,306.122448979592,204.081632653061,102.040816326531,70.204081632653,28.9795918367344,25.918367346939]
data1y=[1920,2260,2410,2530,2650,2810,2930,2940,2920,2950,2960,2950,2960,2950,2950,2950,5460,5820]
data2x=[0.00189, 0.001975, 0.002078, 0.002211, 0.002406, 0.002683, 0.003038]
data2y=[4.743, 7.515, 11.33, 16.4, 23.42, 31.31, 37.64]
data3x=[0.09653, 0.06149, 0.04048, 0.02714, 0.01776, 0.01182, 0.008415]
data3y=[4.743, 7.515, 11.33, 16.4, 23.42, 31.31, 37.64]


matplotlib.use('PS')
plt.plot(data1x, data1y, marker='+', color='r', ls='')
plt.axis([0,1500,1500,6000])
plt.xlabel('Molar Volume $cm^3/mol$')
plt.ylabel('Pressure $kpaa$')
plt.title('Isotherm of Freon at 4°C')
plt.savefig('fig1.eps')

# plt.plot(data2x, data2y,ls='-', marker='+', color='C1', label='Bubble Point Specific Volume')
# plt.plot(data3x, data3y,ls='-', marker='+', color='C2', label='Dew Point Specific Volume')
# plt.axis([0,0.12,0,40])
# plt.xlabel('Specific Volume $m^3/kg$')
# plt.ylabel('Pressure $Bar$')
# plt.title('')
# plt.savefig("fig2.eps")
#plt.show()
