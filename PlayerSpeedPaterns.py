import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import style

timeStamp = []
velocity = []

pathToBallSeperatedDataSet = 'D:/FYP/DEBS2013/PlayerStats/test.csv'
f = open(pathToBallSeperatedDataSet, 'rU') #open train data

for line in f:
    cells = line.split(",")
    timeStamp.append((cells[1]))
    velocity.append((cells[2]))
f.close()

detailsX = {'Player-Velocity': velocity, 'TimeStamp': timeStamp}


dfX = pd.DataFrame(detailsX)
dfX = dfX.astype(float)
dfX.set_index('TimeStamp', inplace=True)



avgX = pd.rolling_mean(dfX['Player-Velocity'], 10)


style.use('fivethirtyeight')

dfX.plot()
avgX.plot()


plt.show()


