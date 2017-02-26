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

#Obtaining absolutet values of all the analytical data streams
col = [abs(x) for x in col]


#Calculating benchmark to obtain anomalies
std = multiplication_constant*(stat.stdev(col))


detailsX = {'col': col, 'TimeIndex': timeInstance}


stdX = {'stdX': std, 'TimeIndex': timeInstance}



#Ploting data
#Colum data
dfX = pd.DataFrame(detailsX)
dfX = dfX.astype(float)
dfX.set_index('TimeIndex', inplace=True)


#Standrad Dev of Colum data
stdX = pd.DataFrame(stdX)
stdX = stdX.astype(float)
stdX.set_index('TimeIndex', inplace=True)


#rolling mean calculation
avgX = dfX.rolling(center=False,window=10).mean()



style.use('fivethirtyeight')

plt.figure("Data Colum Analysis")
plt.plot(dfX, label="Data")
plt.plot(avgX, label="RM")
plt.plot(stdX, label="SD")

plt.legend(loc='upper right')


plt.show()



