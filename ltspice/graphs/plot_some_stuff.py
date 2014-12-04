import matplotlib.pyplot as plt
from matplotlib import rc
import csv, numpy

rc('text', usetex=True)
rc('font',**{'family':'serif','serif':['Computer Modern Roman']})

with open('gaindata.txt', newline='') as inputfile:
	results = list(csv.reader(inputfile))

plotme = numpy.zeros((3,len(results)-1))

i = 0
for x in results[1:len(results)]:
	plotme[0][i] = x[0].split("\t")[0]
	plotme[1][i] = x[0].split('\t')[1]
	plotme[2][i] = x[0].split('\t')[2]
	i += 1

#add divisions where the gain changes
plt.plot((-10,320), (3.5-.10, 3.5-.10),color=[.5,.5,.5])
plt.plot((-10,320), (3.5+.15, 3.5+.15),color=[.5,.5,.5])
plt.text(325,3.5,r'\textbf{Gain}',fontsize=12,verticalalignment='center')
for i in range(16):
	plt.plot((20*i, 20*i), (0, 5), '--', color=[.7,.7,.7])
	if i == 0:
		plt.text(20*i+10,3.5,"$\infty$",horizontalalignment='center')#,color='grey')#"∞")
	else:
		plt.text(20*i+10,3.5,str(round((16/i + 1),1)), fontsize=8,horizontalalignment='center')#,color='grey')

plt.plot(plotme[0]*1e6,plotme[1],'r-', linewidth='2', label="Input")
plt.plot(plotme[0]*1e6,plotme[2],'b-', linewidth='2', label="Output")
plt.xlim((0,3200))

plt.legend()
plt.xlabel("Time ($\mu{}S$)")#μS)")
plt.ylabel("Voltage")
plt.show()