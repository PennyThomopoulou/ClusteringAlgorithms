import numpy as np

ratings = np.arange(400000).reshape(100000,4)

#Read all the ratings
fileStream = open('u.data','r')
lines = fileStream.readlines()
i= 0
for line in lines:
    ratings[i]= line.split("\t")
    i+=1
fileStream.close()
#print(ratings)



#Read all users
users = np.zeros((943,5), dtype=object)

fileStream = open('u.user','r')
lines = fileStream.readlines()
i= 0
lines = [line.strip() for line in lines]
for line in lines:
    users[i]= line.split("|")
    i+=1
fileStream.close()


#assign occupations
fullusers = np.zeros((943,25), dtype = object)
i = 0
for user in users:
    fullusers[i][0] = user[0]
    fullusers[i][1] = user[1]
    fullusers[i][2] = user[2]
    fullusers[i][24] = user[4]
    if user[3] == 'administrator':
        fullusers[i][3] = 1
    elif user[3] == 'artist':
        fullusers[i][4] = 1
    elif user[3] == 'doctor':
        fullusers[i][5] = 1
    elif user[3] == 'educator':
        fullusers[i][6] = 1
    elif user[3] == 'engineer':
        fullusers[i][7] = 1
    elif user[3] == 'entertainment':
        fullusers[i][8] = 1
    elif user[3] == 'executive':
        fullusers[i][9] = 1
    elif user[3] == 'healthcare':
        fullusers[i][10] = 1
    elif user[3] == 'homemaker':
        fullusers[i][11] = 1
    elif user[3] == 'lawyer':
        fullusers[i][12] = 1
    elif user[3] == 'librarian':
        fullusers[i][13] = 1
    elif user[3] == 'marketing':
        fullusers[i][14] = 1
    elif user[3] == 'none':
        fullusers[i][15] = 1
    elif user[3] == 'other':
        fullusers[i][16] = 1
    elif user[3] == 'programmer':
        fullusers[i][17] = 1
    elif user[3] == 'retired':
        fullusers[i][18] = 1
    elif user[3] == 'salesman':
        fullusers[i][19] = 1
    elif user[3] == 'scientist':
        fullusers[i][20] = 1
    elif user[3] == 'student':
        fullusers[i][21] = 1
    elif user[3] == 'technician':
        fullusers[i][22] = 1
    elif user[3] == 'writer':
        fullusers[i][23] = 1
    i+=1
#print(fullusers)


#Read all movies

movies = np.zeros((1682,24), dtype=object)

fileStream = open('u.item','r')
lines = fileStream.readlines()
i= 0
lines = [line.strip() for line in lines]
for line in lines:
    movies[i]= line.split("|")
    i+=1
fileStream.close()

print(movies)

dataset = np.zeros((100000,45),dtype= object)
i = 0
for rating in ratings:
    dataset[i][43] = rating[2]
    dataset[i][44] = rating[3]
    userid = rating[0]-1
    for j in range(23):
        dataset[i][j] = fullusers[userid][j+1]
    movieid = rating[1]-1
    dataset[i][23] = movies[movieid][2]
    for j in range(18):
        dataset[i][j+25] = movies[movieid][j+5]
    i+=1

for i in range (100000):
    for j in range (45):
        if (dataset[i][j] == ''):
            print i
            print j
print (dataset[99999])

np.save('dataset.npy',dataset)