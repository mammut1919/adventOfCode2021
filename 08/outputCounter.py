import numpy as np

inputFile = 'data.txt'

data = np.loadtxt(inputFile, dtype=str, delimiter = "|")

# part 1

count = 0
for inputLine in range (0, len(data)):
    output = ((data[inputLine][1]).split())
    for digit in range (0, 4):
        if (
            len(output[digit]) == 2 # => 1
            or len(output[digit]) == 4 # => 4
            or len(output[digit]) == 3 # => 7
            or len(output[digit]) == 7 # => 8
        ):
            count += 1 

print ('number of unique digits:', count) 


# part 2

result = []
for inputLine in range (0, len(data)):

    code = [[],[],[],[],[],[],[],[],[],[]]

    input = ((data[inputLine][0]).split() + (data[inputLine][1]).split())
    for digit in range (0, 14):
        if ( len(input[digit]) == 2 ): # => 1 
            code[1] = sorted(input[digit])
        if ( len(input[digit]) == 3 ): # => 7 
            code[7] = sorted(input[digit])
        if ( len(input[digit]) == 4 ): # => 4 
            code[4] = sorted(input[digit])
        if ( len(input[digit]) == 7 ): # => 8 
            code[8] = sorted(input[digit])

    #check if 1 is included in len-5-entry => 3
    if ( len(code[1]) == 2 ):
        for digit in range (0, 14):
            if ( len(input[digit]) == 5 ): # => 2 or 3 or 5
                if ( code[1][0] in input[digit] and code[1][1] in input[digit]): # exclude 2 and 5
                    code[3] = sorted(input[digit])
    
    #check if 4 is included in len-6-entry => 9
    if ( len(code[4]) == 4 ):
        for digit in range (0, 14):
            if ( len(input[digit]) == 6 ): # => 6 or 9 or 0
                if ( code[4][0] in input[digit] and code[4][1] in input[digit] and code[4][2] in input[digit] and code[4][3] in input[digit]): # exclude 6 and 0
                    code[9] = sorted(input[digit])

    #check if len-5-array is included in code[9] => 5, else => 2
    if ( len(code[9]) == 6 ):
        for digit in range (0, 14):
            if ( len(input[digit]) == 5 ): # => 2 or 5 or 3
                if (code[3] != sorted(input[digit]) ): # exclude 3
                    if ( input[digit][0] in code[9] and input[digit][1] in code[9] and input[digit][2] in code[9] and input[digit][3] in code[9] and input[digit][4] in code[9] ):
                        code[5] = sorted(input[digit])
                    else:
                        code[2] = sorted(input[digit])

    #check is 5 is included len-6-array => 6, else => 0
    if ( len(code[5]) == 5 and len(code[9]) == 6 ):
        for digit in range (0, 14):
            if ( len(input[digit]) == 6 and sorted(input[digit]) != code[9]): # => 0 or 6
                if ( code[5][0] in input[digit] and code[5][1] in input[digit] and code[5][2] in input[digit] and code[5][3] in input[digit] and code[5][4] in input[digit]) :
                    code[6] = sorted(input[digit])
                else:
                    code[0] = sorted(input[digit])

    temp = 0
    # print(code)
    for output in range (0, 4):
        for codeValue in range (0,10):
            if sorted(input[output+10]) == code[codeValue] :
                temp += codeValue * (10 ** (3-output))
    result.append(temp)

print('sum:', sum(result))