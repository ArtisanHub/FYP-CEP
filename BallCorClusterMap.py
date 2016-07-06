import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn import datasets
from sklearn.decomposition import PCA



raw_data = open( 'D:/FYP/DEBS2013/BallData/test.csv', 'rU' ) #open train data

dataset = np.loadtxt(raw_data, delimiter=",")
print(dataset.shape)

# separate the data from the target attributes
X = dataset[:,1:3]
Y = dataset[:,0]

fig = plt.figure(1, figsize=(8, 6))
ax = Axes3D(fig, elev=-150, azim=1000)
X_reduced = PCA(n_components=4).fit_transform(dataset.data)
ax.scatter(X_reduced[:, 1], X_reduced[:, 2], X_reduced[:, 3], c=Y,
           cmap=plt.cm.Paired)

ax.set_title("Ball Coordinates Cluster Map")
ax.set_xlabel("X-Coordinate")
ax.w_xaxis.set_ticklabels([])
ax.set_ylabel("Y-Coordinate")
ax.w_yaxis.set_ticklabels([])
ax.set_zlabel("Z-Coordinate")
ax.w_zaxis.set_ticklabels([])

plt.show()