from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
import numpy as np
from scipy.cluster.hierarchy import fcluster

# importing dataset from saveasnumpy
dataset = np.load('dataset.npy')

# reducing the size of dataset to the first 1000 ratings
X = dataset[:-99000]

# creating links between ratings(vectors) based on ward linking
Z = linkage(X, 'ward')

# calculating full dendrogram
plt.figure(figsize=(25, 10))
plt.title('Hierarchical Clustering Dendrogram')
plt.xlabel('sample index')
plt.ylabel('distance')
dendrogram(
    Z,
    leaf_rotation=90.,  # rotates the x axis labels
    leaf_font_size=8.,  # font size for the x axis labels
)
plt.show()

# maximum number of clusters, based on BSAS algorithm
k = 4

# get clusters based on k
clusters = fcluster(Z, k, criterion='maxclust')

# print on which number of clusters each rating belongs to
print(clusters)
