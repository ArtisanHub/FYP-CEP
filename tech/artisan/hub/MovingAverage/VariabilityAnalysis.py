import matplotlib.pyplot as plt
import pandas as pd
import statistics as stat
from matplotlib import style

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

out = open( 'D:/FYP-Developments/Dataset-Debs-2013/MovingAverageData/insights.csv', 'w' ) #open train data

for itm in col7:
    if itm > mean7:
        temp = col7.index(itm)
        out.write(str(index[temp]))
        out.write(str(","))

        out.write(str(col3[temp]))
        out.write(str(","))

        out.write(str(col4[temp]))
        out.write(str(","))

        out.write(str(col5[temp]))
        out.write(str(","))

        out.write(str(col6[temp]))
        out.write(str(","))

        out.write(str(col7[temp]))
        out.write(str(","))

        out.write(str("\n"))

    else:
        continue

out.close()

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


#rolling mean calculation
avgX = dfX.rolling(center=False,window=10).mean()
avgY = dfY.rolling(center=False,window=10).mean()
avgZ = dfZ.rolling(center=False,window=10).mean()
avgV = dfV.rolling(center=False,window=10).mean()
avgA = dfA.rolling(center=False,window=10).mean()


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



