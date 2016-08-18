from sklearn.cluster import DBSCAN
from sklearn import preprocessing
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("D:/FYP-Developments/Dataset-Kaggale/trainNew.csv")

data = data[["f", "k"]]
print(data)
data = data.as_matrix().astype("float32", copy = False)

stscaler = preprocessing.StandardScaler().fit(data)
data = stscaler.transform(data)

#print(data)

dbsc = DBSCAN(eps = .5, min_samples = 15).fit(data)

labels = dbsc.labels_
#print(labels)
core_samples = np.zeros_like(labels, dtype = bool)
#print(core_samples)
core_samples[dbsc.core_sample_indices_] = True
#print(dbsc.core_sample_indices_)

print(data)
print("###########")

n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)


##############################################################################
# Plot result
import matplotlib.pyplot as plt

# Black removed and is used for noise instead.
unique_labels = set(labels)
colors = plt.cm.Spectral(np.linspace(0, 1, len(unique_labels)))
for k, col in zip(unique_labels, colors):
    if k == -1:
        # Black used for noise.
        col = 'k'

    class_member_mask = (labels == k)

    xy = data[class_member_mask & core_samples]
    #print(xy[:,1])
    plt.figure("class_member_mask & core_samples")
    plt.plot(xy[:, 0], xy[:,1], 'o', markerfacecolor=col,
             markeredgecolor='k', markersize=14)

    xy = data[class_member_mask & ~core_samples]

    plt.figure("class_member_mask & ~core_samples")
    plt.plot(xy[:, 0], xy[:,1], 'o', markerfacecolor=col,
             markeredgecolor='k', markersize=6)

#plt.title('Estimated number of clusters: %d' % n_clusters_)
plt.show()

# plt.plot(dbsc.components_)
# plt.show()



