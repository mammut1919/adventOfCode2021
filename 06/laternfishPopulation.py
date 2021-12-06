import numpy as np

laternfishPopulation = np.loadtxt('data.txt', dtype=int, delimiter = ",")

for day in range (0,80):
    newLaternfishNumber = 0
    print('day', day)
    for laternfish in range (0, len(laternfishPopulation)):
        laternfishPopulation[laternfish] -= 1
        if (laternfishPopulation[laternfish] == 0):
            laternfishPopulation[laternfish] = 6
            newLaternfishNumber += 1
    print(newLaternfishNumber, 'new lantern fish appeared')
    for newLanternfish in range (0, newLaternfishNumber):
        laternfishPopulation = np.append(laternfishPopulation, 8)


print (len(laternfishPopulation))