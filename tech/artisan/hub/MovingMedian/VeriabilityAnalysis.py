import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import style

index = []
col3 = []
col4 = []
col5 = []
col6 = []
col7 = []

f = open( 'D:/FYP-Developments/Dataset-Debs-2013/MovingAverageData/result.csv', 'rU' ) #open train data
for line in f:

    cells = line.split(",")
    index.append((cells[0]))
    col3.append((cells[3]))
    col4.append((cells[4]))
    col5.append((cells[5]))
    col6.append((cells[6]))
    col7.append((cells[7]))

f.close()

detailsX = {'col3': col3, 'TimeIndex': index}
detailsY = {'col4': col4, 'TimeIndex': index}
detailsZ = {'col5': col5, 'TimeIndex': index}
detailsV = {'col6': col6, 'TimeIndex': index}
detailsA = {'col7': col7, 'TimeIndex': index}

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


#rolling median calculation
avgX = pd.rolling_median(dfX['col3'], 10)
avgY = pd.rolling_median(dfY['col4'], 10)
avgZ = pd.rolling_median(dfZ['col5'], 10)
avgV = pd.rolling_median(dfV['col6'], 10)
avgA = pd.rolling_median(dfA['col7'], 10)

style.use('fivethirtyeight')

dfX.plot()
avgX.plot()

dfY.plot()
avgY.plot()

dfZ.plot()
avgZ.plot()

dfV.plot()
avgV.plot()

dfA.plot()
avgA.plot()

plt.show()


