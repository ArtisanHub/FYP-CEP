import matplotlib.pyplot as plt
import pandas as pd
import statistics as stat
from matplotlib import style
import numpy as np

index = []
col1 = []
col2 = []
col3 = []
col4 = []
col5 = []
col6 = []
col7 = []
col8 = []
col9 = []
col10 = []
col11 = []
col12 = []
col13 = []

count = 0


f = open( 'D:/FYP-Developments/Dataset-Debs-2013/MovingAverageData/result.csv', 'rU' ) #open train data
for line in f:

    cells = line.split(",")
    index.append((cells[2]))
    col1.append((float)(cells[1]))
    col2.append((float)(cells[2]))
    col3.append((float)(cells[3]))
    col4.append((float)(cells[4]))
    col5.append((float)(cells[5]))
    col6.append((float)(cells[6]))
    col7.append((float)(cells[7]))
    col8.append((float)(cells[8]))
    col9.append((float)(cells[9]))
    col10.append((float)(cells[10]))
    col11.append((float)(cells[11]))
    col12.append((float)(cells[12]))
    col13.append((float)(cells[13]))

f.close()

std3 = 3*(stat.stdev(col3))
std4 = 3*(stat.stdev(col4))
std5 = 3*(stat.stdev(col5))
std6 = 3*(stat.stdev(col6))
std7 = 3*(stat.stdev(col7))

print(std7)


detailsX = {'col3': col3, 'TimeIndex': index}
detailsY = {'col4': col4, 'TimeIndex': index}
detailsZ = {'col5': col5, 'TimeIndex': index}
detailsV = {'col6': col6, 'TimeIndex': index}
detailsA = {'col7': col7, 'TimeIndex': index}

stdX = {'stdX': std3, 'TimeIndex': index}
stdY = {'stdY': std4, 'TimeIndex': index}
stdZ = {'stdY': std5, 'TimeIndex': index}
stdV = {'stdY': std6, 'TimeIndex': index}
stdA = {'stdA': std7, 'TimeIndex': index}

#Extracting data
print("Data Extracting")

output = open('D:/FYP-Developments/Dataset-Debs-2013/MovingAverageData/insights.csv', 'w')  # open train data

for itm in col7:
    if itm > std7:
        output.write(str(col1[count]))
        output.write(str(","))

        output.write(str(col2[count]))
        output.write(str(","))

        output.write(str(col3[count]))
        output.write(str(","))

        output.write(str(col4[count]))
        output.write(str(","))

        output.write(str(col5[count]))
        output.write(str(","))

        output.write(str(col6[count]))
        output.write(str(","))

        output.write(str(col7[count]))
        output.write(str(","))

        output.write(str(col8[count]))
        output.write(str(","))

        output.write(str(col9[count]))
        output.write(str(","))

        output.write(str(col10[count]))
        output.write(str(","))

        output.write(str(col11[count]))
        output.write(str(","))

        output.write(str(col12[count]))
        output.write(str(","))

        output.write(str(col13[count]))
        output.write(str(","))

        output.write(str("\n"))

    count = count + 1

output.close()
print("Data Extracting Done")


#Ploting data
#Colum data
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

#Standrad Dev of Colum data
stdX = pd.DataFrame(stdX)
stdX = stdX.astype(float)
stdX.set_index('TimeIndex', inplace=True)

stdY = pd.DataFrame(stdY)
stdY = stdY.astype(float)
stdY.set_index('TimeIndex', inplace=True)

stdZ = pd.DataFrame(stdZ)
stdZ = stdZ.astype(float)
stdZ.set_index('TimeIndex', inplace=True)

stdV = pd.DataFrame(stdV)
stdV = stdV.astype(float)
stdV.set_index('TimeIndex', inplace=True)

stdA = pd.DataFrame(stdA)
stdA = stdA.astype(float)
stdA.set_index('TimeIndex', inplace=True)


#rolling mean calculation
avgX = dfX.rolling(center=False,window=10).mean()
avgY = dfY.rolling(center=False,window=10).mean()
avgZ = dfZ.rolling(center=False,window=10).mean()
avgV = dfV.rolling(center=False,window=10).mean()
avgA = dfA.rolling(center=False,window=10).mean()


style.use('fivethirtyeight')

plt.figure("column 3")
plt.plot(dfX, label="Data")
plt.plot(avgX, label="RM")
#plt.plot(stdX, label="SD")

plt.legend(loc='upper right')

plt.figure("column 4")
plt.plot(dfY, label="Data")
plt.plot(avgY, label="RM")
#plt.plot(stdY, label="SD")

plt.legend(loc='upper right')

plt.figure("column 5")
plt.plot(dfZ, label="Data")
plt.plot(avgZ, label="RM")
#plt.plot(stdZ, label="SD")

plt.legend(loc='upper right')

plt.figure("column 6")
plt.plot(dfV, label="Data")
plt.plot(avgV, label="RM")
plt.plot(stdV, label="SD")

plt.legend(loc='upper right')

plt.figure("column 7")
line2d = plt.plot(dfA, label="Data")
line2dRMean = plt.plot(avgA, label="RM")
plt.plot(stdA, label="SD")

plt.legend(loc='upper right')

plt.show()



