scanData = []
with open("data.txt") as data:
    for line in data:
        scanData.append(int(line))

increaseCount = 0

for i in range (1, len(scanData)):
    if (scanData[i] > scanData[i-1]):
        increaseCount += 1

print(increaseCount)
