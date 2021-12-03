import numpy as np 
import matplotlib.pyplot as plt

# day 1: scan of ground data
scanData = np.loadtxt('../01/data.txt', usecols=(0))

# day 2: submarine movement
movementCommand = np.loadtxt('../02/data.txt', dtype=str, usecols=(0))
movementLength = np.loadtxt('../02/data.txt', usecols=(1))

positionX = [0]
positionY = [0]

for i in range (0, len(movementCommand)):
    if (movementCommand[i] == 'forward'):
        positionX.append( positionX[i] + movementLength[i] )
        positionY.append( positionY[i] )
    else:
        if (movementCommand[i] == 'up'):
            positionX.append( positionX[i] )
            positionY.append( positionY[i] + movementLength[i] )
        else:
            if (movementCommand[i] == 'down'):
                positionX.append( positionX[i] )
                positionY.append( positionY[i] - movementLength[i] )
            else:
                print('error')

improvedPositionX = [0]
improvedPositionY = [0]
aim = 0

for i in range (0, len(movementCommand)):
    if (movementCommand[i] == 'forward'):
        improvedPositionX.append( positionX[i] + ( movementLength[i] * np.cos(-+aim * np.pi / 360 )))
        improvedPositionY.append( positionY[i] + ( movementLength[i] * -np.sin(-aim * np.pi / 360 )))
    else:
        if (movementCommand[i] == 'up'):
            aim -= movementLength[i]
        else:
            if (movementCommand[i] == 'down'):
                aim += movementLength[i]
            else:
                print('error')

# data for plots
plt.plot(-scanData, label='ground')
plt.plot(positionX, positionY, label="submarine route", )
plt.plot(improvedPositionX, improvedPositionY, label="improved submarine route", )

# plot 1
plt.title('Advent of Code 2021 - Submarine over ground')
plt.xlabel('distance / m')
plt.ylabel('depth / m')
plt.legend()
#plt.show()
plt.savefig('submarine_over_ground.png')

# plot 2 - zoomed in
plt.title('Advent of Code 2021 - Compare submarine routes')
plt.xlabel('distance / m')
plt.ylabel('depth / m')
plt.ylim(-1000, 0)
plt.legend()
#plt.show()
plt.savefig('compare_submarine_routes.png')

