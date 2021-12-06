import numpy as np

laternfishPopulation = np.loadtxt('data.txt', dtype=int, delimiter = ",")

laternFishAge = [0,0,0,0,0,0,0,0,0,0,0]

for laternfish in laternfishPopulation:
    laternFishAge[laternfish] += 1

for day in range (0,255):

    for i in range(1,11):
        laternFishAge[i-1] = laternFishAge[i]

    laternFishAge[7] += laternFishAge[0]
    laternFishAge[9] = laternFishAge[0]
    laternFishAge[0] = 0

print(sum(laternFishAge))
