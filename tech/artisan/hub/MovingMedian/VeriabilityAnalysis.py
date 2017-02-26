import matplotlib.pyplot as plt
import pandas as pd
import statistics as stat
from matplotlib import style

col = []
timeInstance = []
multiplication_constant = 3 #Here the general norm is to consider the three times of standard deviation

count = 0
f = open( '', 'rU' ) #open train data
for line in f:

    cells = line.split(",")
    #Assign the time instance values to array TimeInstance
    #Assign dataset colum values to array col
    #Obtain each data columns to seperate arrays in order to conduct the analysis

f.close()

mean = stat.mean(col)

detailsX = {'col': col, 'TimeIndex': timeInstance}

meanA = {'meanX': mean, 'TimeIndex': timeInstance}


dfX = pd.DataFrame(detailsX)
dfX = dfX.astype(float)
dfX.set_index('TimeIndex', inplace=True)


mnX = pd.DataFrame(meanA)
mnX = mnX.astype(float)
mnX.set_index('TimeIndex', inplace=True)


#rolling median calculation
avgX = pd.rolling_median(dfX['col'], 10)


style.use('fivethirtyeight')

plt.plot(dfX)
plt.plot(avgX)


plt.show()



