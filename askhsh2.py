import numpy as np
def changedate(monthnumber,data):
    day = int(data[:-9])
    month = int(monthnumber)
    year = int(data[7:])
    date = day-1+(month-1)*30+(year-1922)*365
    return date
np.set_printoptions(threshold=np.nan)
dataset = np.load('dataset.npy')
print(dataset[0][24])
for data in dataset:
    if data[1] == 'M':
        data[1] = 0
    elif data[1] == 'F':
        data[1] = 1
    month = data[24][3:-5]
    if month == 'Jan':
        data[24] = changedate(1,data[24])
    if month == 'Feb':
        data[24] = changedate(2,data[24])
    if month == 'Mar':
        data[24] = changedate(3,data[24])
    if month == 'Apr':
        data[24] = changedate(4,data[24])
    if month == 'May':
        data[24] = changedate(5,data[24])
    if month == 'Jun':
        data[24] = changedate(6,data[24])
    if month == 'Jul':
        data[24] = changedate(7,data[24])
    if month == 'Aug':
        data[24] = changedate(8,data[24])
    if month == 'Sep':
        data[24] = changedate(9,data[24])
    if month == 'Oct':
        data[24] = changedate(10,data[24])
    if month == 'Nov':
        data[24] = changedate(11,data[24])
    if month == 'Dec':
        data[24] = changedate(12,data[24])
    data = data[23:]
print(dataset[0])
