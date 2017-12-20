import numpy as np
def changedate(monthnumber,data):
    day = int(data[:-9])
    month = int(monthnumber)
    year = int(data[7:])
    date = day-1+(month-1)*30+(year-1922)*365
    return date
np.set_printoptions(threshold=np.nan)
dataset = np.load('dataset.npy')

print dataset[0]

for data in dataset:
    if data[1] == 'M':
        data[1] = 0
    elif data[1] == 'F':
        data[1] = 1
    month = data[23][3:-5]
    temp = data[23]
    if temp == '':
        print data
    if month == 'Jan':
        data[23] = changedate(1,data[23])
    if month == 'Feb':
        data[23] = changedate(2,data[23])
    if month == 'Mar':
        data[23] = changedate(3,data[23])
    if month == 'Apr':
        data[23] = changedate(4,data[23])
    if month == 'May':
        data[23] = changedate(5,data[23])
    if month == 'Jun':
        data[23] = changedate(6,data[23])
    if month == 'Jul':
        data[23] = changedate(7,data[23])
    if month == 'Aug':
        data[23] = changedate(8,data[23])
    if month == 'Sep':
        data[23] = changedate(9,data[23])
    if month == 'Oct':
        data[23] = changedate(10,data[23])
    if month == 'Nov':
        data[23] = changedate(11,data[23])
    if month == 'Dec':
        data[23] = changedate(12,data[23])
    #print len(data)

    for minidata in data:
        #print i
        if type(minidata) != int:
            if type(minidata) == str:
                if not minidata:
                    print data[23]
                else:
                    minidata = int(minidata)





    #print data
#print(dataset[1])
