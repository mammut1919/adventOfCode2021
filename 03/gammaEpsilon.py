import numpy as np

gammaRate=[]
epsilonRate=[]

input=[]
with open("data.txt") as data:
    for line in data:
        input.append(str(line))

for j in range (0,12):
    countOne=0
    countZero=0
    for i in range (0, len(input)):

        if ((input[i])[j:j+1] == '0'):
            countZero += 1
        else:
            countOne +=1
    if countOne > countZero:
        gammaRate.append(1)
        epsilonRate.append(0)
    else: 
        gammaRate.append(0)
        epsilonRate.append(1)

gamma=0
epsilon=0
for i in range(0, len(gammaRate)):
    gamma += 2**(11-i) * gammaRate[i]
    epsilon += 2**(11-i) * epsilonRate[i]

print(gamma* epsilon)
