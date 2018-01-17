import numpy as np
import math
from sklearn.cluster import KMeans

np.set_printoptions(threshold=np.nan)

dataset = np.load('dataset.npy')

MAX_CLUSTER_NUMBER = 20
THRESHOLD = 2

def FindDistance(vec1, vec2):
    distance = 0
    for i in range(vec1.size):
        distance += (vec1[i]-vec2[i])**2
    distance= math.sqrt(distance)
    return distance

def FindClosestCluster(vec1, clusterPositions, currentClustersNumber):
    numberOfCluster = 0
    minumunClusterDistance = FindDistance(vec1, clusterPositions[0])
    for i in range(currentClustersNumber):
        currentClusterDistance = FindDistance(vec1, clusterPositions[i])
        if (minumunClusterDistance> currentClusterDistance):
            minumunClusterDistance = currentClusterDistance
            numberOfCluster = i
    return numberOfCluster

#BSAS Algorithm

clusterPositions = np.arange(MAX_CLUSTER_NUMBER*dataset.shape[1]).reshape(MAX_CLUSTER_NUMBER,dataset.shape[1])
assignedCluster = np.arange(dataset.size)

clusterPositions[0] = dataset[0]
assignedCluster[0] = 0
currentClustersNumber = 1
max = 0
for i in range(dataset.shape[0]):
    currentClosestCluster = FindClosestCluster(dataset[i],clusterPositions,currentClustersNumber)
    if(FindDistance(clusterPositions[currentClosestCluster], dataset[i])>THRESHOLD and currentClustersNumber<MAX_CLUSTER_NUMBER):
        clusterPositions[currentClustersNumber] = dataset[i]
        assignedCluster[i] = currentClustersNumber
        currentClustersNumber +=1
    else:
        assignedCluster[i] = currentClosestCluster
print(currentClustersNumber)

#K-Means Algorithm

kmeans = KMeans(n_clusters=currentClustersNumber, random_state=0).fit(dataset)
kmeansLabels = kmeans.labels_
print(kmeans.labels_)
clusterCenters = kmeans.cluster_centers_
print(clusterCenters)
