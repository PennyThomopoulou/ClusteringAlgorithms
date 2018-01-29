import numpy as np
from sklearn.cluster import KMeans

# prints the whole array instead of the shorter version of it
np.set_printoptions(threshold=np.nan)

# loads the dataset from saveasnumpy
dataset = np.load('dataset.npy')

# total cluster number based on the result of BSAS
k = 4

# K-Means Algorithm
# apply k-means with sk learn library, based on the number of clusters we found via BSAS
kmeans = KMeans(n_clusters=k, random_state=0).fit(dataset)

# get the labels for each rating, basically the number of cluster every rating belongs to
kmeansLabels = kmeans.labels_
print(kmeans.labels_)

# get the position of every cluster center
clusterCenters = kmeans.cluster_centers_
print(clusterCenters)
