import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.decomposition import PCA

pathToPlayerStats = 'D:\FYP\DEBS2013\PlayerStats/DennisTA.csv'
raw_data = open(pathToPlayerStats, 'rU' ) #open train data

dataset = np.loadtxt(raw_data, delimiter=",")
print(dataset.shape)

# separate the data from the target attributes
X = dataset[:,1:3]
Y = dataset[:,0]

fig = plt.figure(1, figsize=(8, 6))
ax = Axes3D(fig, elev=-150, azim=1000)
X_reduced = PCA(n_components=5).fit_transform(dataset.data)
ax.scatter(X_reduced[:, 2], X_reduced[:, 3], X_reduced[:, 4], c=Y,
           cmap=plt.cm.Paired)

ax.set_title("Player Speed Cluster Map")
ax.set_xlabel("Velocity-X")
ax.w_xaxis.set_ticklabels([])
ax.set_ylabel("Velocity-Y")
ax.w_yaxis.set_ticklabels([])
ax.set_zlabel("Velocity-Z")
ax.w_zaxis.set_ticklabels([])

plt.show()