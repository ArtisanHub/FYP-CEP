from sklearn import preprocessing
import pandas as pd
import numpy as np
from matplotlib import style
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

#col0 = []
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

salihPath = "/home/jawadhsr/Desktop/test.csv"
f = open( salihPath, 'rU' )

for line in f:

    cells = line.split(",")
    #col0.append((float)(cells[0]))
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

col3_scaled = preprocessing.scale(col3)
col4_scaled = preprocessing.scale(col4)
col5_scaled = preprocessing.scale(col5)


print("-------------------")
print(col3)
print("##")
print(col3_scaled)
print("###")
print(col3_scaled.mean(axis=0))
print("####")
print(col3_scaled.std(axis=0))
print("-------------------")

print("-------------------")
print(col4)
print("##")
print(col4_scaled)
print("###")
print(col4_scaled.mean(axis=0))
print("####")
print(col4_scaled.std(axis=0))
print("-------------------")

print("-------------------")
print(col5)
print("##")
print(col5_scaled)
print("###")
print(col5_scaled.mean(axis=0))
print("####")
print(col5_scaled.std(axis=0))
print("-------------------")

style.use('fivethirtyeight')

plt.figure("Column 3 - Scaled")
plt.plot(col3,mlab.normpdf(col3,np.mean(col3),np.std(col3)), label="Data")
plt.legend(loc='upper right')

plt.figure("Column 4 - Scaled")
plt.plot(col4_scaled, label="Data")
plt.legend(loc='upper right')

plt.figure("Column 5 - Scaled")
plt.plot(col5_scaled, label="Data")
plt.legend(loc='upper right')


plt.show()

