import numpy as np

inputfile='data.txt'
x1 = np.loadtxt(inputfile, dtype=int, usecols=(0))
y1 = np.loadtxt(inputfile, dtype=int, usecols=(1))
x2 = np.loadtxt(inputfile, dtype=int, usecols=(2))
y2 = np.loadtxt(inputfile, dtype=int, usecols=(3))

size=1000
ocean=np.zeros([size,size])

for i in range (0, len(x1)):
    if (x1[i] != x2[i] and y1[i] == y2[i]):
        if(x2[i] > x1[i]):
            for j in range (x1[i], x2[i]+1):
                ocean[j, y1[i]] += 1
        else:
            for j in range (x2[i], x1[i]+1):
                ocean[j, y1[i]] += 1
    if (x1[i] == x2[i] and y1[i] != y2[i]):
        if(y2[i] > y1[i]):
            for j in range (y1[i], y2[i]+1):
                ocean[x1[i], j] += 1
        else:
            for j in range (y2[i], y1[i]+1):
                ocean[x1[i], j] += 1

# diagonal lines
for i in range (0, len(x1)):
    if (abs(x1[i] - x2[i]) == abs(y1[i] - y2[i])):

        if(x1[i]-x2[i] > 0 and y1[i] - y2[i] > 0):
            for j in range (0, x1[i]-x2[i]+1):
                ocean[x1[i]-j, y1[i]-j] += 1

        if(x1[i]-x2[i] < 0 and y1[i] - y2[i] < 0):
            for j in range (0, x2[i]-x1[i]+1):
                ocean[x1[i]+j, y1[i]+j] += 1

        if(x1[i]-x2[i] > 0 and y1[i] - y2[i] < 0):
            for j in range (0, x1[i]-x2[i]+1):
                ocean[x1[i]-j, y1[i]+j] += 1

        if(x1[i]-x2[i] < 0 and y1[i] - y2[i] > 0):
            for j in range (0, x2[i]-x1[i]+1):
                ocean[x1[i]+j, y1[i]-j] += 1

count=0
for i in range (0,size):
    for j in range(0,size):
        if ocean[i,j]>1:
            count += 1

print(count)