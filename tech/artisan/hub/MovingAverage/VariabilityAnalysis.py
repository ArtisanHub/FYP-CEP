import matplotlib.pyplot as plt
import pandas as pd
import statistics as stat
from matplotlib import style
import numpy as np

index = []
col3 = []
col4 = []
col5 = []
col6 = []
col7 = []

temp = 0

f = open( 'D:/FYP-Developments/Dataset-Debs-2013/MovingAverageData/result.csv', 'rU' ) #open train data
for line in f:

    cells = line.split(",")
    index.append((cells[0]))
    col3.append((float)(cells[3]))
    col4.append((float)(cells[4]))
    col5.append((float)(cells[5]))
    col6.append((float)(cells[6]))
    col7.append((float)(cells[7]))

f.close()

mean7 = stat.mean(col7)
print(mean7)

detailsX = {'col3': col3, 'TimeIndex': index}
detailsY = {'col4': col4, 'TimeIndex': index}
detailsZ = {'col5': col5, 'TimeIndex': index}
detailsV = {'col6': col6, 'TimeIndex': index}
detailsA = {'col7': col7, 'TimeIndex': index}

meanA = {'meanX': mean7, 'TimeIndex': index}


dfX = pd.DataFrame(detailsX)
dfX = dfX.astype(float)
dfX.set_index('TimeIndex', inplace=True)

dfY = pd.DataFrame(detailsY)
dfY = dfY.astype(float)
dfY.set_index('TimeIndex', inplace=True)

dfZ = pd.DataFrame(detailsZ)
dfZ = dfZ.astype(float)
dfZ.set_index('TimeIndex', inplace=True)

dfV = pd.DataFrame(detailsV)
dfV = dfV.astype(float)
dfV.set_index('TimeIndex', inplace=True)


dfA = pd.DataFrame(detailsA)
dfA = dfA.astype(float)
dfA.set_index('TimeIndex', inplace=True)

mnX = pd.DataFrame(meanA)
mnX = mnX.astype(float)
mnX.set_index('TimeIndex', inplace=True)


#rolling mean calculation
avgX = dfX.rolling(center=False,window=10).mean()
avgY = dfY.rolling(center=False,window=10).mean()
avgZ = dfZ.rolling(center=False,window=10).mean()
avgV = dfV.rolling(center=False,window=10).mean()
avgA = dfA.rolling(center=False,window=10).mean()


style.use('fivethirtyeight')

plt.figure("column 3")
plt.plot(dfX)
plt.plot(avgX)

plt.figure("column 4")
plt.plot(dfY)
plt.plot(avgY)

plt.figure("column 5")
plt.plot(dfZ)
plt.plot(avgZ)

plt.figure("column 6")
plt.plot(dfV)
plt.plot(avgV)

plt.figure("column 7")
line2d = plt.plot(dfA)
line2dRMean = plt.plot(avgA)


xvalues = line2d[0].get_xdata()
for itm in xvalues:
    print(itm)
yvalues = line2d[0].get_ydata()
print(yvalues)

print("####################")

xMvalues = line2dRMean[0].get_xdata()
for itm in xMvalues:
    print(itm)
yMvalues = line2dRMean[0].get_ydata()
print(yMvalues)

print("!!!!!!!!!!!!!!!!!!!")

out = open( 'D:/FYP-Developments/Dataset-Debs-2013/MovingAverageData/insights.csv', 'w' ) #open train data
for itm in yMvalues:
    temp = np.where(yMvalues == itm)
    if yMvalues[temp] >= 2*yvalues[temp]:
        out.write(str(yMvalues.item(temp)))
        out.write("\n")
    elif yvalues[temp] >= 2*yMvalues[temp]:
        out.write(str(yvalues.item(temp)))
        out.write("\n")
    else:
        continue

out.close()
plt.show()



