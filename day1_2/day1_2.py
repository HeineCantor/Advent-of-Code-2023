numberDict = {
    "one" : 1,
    "two" : 2,
    "three" : 3,
    "four" : 4,
    "five" : 5,
    "six" : 6,
    "seven" : 7,
    "eight" : 8,
    "nine" : 9,
}

if __name__ == "__main__":
    inputFile = open("input.txt")

    line = inputFile.readline().strip()

    sum = 0

    while line:
        numList = []

        i = 0
        while i < len(line):
            char = line[i]

            if('0' <= char <= '9'):
                numList.append(int(char))
            else:
                for numericElement in numberDict:
                    if(line[i:i+len(numericElement)] == numericElement):
                        numList.append(numberDict[numericElement])
                        break

            i+=1

        value = numList[0]*10+numList[-1]
        sum+=value

        line = inputFile.readline().strip()

    print(sum)