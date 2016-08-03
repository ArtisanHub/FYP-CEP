from sklearn import preprocessing
import numpy as np
from matplotlib import style
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

col0 = []
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

temp = []

left_margin = -0.5
right_margin = 0.5

sep = ","

def extractData():

    count = 0
    for itm in col6:
        if itm < left_margin or itm > right_margin:
            e_data_row = str(col0[count]) + sep + str(col1[count]) + sep + str(col2[count]) + sep + str(
                col3[count]) + sep + str(
                col4[count]) + sep + str(col5[count]) + sep + str(col6[count]) \
                         + sep + str(col7[count]) + sep + str(col8[count]) + sep + str(col9[count]) + sep + str(
                col10[count]) + sep + str(col11[count]) + sep + str(col12[count]) \
                         + str("\n")

            output.write(e_data_row)
            temp.append(count)
        count = count + 1

    count = 0
    for itm in col5:
        if itm < left_margin or itm > right_margin:
            e_data_row = str(col0[count]) + sep + str(col1[count]) + sep + str(col2[count]) + sep + str(
                col3[count]) + sep + str(
                col4[count]) + sep + str(col5[count]) + sep + str(col6[count]) \
                         + sep + str(col7[count]) + sep + str(col8[count]) + sep + str(col9[count]) + sep + str(
                col10[count]) + sep + str(col11[count]) + sep + str(col12[count]) \
                         + str("\n")

            output.write(e_data_row)
            temp.append(count)
        count = count + 1

    count = 0
    for itm in col4:
        if itm < left_margin or itm > right_margin:
            e_data_row = str(col0[count]) + sep + str(col1[count]) + sep + str(col2[count]) + sep + str(
                col3[count]) + sep + str(
                col4[count]) + sep + str(col5[count]) + sep + str(col6[count]) \
                         + sep + str(col7[count]) + sep + str(col8[count]) + sep + str(col9[count]) + sep + str(
                col10[count]) + sep + str(col11[count]) + sep + str(col12[count]) \
                         + str("\n")

            output.write(e_data_row)
            temp.append(count)
        count = count + 1

    count = 0
    for itm in col3:
        if itm < left_margin or itm > right_margin:
            e_data_row = str(col0[count]) + sep + str(col1[count]) + sep + str(col2[count]) + sep + str(
                col3[count]) + sep + str(
                col4[count]) + sep + str(col5[count]) + sep + str(col6[count]) \
                         + sep + str(col7[count]) + sep + str(col8[count]) + sep + str(col9[count]) + sep + str(
                col10[count]) + sep + str(col11[count]) + sep + str(col12[count]) \
                         + str("\n")

            output.write(e_data_row)
            temp.append(count)
        count = count + 1

    count = 0
    for itm in col2:
        if itm < left_margin or itm > right_margin:
            e_data_row = str(col0[count]) + sep + str(col1[count]) + sep + str(col2[count]) + sep + str(
                col3[count]) + sep + str(
                col4[count]) + sep + str(col5[count]) + sep + str(col6[count]) \
                         + sep + str(col7[count]) + sep + str(col8[count]) + sep + str(col9[count]) + sep + str(
                col10[count]) + sep + str(col11[count]) + sep + str(col12[count]) \
                         + str("\n")

            output.write(e_data_row)
            temp.append(count)
        count = count + 1

    return


f = open( "D:/FYP-Developments/Dataset-Debs-2013/full-game/full-game.csv", 'rU' )

for line in f:

    cells = line.split(",")
    col0.append((float)(cells[0]))
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

f.close()

col2 = preprocessing.scale(col2)
col3 = preprocessing.scale(col3)
col4 = preprocessing.scale(col4)
col5 = preprocessing.scale(col5)
col6 = preprocessing.scale(col6)

output = open('D:/FYP-Developments/Dataset-Debs-2013/MovingAverageData/resultNormalised.csv', 'w')

extractData()

output.close()
temp.clear()

print("Data Extracting complete")
print("-------------------------------")


# style.use('fivethirtyeight')
#
# plt.figure("Column 3 - Scaled")
# plt.plot(col3,mlab.normpdf(col3,np.mean(col3),np.std(col3)))
#
# plt.figure("Column 4 - Scaled")
# plt.plot(col4,mlab.normpdf(col4,np.mean(col4),np.std(col4)))
#
# plt.figure("Column 5 - Scaled")
# plt.plot(col5,mlab.normpdf(col5,np.mean(col5),np.std(col5)))
#
#
# plt.show()

