import numpy as np

movementCommand = np.loadtxt('data.txt', dtype=str, usecols=(0))
movementLength = np.loadtxt('data.txt', usecols=(1))

positionX = 0
positionY = 0
aim = 0

for i in range (0, len(movementCommand)):
    if (movementCommand[i] == 'forward'):
        positionX += movementLength[i]
        positionY += movementLength[i] * -aim
    else:
        if (movementCommand[i] == 'up'):
            aim -= movementLength[i]
        else:
            if (movementCommand[i] == 'down'):
                aim += movementLength[i]
            else:
                print('error')

depth = - positionY

print( positionX * depth )