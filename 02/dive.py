import numpy as np

movementCommand = np.loadtxt('data.txt', dtype=str, usecols=(0))
movementLength = np.loadtxt('data.txt', usecols=(1))

positionX = 0
positionY = 0

for i in range (0, len(movementCommand)):
    if (movementCommand[i] == 'forward'):
        positionX += movementLength[i]
    else:
        if (movementCommand[i] == 'up'):
            positionY += movementLength[i]
        else:
            if (movementCommand[i] == 'down'):
                positionY -= movementLength[i]
            else:
                print('error')

depth = - positionY

print( positionX * depth )