import statistics as stat

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

multiplication_constant = 4

count = 0
f = open('D:/FYP-Developments/Dataset-Debs-2013/MovingAverageData/resultDTW1.csv', 'rU') #open train data
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

std7 = multiplication_constant*(stat.stdev(col7))


output = open('D:/FYP-Developments/Dataset-Debs-2013/MovingAverageData/resultDTW1.csv', 'w')

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

        output.write(str("\n"))

    count = count + 1

output.close()
print("Data Extracting Done for file 1")
print("-------------------------------")

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

std7 = multiplication_constant*(stat.stdev(col7))


output = open('D:/FYP-Developments/Dataset-Debs-2013/MovingAverageData/resultDTW2.csv', 'w')

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

        output.write(str("\n"))

    count = count + 1

output.close()
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

std7 = multiplication_constant*(stat.stdev(col7))


output = open('D:/FYP-Developments/Dataset-Debs-2013/MovingAverageData/resultDTW3.csv', 'w')

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

        output.write(str("\n"))

    count = count + 1

output.close()
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

std7 = multiplication_constant*(stat.stdev(col7))


output = open('D:/FYP-Developments/Dataset-Debs-2013/MovingAverageData/resultDTW4.csv', 'w')

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

        output.write(str("\n"))

    count = count + 1

output.close()
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

std7 = multiplication_constant*(stat.stdev(col7))


output = open('D:/FYP-Developments/Dataset-Debs-2013/MovingAverageData/resultDTW5.csv', 'w')

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

        output.write(str("\n"))

    count = count + 1

output.close()
print("Data Extracting Done for file 5")
print("-------------------------------")






