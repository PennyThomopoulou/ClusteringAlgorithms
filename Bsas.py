import numpy as np
import math
from sklearn.cluster import KMeans

# prints the whole array instead of the shorter version of it
np.set_printoptions(threshold=np.nan)

# loads the dataset from saveasnumpy
dataset = np.load('dataset.npy')

# maximum number of clusters to create
MAX_CLUSTER_NUMBER = 20

# threshold for how different 2 vectors can be based on their distance
THRESHOLD = 2.45

# finds the euclidean distance between 2 vectors
def FindDistance(vec1, vec2):
    distance = 0
    for i in range(vec1.size):
        distance += (vec1[i]-vec2[i])**2
    distance= math.sqrt(distance)
    return distance

# finds the closest possible cluster from a vector, given the vector itself,
# the current clusters locations and the number of existing clusters
def FindClosestCluster(vec1, clusterPositions, currentClustersNumber):
    numberOfCluster = 0
    minumunClusterDistance = FindDistance(vec1, clusterPositions[0])
    for i in range(currentClustersNumber):
        currentClusterDistance = FindDistance(vec1, clusterPositions[i])
        if (minumunClusterDistance> currentClusterDistance):
            minumunClusterDistance = currentClusterDistance
            numberOfCluster = i
    return numberOfCluster


# BSAS Algorithm
# create empty array for cluster positions of size MaxClustersNumber x DatasetFeatures
clusterPositions = np.arange(MAX_CLUSTER_NUMBER*dataset.shape[1]).reshape(MAX_CLUSTER_NUMBER, dataset.shape[1])

# create empty array of size 100.000(number of ratings), to place the number of cluster each rating belongs to
assignedCluster = np.arange(dataset.size)

clusterPositions[0] = dataset[0]
assignedCluster[0] = 0
currentClustersNumber = 1
max = 0

# for every rating in dataset, find the closest cluster
for i in range(dataset.shape[0]):
    currentClosestCluster = FindClosestCluster(dataset[i],clusterPositions,currentClustersNumber)
    # if that distance is bigger than the assigned threshold, and if the number of max clusters wasn't reached,
    # create new cluster. Otherwise, assign it to the closest cluster
    if(FindDistance(clusterPositions[currentClosestCluster], dataset[i])>THRESHOLD and currentClustersNumber<MAX_CLUSTER_NUMBER):
        clusterPositions[currentClustersNumber] = dataset[i]
        assignedCluster[i] = currentClustersNumber
        currentClustersNumber += 1
    else:
        assignedCluster[i] = currentClosestCluster
print(currentClustersNumber)


