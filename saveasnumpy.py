import numpy as np

np.set_printoptions(threshold=np.nan)

ratings = np.arange(400000).reshape(100000, 4)

#Read all the ratings
fileStream = open('u.data', 'r')
lines = fileStream.readlines()
i= 0
for line in lines:
    ratings[i]= line.split("\t")
    i += 1
fileStream.close()
#print(ratings)

#Read all users
users = np.zeros((943, 5), dtype=object)

fileStream = open('u.user', 'r')
lines = fileStream.readlines()
i= 0
lines = [line.strip() for line in lines]
for line in lines:
    users[i]= line.split("|")
    i+=1
fileStream.close()

#Read all movies

movies = np.zeros((1682,24), dtype=object)

fileStream = open('u.item', 'r')
lines = fileStream.readlines()
i= 0
lines = [line.strip() for line in lines]
for line in lines:
    movies[i]= line.split("|")
    i+=1
fileStream.close()

dataset = np.zeros((100000, 19), dtype=float)
i = 0
for rating in ratings:
    movieId = rating[1] - 1

    for j in range(18):
        dataset[i][j] = movies[movieId][j + 6]

    dataset[i][18] = rating[2]*0.25-0.25
    i += 1
print(dataset)

np.save('dataset.npy', dataset)
