scanData = []
with open("data.txt") as data:
    for line in data:
        scanData.append(int(line))

increaseCount = 0
for i in range (3, len(scanData)):
    if ( scanData[i-2]+scanData[i-1]+scanData[i] > scanData[i-3]+scanData[i-2]+scanData[i-1] ):
        increaseCount += 1

print(increaseCount)
