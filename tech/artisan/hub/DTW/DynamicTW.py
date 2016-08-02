import mlpy
import matplotlib.pyplot as plt
import matplotlib.cm as cm
x = []
y = []

indx = 0

f = open( 'D:/FYP-Developments/Dataset-Debs-2013/MovingAverageData/resultDTW1.csv', 'rU' ) #open train data
for line in f:

    cells = line.split(",")
    x.append((float)(cells[7]))
    indx = indx + 1

    if indx == 10000:
        break

f.close()

indx = 0
f = open( 'D:/FYP-Developments/Dataset-Debs-2013/MovingAverageData/resultDTW2.csv', 'rU' ) #open train data
for line in f:

    cells = line.split(",")
    y.append((float)(cells[7]))
    indx = indx + 1

    if indx == 10000:
        break

f.close()

dist, cost, path = mlpy.dtw_std(x, y, dist_only=False)
mlpy.dtw_subsequence
print("############")
print(dist)
print("############")

dist
0.0

fig = plt.figure("DTW")
ax = fig.add_subplot(111)
plot1 = plt.imshow(cost.T, origin='lower', cmap=cm.plasma, interpolation='nearest')
plot2 = plt.plot(path[0], path[1], 'w')
xlim = ax.set_xlim((-0.5, cost.shape[0]-0.5))
ylim = ax.set_ylim((-0.5, cost.shape[1]-0.5))


plt.figure("Path Analysis")
plt.plot(path[0])
plt.plot(path[1])

plt.show()