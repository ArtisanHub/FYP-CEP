import mlpy
import matplotlib.pyplot as plt
import matplotlib.cm as cm
a = []
b = []
c = []
d = []
e = []

indx = 0
dtw_data_limit = 15000
f = open( 'D:/FYP-Developments/Dataset-Debs-2013/MovingAverageData/resultDTW1.csv', 'rU' ) #open train data
for line in f:

    cells = line.split(",")
    a.append((float)(cells[7]))
    indx = indx + 1

    if indx == dtw_data_limit:
        break

f.close()

indx = 0
f = open( 'D:/FYP-Developments/Dataset-Debs-2013/MovingAverageData/resultDTW2.csv', 'rU' ) #open train data
for line in f:

    cells = line.split(",")
    b.append((float)(cells[7]))
    indx = indx + 1

    if indx == dtw_data_limit:
        break

f.close()

indx = 0
f = open( 'D:/FYP-Developments/Dataset-Debs-2013/MovingAverageData/resultDTW3.csv', 'rU' ) #open train data
for line in f:

    cells = line.split(",")
    c.append((float)(cells[7]))
    indx = indx + 1

    if indx == dtw_data_limit:
        break

f.close()

indx = 0
f = open( 'D:/FYP-Developments/Dataset-Debs-2013/MovingAverageData/resultDTW4.csv', 'rU' ) #open train data
for line in f:

    cells = line.split(",")
    d.append((float)(cells[7]))
    indx = indx + 1

    if indx == dtw_data_limit:
        break

f.close()

indx = 0
f = open( 'D:/FYP-Developments/Dataset-Debs-2013/MovingAverageData/resultDTW5.csv', 'rU' ) #open train data
for line in f:

    cells = line.split(",")
    e.append((float)(cells[7]))
    indx = indx + 1

    if indx == dtw_data_limit:
        break

f.close()

dist, cost, path = mlpy.dtw_std(a, d, dist_only=False)

print("Distance between 7th and 28th minutes - Two Golas")
print(dist)
print("############")

dist, cost, path = mlpy.dtw_std(b, c, dist_only=False)

print("Distance between 13th and 22nd minutes - Two Goals")
print(dist)
print("############")

dist, cost, path = mlpy.dtw_std(a, e, dist_only=False)

print("Distance between 7th and 5th minutes")
print(dist)
print("############")

dist, cost, path = mlpy.dtw_std(b, e, dist_only=False)

print("Distance between 13th and 5th minutes")
print(dist)
print("############")

