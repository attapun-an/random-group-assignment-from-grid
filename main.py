import random

groups = 4
rows = 5
cols = 5
total = rows*cols
each = groups/4


avail_ = []
for x in range(cols):
    for y in range(rows):
        avail_.append([x,y])


# to store indexes that have already been generated
c = []
# g is a counter that will increment every time a group is completed
generated = []


def searchforitem(item, arr):
    flag = False
    for i in range(len(arr)):
        if arr[i] == item:
            flag = True
    return flag


while len(c) < total:
    r = random.randint(0,total-1)
    exist = searchforitem(r, c)
    if exist == False:
        c.append(r)
        generated.append(avail_[r])

g = 1
for item in generated:

