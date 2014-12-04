import matplotlib.pyplot as plt
from matplotlib import rc
import csv, numpy

rc('text', usetex=True)
rc('font',**{'family':'serif','serif':['Computer Modern Roman']})

with open('spi-b0b1csnmosi.txt', newline='') as inputfile:
	results = list(csv.reader(inputfile))

plotme = numpy.zeros((5,len(results)-1))

i = 0
for x in results[1:len(results)]:
	plotme[0][i] = x[0].split("\t")[0]
	plotme[1][i] = x[0].split('\t')[1]
	plotme[2][i] = x[0].split('\t')[2]
	plotme[3][i] = x[0].split('\t')[3]
	plotme[4][i] = x[0].split('\t')[4]
	i += 1



plt.plot(plotme[0]*1e6,plotme[1],'r-', linewidth='2', label="B0")
plt.plot(plotme[0]*1e6,plotme[2]+6,'b-', linewidth='2', label="B1")
plt.plot(plotme[0]*1e6,plotme[3]+18,'g-', linewidth='2', label="CSn")
plt.plot(plotme[0]*1e6,plotme[4]+12,'m-', linewidth='2', label="MOSI")
plt.xlim((0,3000))

plt.legend()
plt.xlabel("Time ($\mu{}S$)")#μS)")

plt.show()