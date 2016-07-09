import matplotlib.pyplot as plt
import pandas as pd
from matplotlib import style

timeStamp = []
lables = []
xCordinates = []
yCordinates = []
zCordinates = []

f = open( '/home/rnavagamuwa/Documents/CSE/FYP/Datasets/DEBS-2013-SoccerField/BallSeperated/ball-4.csv', 'rU' ) #open train data
for line in f:
    cells = line.split(",")
    timeStamp.append((cells[0]))
    xCordinates.append((cells[1]))
    yCordinates.append((cells[2]))
    zCordinates.append((cells[3]))
f.close()

detailsX = {'X_Coordinates': xCordinates, 'TimeStamp': timeStamp}
detailsY = {'Y_Coordinates': yCordinates, 'TimeStamp': timeStamp}
detailsZ = {'Z_Coordinates': zCordinates, 'TimeStamp': timeStamp}

dfX = pd.DataFrame(detailsX)
dfX = dfX.astype(float)
dfX.set_index('TimeStamp', inplace=True)

dfY = pd.DataFrame(detailsY)
dfY = dfY.astype(float)
dfY.set_index('TimeStamp', inplace=True)

dfZ = pd.DataFrame(detailsZ)
dfZ = dfZ.astype(float)
dfZ.set_index('TimeStamp', inplace=True)

avgX = pd.rolling_mean(dfX['X_Coordinates'], 10)
avgY = pd.rolling_mean(dfY['Y_Coordinates'], 10)
avgZ = pd.rolling_mean(dfZ['Z_Coordinates'], 10)

style.use('fivethirtyeight')

dfX.plot()
avgX.plot()

dfY.plot()
avgY.plot()

dfZ.plot()
avgZ.plot()

plt.show()


