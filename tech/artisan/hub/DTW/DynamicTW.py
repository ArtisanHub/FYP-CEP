import mlpy
import matplotlib.pyplot as plt
import matplotlib.cm as cm
a = []
b = []

indx = 0
dtw_data_limit = 50000
f = open( '', 'rU' ) #Provide dataset 1 file path for comparison
for line in f:

    cells = line.split(",")
    a.append((float)(cells["X"])) #X = Provide the respective column of the dataset which needs to be analysed
    indx = indx + 1

    if indx == dtw_data_limit:
        break

f.close()

indx = 0
f = open( '', 'rU' ) #Provide dataset 2 file path for comparison
for line in f:

    cells = line.split(",")
    b.append((float)(cells["X"])) #X = Provide the respective column of the dataset which needs to be analysed
    indx = indx + 1

    if indx == dtw_data_limit:
        break

f.close()

dist, cost, path = mlpy.dtw_std(a, b, dist_only=False)

print("Distance between a and b temporal sequneces")
print(dist)
print("############")

#End - Distance Calculation

#Start - Plot

plt.figure("Two temporal sequnences")
plt.plot(a)
plt.plot(b)

fig = plt.figure("Accumulated Cost Matrix & warping path")
ax = fig.add_subplot("ACM & WP")
plot1 = plt.imshow(cost.T, origin='lower', cmap=cm.plasma, interpolation='nearest')
plot2 = plt.plot(path[0], path[1], 'w')
xlim = ax.set_xlim((-0.5, cost.shape[0]-0.5))
ylim = ax.set_ylim((-0.5, cost.shape[1]-0.5))

#End - Plot

plt.show()

