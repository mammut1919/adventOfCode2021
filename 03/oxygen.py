import numpy as np

input=[]
with open("data.txt") as data:
    for line in data:
        input.append(str(line))

oxygen = input
for j in range (0,12):
    countOne=0
    countZero=0
    for i in range (0, len(oxygen)):
        if ((oxygen[i])[j:j+1] == '0'):
            countZero += 1
        else:
            countOne +=1

    temp=[]
    for i in range (0, len(oxygen)):
        if (countZero > countOne):
            if((oxygen[i])[j:j+1] == '0'):
                temp.append(oxygen[i])
        else:
            if((oxygen[i])[j:j+1] == '1'):
                temp.append(oxygen[i])
    oxygen=temp

    if len(oxygen)==1:
        oxygenResult=oxygen[0]

co2=input
for j in range (0,12):
    countOne=0
    countZero=0
    for i in range (0, len(co2)):
        if ((co2[i])[j:j+1] == '0'):
            countZero += 1
        else:
            countOne +=1

    temp=[]
    for i in range (0, len(co2)):
        if (countZero <= countOne):
            if((co2[i])[j:j+1] == '0'):
                temp.append(co2[i])
        else:
            if((co2[i])[j:j+1] == '1'):
                temp.append(co2[i])
    co2=temp

    if len(co2)==1:
        co2Result = co2[0]

oxygenArray=[]
co2Array=[]
for i in range (0, 12):
    if(oxygenResult[i:i+1]=='0'):
        oxygenArray.append(0)
    else:
        oxygenArray.append(1)
    if(co2Result[i:i+1]=='0'):
        co2Array.append(0)
    else:
        co2Array.append(1)


oxygenOutput=0
co2Output=0
for i in range(0, len(oxygenArray)):
    oxygenOutput += 2**(11-i) * oxygenArray[i]
    co2Output += 2**(11-i) * co2Array[i]

print(oxygenOutput* co2Output)