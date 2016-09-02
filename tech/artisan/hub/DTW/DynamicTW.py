import mlpy
import matplotlib.pyplot as plt
import matplotlib.cm as cm
a = [1,2,3,4]
b = [5,3,5,2]
# c = []
# d = []
# e = []

# indx = 0
# dtw_data_limit = 50000
# f = open( 'D:/FYP-Developments/Dataset-Debs-2013/MovingAverageData/resultDTW1.csv', 'rU' ) #open train data
# for line in f:
#
#     cells = line.split(",")
#     a.append((float)(cells[7]))
#     indx = indx + 1
#
#     if indx == dtw_data_limit:
#         break
#
# f.close()
#
# indx = 0
# f = open( 'D:/FYP-Developments/Dataset-Debs-2013/MovingAverageData/resultDTW2.csv', 'rU' ) #open train data
# for line in f:
#
#     cells = line.split(",")
#     b.append((float)(cells[7]))
#     indx = indx + 1
#
#     if indx == dtw_data_limit:
#         break
#
# f.close()

# indx = 0
# f = open( 'D:/FYP-Developments/Dataset-Debs-2013/MovingAverageData/resultDTW3.csv', 'rU' ) #open train data
# for line in f:
#
#     cells = line.split(",")
#     c.append((float)(cells[7]))
#     indx = indx + 1
#
#     if indx == dtw_data_limit:
#         break
#
# f.close()
#
# indx = 0
# f = open( 'D:/FYP-Developments/Dataset-Debs-2013/MovingAverageData/resultDTW4.csv', 'rU' ) #open train data
# for line in f:
#
#     cells = line.split(",")
#     d.append((float)(cells[7]))
#     indx = indx + 1
#
#     if indx == dtw_data_limit:
#         break
#
# f.close()
#
# indx = 0
# f = open( 'D:/FYP-Developments/Dataset-Debs-2013/MovingAverageData/resultDTW5.csv', 'rU' ) #open train data
# for line in f:
#
#     cells = line.split(",")
#     e.append((float)(cells[7]))
#     indx = indx + 1
#
#     if indx == dtw_data_limit:
#         break
#
# f.close()

dist, cost, path = mlpy.dtw_std(a, b, dist_only=False)

print("Distance between a and b temporal sequneces")
print(dist)
print("############")


plt.figure("Two temporal sequnences")
plt.plot(a)
plt.plot(b)

fig = plt.figure("Accumulated Cost Matrix & warping path")
ax = fig.add_subplot("ACM & WP")
plot1 = plt.imshow(cost.T, origin='lower', cmap=cm.plasma, interpolation='nearest')
plot2 = plt.plot(path[0], path[1], 'w')
xlim = ax.set_xlim((-0.5, cost.shape[0]-0.5))
ylim = ax.set_ylim((-0.5, cost.shape[1]-0.5))


plt.show()

