import numpy as np

crabPositions = np.loadtxt('data.txt', dtype=int, delimiter = ",")

fuel = np.zeros(max(crabPositions)-min(crabPositions))

for finalPosition in range(0, max(crabPositions)):
    for crab in range(0, len(crabPositions)):
        fuel[finalPosition] += abs(crabPositions[crab] - finalPosition)

print(min(fuel))


correctFuel = np.zeros(max(crabPositions)-min(crabPositions))

for finalPosition in range(0, max(crabPositions)):
    for crab in range(0, len(crabPositions)):
        distance = (abs(crabPositions[crab] - finalPosition))
        correctFuel[finalPosition] += (distance * (distance-1) / 2 + distance)

print(min(correctFuel))