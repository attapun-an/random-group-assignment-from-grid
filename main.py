import random

groups = 5
rows = 5
cols = 5
total = rows*cols
each = total/groups


avail_ = []
for x in range(cols):
    for y in range(rows):
        avail_.append([x+1,y+1])


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
# is a counter that gets reset every time a group is filled
n = 0
t = 0
while g <= groups:
    print(g)
    temp = []
    while n < each:
        temp.append(generated[t])
        n += 1
        t += 1
    n = 0
    g += 1
    print(temp)


