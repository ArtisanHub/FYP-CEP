import statistics as stat

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
col13 = []

temp = []
sep = ","
e_data_row = ""

multiplication_constant = 4

def extractData():
    count = 0
    for itm in col7:
        if itm > std7:
            e_data_row = str(col1[count]) + sep + str(col2[count]) + sep + str(col3[count]) + sep + str(
                col4[count]) + sep + str(col5[count]) + sep + str(col6[count]) \
                         + sep + str(col7[count]) + sep + str(col8[count]) + sep + str(col9[count]) + sep + str(
                col10[count]) + sep + str(col11[count]) + sep + str(col12[count]) \
                         + sep + str(col13[count]) + str("\n")

            output.write(e_data_row)
            temp.append(count)
        count = count + 1

    count = 0
    for itm in col6:
        if itm > std6:
            if count not in temp:
                e_data_row = str(col1[count]) + sep + str(col2[count]) + sep + str(col3[count]) + sep + str(
                    col4[count]) + sep + str(col5[count]) + sep + str(col6[count]) \
                             + sep + str(col7[count]) + sep + str(col8[count]) + sep + str(col9[count]) + sep + str(
                    col10[count]) + sep + str(col11[count]) + sep + str(col12[count]) \
                             + sep + str(col13[count]) + str("\n")

                output.write(e_data_row)
                temp.append(count)
        count = count + 1

    count = 0
    for itm in col5:
        if itm > std5:
            if count not in temp:
                e_data_row = str(col1[count]) + sep + str(col2[count]) + sep + str(col3[count]) + sep + str(
                    col4[count]) + sep + str(col5[count]) + sep + str(col6[count]) \
                             + sep + str(col7[count]) + sep + str(col8[count]) + sep + str(col9[count]) + sep + str(
                    col10[count]) + sep + str(col11[count]) + sep + str(col12[count]) \
                             + sep + str(col13[count]) + str("\n")

                output.write(e_data_row)
                temp.append(count)
        count = count + 1

    count = 0
    for itm in col4:
        if itm > std4:
            if count not in temp:
                e_data_row = str(col1[count]) + sep + str(col2[count]) + sep + str(col3[count]) + sep + str(
                    col4[count]) + sep + str(col5[count]) + sep + str(col6[count]) \
                             + sep + str(col7[count]) + sep + str(col8[count]) + sep + str(col9[count]) + sep + str(
                    col10[count]) + sep + str(col11[count]) + sep + str(col12[count]) \
                             + sep + str(col13[count]) + str("\n")

                output.write(e_data_row)
                temp.append(count)
        count = count + 1

    count = 0
    for itm in col3:
        if itm > std3:
            if count not in temp:
                e_data_row = str(col1[count]) + sep + str(col2[count]) + sep + str(col3[count]) + sep + str(
                    col4[count]) + sep + str(col5[count]) + sep + str(col6[count]) \
                             + sep + str(col7[count]) + sep + str(col8[count]) + sep + str(col9[count]) + sep + str(
                    col10[count]) + sep + str(col11[count]) + sep + str(col12[count]) \
                             + sep + str(col13[count]) + str("\n")

                output.write(e_data_row)
                temp.append(count)
        count = count + 1

    return

#Use of file 1

f = open('D:/FYP-Developments/Dataset-Debs-2013/MovingAverageData/resultDTW1.csv', 'rU') #open train data
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
    col13.append((float)(cells[13]))

f.close()

#Obtaining absolute values of all the analytical data streams
col3 = [abs(x) for x in col3]
col4 = [abs(x) for x in col4]
col5 = [abs(x) for x in col5]

#Calculating benchmark to obtain anomalies
std3 = multiplication_constant*(stat.stdev(col3))
std4 = multiplication_constant*(stat.stdev(col4))
std5 = multiplication_constant*(stat.stdev(col5))
std6 = multiplication_constant*(stat.stdev(col6))
std7 = multiplication_constant*(stat.stdev(col7))

output = open('D:/FYP-Developments/Dataset-Debs-2013/MovingAverageData/resultDTW1.csv', 'w')

extractData()

output.close()
temp.clear()
print("Data Extracting Done for file 1")
print("-------------------------------")

#End of use of file 1

count = 0
f = open('D:/FYP-Developments/Dataset-Debs-2013/MovingAverageData/resultDTW2.csv', 'rU') #open train data
for line in f:

    cells = line.split(",")
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

#Obtaining absolute values of all the analytical data streams
col3 = [abs(x) for x in col3]
col4 = [abs(x) for x in col4]
col5 = [abs(x) for x in col5]

#Calculating benchmark to obtain anomalies
std3 = multiplication_constant*(stat.stdev(col3))
std4 = multiplication_constant*(stat.stdev(col4))
std5 = multiplication_constant*(stat.stdev(col5))
std6 = multiplication_constant*(stat.stdev(col6))
std7 = multiplication_constant*(stat.stdev(col7))


output = open('D:/FYP-Developments/Dataset-Debs-2013/MovingAverageData/resultDTW2.csv', 'w')

extractData()

output.close()
temp.clear()
print("Data Extracting Done for file 2")
print("-------------------------------")

count = 0
f = open('D:/FYP-Developments/Dataset-Debs-2013/MovingAverageData/resultDTW3.csv', 'rU') #open train data
for line in f:

    cells = line.split(",")
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

#Obtaining absolute values of all the analytical data streams
col3 = [abs(x) for x in col3]
col4 = [abs(x) for x in col4]
col5 = [abs(x) for x in col5]

#Calculating benchmark to obtain anomalies
std3 = multiplication_constant*(stat.stdev(col3))
std4 = multiplication_constant*(stat.stdev(col4))
std5 = multiplication_constant*(stat.stdev(col5))
std6 = multiplication_constant*(stat.stdev(col6))
std7 = multiplication_constant*(stat.stdev(col7))


output = open('D:/FYP-Developments/Dataset-Debs-2013/MovingAverageData/resultDTW3.csv', 'w')

extractData()

output.close()
temp.clear()
print("Data Extracting Done for file 3")
print("-------------------------------")

count = 0
f = open('D:/FYP-Developments/Dataset-Debs-2013/MovingAverageData/resultDTW4.csv', 'rU') #open train data
for line in f:

    cells = line.split(",")
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

#Obtaining absolute values of all the analytical data streams
col3 = [abs(x) for x in col3]
col4 = [abs(x) for x in col4]
col5 = [abs(x) for x in col5]

#Calculating benchmark to obtain anomalies
std3 = multiplication_constant*(stat.stdev(col3))
std4 = multiplication_constant*(stat.stdev(col4))
std5 = multiplication_constant*(stat.stdev(col5))
std6 = multiplication_constant*(stat.stdev(col6))
std7 = multiplication_constant*(stat.stdev(col7))


output = open('D:/FYP-Developments/Dataset-Debs-2013/MovingAverageData/resultDTW4.csv', 'w')

extractData()

output.close()
temp.clear()
print("Data Extracting Done for file 4")
print("-------------------------------")

count = 0
f = open('D:/FYP-Developments/Dataset-Debs-2013/MovingAverageData/resultDTW5.csv', 'rU') #open train data
for line in f:

    cells = line.split(",")
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

#Obtaining absolute values of all the analytical data streams
col3 = [abs(x) for x in col3]
col4 = [abs(x) for x in col4]
col5 = [abs(x) for x in col5]

#Calculating benchmark to obtain anomalies
std3 = multiplication_constant*(stat.stdev(col3))
std4 = multiplication_constant*(stat.stdev(col4))
std5 = multiplication_constant*(stat.stdev(col5))
std6 = multiplication_constant*(stat.stdev(col6))
std7 = multiplication_constant*(stat.stdev(col7))


output = open('D:/FYP-Developments/Dataset-Debs-2013/MovingAverageData/resultDTW5.csv', 'w')

extractData()

output.close()
temp.clear()
print("Data Extracting Done for file 5")
print("-------------------------------")






